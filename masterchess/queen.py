from .figure import Figure
from .rook import Rook
from .bishop import Bishop


class Queen(Rook, Bishop, Figure):
    def __init__(self, x, y, type_of_figure, game):
        Figure.__init__(self, x, y, type_of_figure, game)
        self.game = game

    # if there is figure in path=>return False
    def check_front_path(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if Rook.check_front_path(self, first_click_x, first_click_y, second_click_x, second_click_y):
            if Bishop.check_front_path(self, first_click_x, first_click_y, second_click_x, second_click_y):
                return True
        return False

    def check_movement(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if self.check_front_path(first_click_x, first_click_y, second_click_x, second_click_y) and self.game.is_enemy_or_free_square(second_click_x, second_click_y, self.type_of_figure):
            return True
        return False
