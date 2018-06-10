# main class for figure


class Figure:
    def __init__(self, x, y, type_of_figure, game):
        self.game = game
        self.type_of_figure = type_of_figure
        self.x = x
        self.y = y

    def deleteFigure(self, x, y):
        for i in self.game.check_same_type_of_team:
            if x == self.game.second_click_x and y == self.game.second_click_y:
                del self.game.list_of_figures[self.game.list_of_figures.index(i)]
