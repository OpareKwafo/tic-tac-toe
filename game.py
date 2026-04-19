import random

from player import Player
from board import Board
from check_winner import check_winner

# Create a player
human_player = Player("Human", "X")

# Create Computer player
computer_player = Player("computer", "O", True)

# Show board
game_board = Board()
game_board.show_board()

count = 1

game_over = False

while count < 10 and not game_over: 

    # Get player selection
    player_selection = human_player.select_position()

    # Update board with player selection; Check if that position is empty first
    while game_board.get_position(player_selection) != " ":
        player_selection = human_player.select_position()
    game_board.set_position(player_selection, human_player.move) 
    print(f"This is the game board after your turn")
    game_board.show_board()

    # Get computer selection
    computer_selection = computer_player.select_position()

    # Update board with computer selection; Check if that position is empty first
    while game_board.get_position(computer_selection) != " ":
        computer_selection = computer_player.select_position()
    game_board.set_position(computer_selection, computer_player.move) 
    print(f"This is the game board after the computer's turn")
    game_board.show_board()

    print(f"This is the game board after round {count}")
    game_board.show_board()
    count += 1


    # Check winner - We only want to start checking after round 3
    if count >= 3:
        winner = check_winner(game_board, human_player.move, computer_player.move)
    # End game if there is a winner
        if winner:
            game_over = True

    



























