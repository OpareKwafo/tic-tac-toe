import random

# Initializing the board as a dictionary.
board = {
    "1": " ", "2": " ", "3": " ",
    "4": " ", "5": " ", "6": " ",
    "7": " ", "8": " ", "9": " "
}

# The winning combination
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

# Assigning symbols
player_move = "X"
computer_move = "O"

def show_board():

    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("-+-+-+-+-")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("-+-+-+-+-")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])

count = 1
game_over = False



while count < 10 and not game_over:

    # Getting player move
    player_position = input("where do you want to put it - Enter 1 - 9: ")
    print(f"The player position is {player_position}")
    computer_position = str(random.randint(1, 9))
    print(f"Computer position is {computer_position}")

    # Keep asking for input if the selected position if already filled
    while board[player_position] != " ":
        player_position = input("where do you want to put it - Enter 1 - 9: ")
        print(f"The player position is {player_position}")
    board[player_position] = player_move

    while board[computer_position] != " ":
        computer_position = str(random.randint(1, 9))
        print(f"Computer position is {computer_position}")
    board[computer_position] = computer_move

    
    show_board()
    print("-" * 20)

    # Only check for winner after 3 rounds
    if count >= 3:
        for combo in winning_combination:
            # Unpack each tuple
            a, b, c = combo

            # Check if you have the same symbol in a row
            if (board[a] == board[b] == board[c]) and board[a] != " ":
                game_over = True
                if board[a] == player_move:
                    print("player_one won")
                    break
                elif board[a] == computer_move:
                    print("computer won")
                    break
                else:
                    print("Appears to be a draw")
                    break

    print(f"This is the board after round {count}")
    show_board()
    # Update the count
    count += 1
            






