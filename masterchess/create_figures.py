from .rook import Rook
from .knight import Knight
from .bishop import Bishop
from .king import King
from .queen import Queen
from .pawn import Pawn


class CreateFigures:
    def __init__(self, chess_game):
        self.game = chess_game

    def type_of_the_figure(self, name, x, y, chess_game):
        return {
            'R': Rook(x, y, name, chess_game),
            'K': Knight(x, y, name, chess_game),
            'B': Bishop(x, y, name, chess_game),
            'Q': Queen(x, y, name, chess_game),
            'T': King(x, y, name, chess_game),
            'r': Rook(x, y, name, chess_game),
            'k': Knight(x, y, name, chess_game),
            'b': Bishop(x, y, name, chess_game),
            'q': Queen(x, y, name, chess_game),
            't': King(x, y, name, chess_game),
            'p': Pawn(x, y, name, chess_game),
            'P': Pawn(x, y, name, chess_game),
        }[name]

    def create_figures(self):
        for i in range(0, 8):  # i == y pos
            for j in range(0, 8):  # j == x pos
                if self.game.collation[i][j] != 'n':
                    self.game.list_of_figures.append(self.type_of_the_figure(self.game.collation[i][j], j, i, self.game))
                    # print("x, y", self.game.list_of_figures[len(self.game.list_of_figures)-1].x, self.game.list_of_figures[len(self.game.list_of_figures)-1].y, "type of figure: ", self.game.list_of_figures[len(self.game.list_of_figures)-1].type_of_figure)
