from player import Player
from board import Board

def check_winner(game_board, human_player_move, computer_player_move):
    """This function checks if a player won"""

    winner = None
    winning_combination = [
        ("1", "2", "3"), 
        ("4", "5", "6"),
        ("7", "8", "9"),
        ("1", "4", "7"),
        ("2", "5", "8"),
        ("3", "6", "9"),
        ("1", "5", "9"),
        ("3", "5", "7")
    ]

    for combo in winning_combination:
        # Unpack each tuple
        a, b, c = combo

        # Check if you have the same symbol in a row
        if (game_board.get_position(a) == game_board.get_position(b) == game_board.get_position(c)) and game_board.get_position(a) != " ":
            # game_over = True
            if game_board.get_position(a) == human_player_move:
                print("CONGRATULATIONS!! YOU WON")
                return "player"
            elif game_board.get_position(a) == computer_player_move:
                print("YOU LOST HAHAHA!! THE COMPUTER WON - TRY AGAIN")
                return "computer"
            else:
                print("THIS IS A DRAW")
    return None
    