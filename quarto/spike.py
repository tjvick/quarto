import numpy as np
import random


class ComputerPlayer:
    def __init__(self, game):
        self.game = game

    def take_turn(self):
        turn = self.choose_turn()
        game.apply_turn(turn)

    def choose_turn(self):
        available_positions = self.game.available_positions
        random_position = random.choice(available_positions)

        available_pieces = self.game.available_pieces
        random_piece = random.choice(available_pieces)
        return QuartoTurn(random_position, random_piece)


class QuartoGame:
    def __init__(self):
        self.board = QuartoBoard()
        self.active_player = False
        self.chosen_piece = QuartoPiece(0)

    def apply_turn(self, turn):
        self.board.place(self.chosen_piece, turn.position)
        self.chosen_piece = turn.piece
        self.active_player = not self.active_player

    @property
    def available_pieces(self):
        placed_pieces = set(self.board.placed_pieces)
        all_pieces = set(QUARTO_PIECES)
        return all_pieces.difference(placed_pieces).difference({self.chosen_piece})

    @property
    def available_postiions(self):
        # wip
        positions = set()


class QuartoBoard:
    def __init__(self):
        self.placements = np.empty(16, dtype=object)

    def place(self, piece, position):
        self.placements[position.index] = piece

    @property
    def placed_pieces(self):
        # wrong
        return self.placements.flatten()

    @property
    def occupied_positions(self):
        # wip
        return


class QuartoTurn:
    def __init__(self, position, piece):
        self.position = position
        self.piece = piece


class QuartoPiece:
    def __init__(self, id_):
        self.id = id_
        self.characteristics = [0, 0, 0, 0]


class QuartoBoardPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @property
    def index(self):
        return self.row*4 + self.col


QUARTO_PIECES = (QuartoPiece(ix) for ix in range(16))

game = QuartoGame()
player1 = ComputerPlayer(game)
player2 = ComputerPlayer(game)
# while not game.is_over:
player1.take_turn()
player2.take_turn()



