from masterchess.models import Game


class ChessGame:
    def __init__(self, collation, id_game):
        self.id_game = id_game
        self.collation = collation
        self.list_of_figures = []
        self.first_click_x = 0
        self.first_click_y = 0
        self.second_click_x = 0
        self.second_click_y = 0
        self.checked_movement = False

    def figure_on_position(self, x, y):  #return figure instance on position x, y
        for i in self.list_of_figures:
            if i.x == x and i.y == y:
                return self.list_of_figures[self.list_of_figures.index(i)]
        return False

    def is_enemy_or_free_square(self, x, y, type_of_asking_figure):
        if type_of_asking_figure.isupper():
            if self.collation[y][x] in 'rkbqtpn':
                return True
            else:
                return False

        elif type_of_asking_figure.islower():
            if self.collation[y][x] in 'RKBQTPn':
                return True
            else:
                return False



    def move(self, first_click_x, first_click_y, second_click_x, second_click_y):
        self.first_click_x = first_click_x
        self.first_click_y = first_click_y
        self.second_click_x = second_click_x
        self.second_click_y = second_click_y
        if self.collation[first_click_y][first_click_x] != 'n':
            figure_instance = self.figure_on_position(first_click_x, first_click_y)
            self.checked_movement = figure_instance.check_movement(first_click_x, first_click_y, second_click_x, second_click_y)
            if self.checked_movement:
                self.move_figure(figure_instance)

    def move_figure(self, figure_instance):
        self.collation[self.second_click_y][self.second_click_x] = figure_instance.type_of_figure
        self.collation[self.first_click_y][self.first_click_x] = 'n'
        collation_to_string = ''
        for i in range(0, 8):
            collation_to_string += ''.join(self.collation[i])
        game_obj = Game.objects.get(id=self.id_game)
        game_obj.game_collation = collation_to_string
        game_obj.save()


