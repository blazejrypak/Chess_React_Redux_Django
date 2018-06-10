from .figure import Figure


class Pawn(Figure):
    def __init__(self, x, y, type_of_figure, game):
        self.game = game
        Figure.__init__(self, x, y, type_of_figure, game)

    # if there is figure in path=>return False
    def check_front_path(self, first_click_x, first_click_y, second_click_y):
        for i in range(first_click_y+1, second_click_y):  #(second_click_y) cause of on position second_click_y plus one could be enemy
            if self.game.collation[i][first_click_x] != 'n':
                return False
        return True

    def check_movement(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if self.check_front_path(first_click_x, first_click_y, second_click_y) and self.game.is_enemy_or_free_square(second_click_x, second_click_y, self.type_of_figure):
            if first_click_x == second_click_x and abs(second_click_y-first_click_y) == 2 and (first_click_y == 1 or first_click_y == 6):
                return True
            else:
                if first_click_x == second_click_x and second_click_y-first_click_y == 1 and self.type_of_figure == 'P':
                    return True
                elif first_click_x == second_click_x and first_click_y-second_click_y == 1 and self.type_of_figure == 'p':
                    return True
            return False

