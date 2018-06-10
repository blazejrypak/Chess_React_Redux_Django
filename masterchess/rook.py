from .figure import Figure


class Rook(Figure):
    def __init__(self, x, y, type_of_figure, game):
        Figure.__init__(self, x, y, type_of_figure, game)
        self.game = game

    # if there is figure in path=>return False
    def check_front_path(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if first_click_x == second_click_x:
            if second_click_y > first_click_y:
                for i in range(first_click_y+1, second_click_y):
                    if self.game.collation[i][first_click_x] != 'n':
                        return False
                return True
            else:
                for i in range(second_click_y, first_click_y):
                    if self.game.collation[i][first_click_x] != 'n':
                        return False
                return True
        elif first_click_y == second_click_y:
            if second_click_x < first_click_x:
                for i in range(second_click_x+1, first_click_x):
                    print(self.game.collation[first_click_y][i])
                    if self.game.collation[first_click_y][i] != 'n':
                        return False
                return True
            else:
                print(first_click_x, second_click_x)
                for i in range(first_click_x+1, second_click_x):
                    if self.game.collation[first_click_y][i] != 'n':
                        return False
                return True

    def check_movement(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if self.check_front_path(first_click_x, first_click_y, second_click_x, second_click_y) and self.game.is_enemy_or_free_square(second_click_x, second_click_y, self.type_of_figure):
            if first_click_x == second_click_x or first_click_y == second_click_y:
                return True
            return False
