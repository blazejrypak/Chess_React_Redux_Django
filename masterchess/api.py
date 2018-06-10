from rest_framework import viewsets, permissions

from .models import Game, Move
from .serializers import GameSerializers, MoveSerializers
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .chess_game import ChessGame
from .create_figures import CreateFigures
from pprint import pprint


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    permissions_classes = [permissions.AllowAny, ]
    serializer_class = GameSerializers


class MoveViewSet(viewsets.ViewSet):

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

def new_game(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        new__game = "RKBQTBKRPPPPPPPPnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnpppppppprkbqtbkr"
        obj = Game(game_collation=new__game)
        obj.save()
        serializer = GameSerializers(obj)
        return JsonResponse(serializer.data)

