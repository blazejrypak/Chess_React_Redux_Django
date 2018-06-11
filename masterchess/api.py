from rest_framework import viewsets, permissions, generics

from .models import Game, Move
from .serializers import GameSerializers, MoveSerializers

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .chess_game import ChessGame
from .create_figures import CreateFigures
from pprint import pprint

from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegistrationApi(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class GameViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated, ]
    serializer_class = GameSerializers

    def get_queryset(self):
        return self.request.user.games.all()

    def perform_create(self, serializer):
        game_col = "RKBQTBKRPPPPPPPPnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnpppppppprkbqtbkr"
        serializer.save(game_collation=game_col, user=self.request.user)


class MoveViewSet(viewsets.ViewSet):
    permissions_classes = [permissions.IsAuthenticated, ]

    def list(self, request):
        queryset = Move.objects.all()
        serializer = MoveSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        move_obj = Move(pos_from=request.data.get('pos_from'), pos_to=request.data.get('pos_to'), game=request.data.get('game'))
        move_obj.save()
        first_click_x = move_obj.pos_from % 10
        first_click_y = ((move_obj.pos_from - (move_obj.pos_from % 10))/10)-1  #set zero position cause i'am receiving lowest y_pos 1
        second_click_x = move_obj.pos_to % 10
        second_click_y = ((move_obj.pos_to - (move_obj.pos_to % 10))/10)-1  #same problem as above


        chess_game_collation = Game.objects.get(id=move_obj.game).game_collation
    # chess_game_collation from unicode to 2D array
        new_array_collation = []
        row = []
        for index, item in enumerate(chess_game_collation):
            row.append(chr(ord(item)))
            if len(row) == 8:
                new_array_collation.append(row)
                row = []
        game_instance = ChessGame(new_array_collation, move_obj.game)
        create_figures_instance = CreateFigures(game_instance)
        create_figures_instance.create_figures()
        game_instance.move(first_click_x, first_click_y, second_click_x, second_click_y)

        del chess_game_collation
        del game_instance
        del create_figures_instance
        serializer = MoveSerializers(move_obj)
        return JsonResponse(serializer.data)

