import random
# player class
# Attributes:

# player has a name
# player has a move or symbole

class Player:
    """A simple way to simulate a game player"""

    def __init__(self, name, move, is_computer=False):
        self.name = name
        self.move = move
        self.is_computer = is_computer


# Actions:
# player has to select a position on the board

    def select_position(self):

        if self.is_computer == True:
            return str(random.randint(1, 9))
        else:
            return input("where do you want to put it - Enter 1 - 9: ")





         

        





