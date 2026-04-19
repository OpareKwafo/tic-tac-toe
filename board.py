from player import Player
# Board class
# Attributes:
# has a structure - 9 position structure

class Board:
    """A simple way to describe the tic-tac-toe board"""
    def __init__(self):
        
        self.board = {
            "1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " "
        }
        
# Actions:
# Show board
    def show_board(self):
        """Displays the game board"""
        
        print(self.board["1"] + " | " + self.board["2"] + " | " + self.board["3"])
        print("-+-+-+-+-")
        print(self.board["4"] + " | " + self.board["5"] + " | " + self.board["6"])
        print("-+-+-+-+-")
        print(self.board["7"] + " | " + self.board["8"] + " | " + self.board["9"])

    def get_position(self, pos):
        """Return's the entry in the position you specify on the board"""
        return self.board[pos]
    

    def set_position(self, pos, move):
        """Updates the board with the player position"""
        self.board[pos] = move



   
        
