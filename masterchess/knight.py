from .figure import Figure


class Knight(Figure):
    def __init__(self, x, y, type_of_figure, game):
        self.game = game
        Figure.__init__(self, x, y, type_of_figure, game)

    def check_movement(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if self.game.is_enemy_or_free_square(second_click_x, second_click_y, self.type_of_figure):
            if pow(abs(second_click_x-first_click_x), 2) + pow(abs(second_click_y-first_click_y), 2) == 5:
                return True
            return False

