import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(self.letter)

    def get_move(self, game):
        square = random.choice(game.availableMoves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        validSquare = False
        val = None
        While not validSquare:
            square = input(self.letter + '\`s turn. Input move (0-9):')
