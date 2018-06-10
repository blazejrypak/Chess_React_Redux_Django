from .figure import Figure


class Bishop(Figure):
    def __init__(self, x, y, type_of_figure, game):
        Figure.__init__(self, x, y, type_of_figure, game)
        self.game = game

    def check_front_path(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if first_click_x < second_click_x and first_click_y > second_click_y:
            a = first_click_x+1
            b = first_click_y-1
            while a != second_click_x and b != second_click_y:
                if self.game.collation[b][a] != 'n':
                    return False
                a += 1
                b -= 1
            return True

        elif first_click_x < second_click_x and first_click_y < second_click_y:
            a = first_click_x+1
            b = first_click_y+1
            while a != second_click_x and b != second_click_y:
                if self.game.collation[b][a] != 'n':
                    return False
                a += 1
                b += 1
            return True

        elif first_click_x > second_click_x and first_click_y < second_click_y:
            a = first_click_x-1
            b = first_click_y+1
            while a != second_click_x and b != second_click_y:
                if self.game.collation[b][a] != 'n':
                    return False
                a -= 1
                b += 1
            return True

        elif first_click_x > second_click_x and first_click_y > second_click_y:
            a = first_click_x-1
            b = first_click_y-1
            while a != second_click_x and b != second_click_y:
                if self.game.collation[b][a] != 'n':
                    return False
                a -= 1
                b -= 1
            return True

    def check_movement(self, first_click_x, first_click_y, second_click_x, second_click_y):
        if abs(second_click_x-first_click_x) == abs(second_click_y-first_click_y):
            if self.check_front_path(first_click_x, first_click_y, second_click_x,
                                     second_click_y) and self.game.is_enemy_or_free_square(
                    second_click_x, second_click_y, self.type_of_figure):
                return True
            return False

