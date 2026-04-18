import pprint
import random

# Initializing the board as a dictionary.
board = {
    "1": " ", "2": " ", "3": " ",
    "4": " ", "5": " ", "6": " ",
    "7": " ", "8": " ", "9": " "
}

# Assigning symbols
player_move = "X"
computer_move = "O"

def show_board():

    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("-+-+-+-+-")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("-+-+-+-+-")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])

# pprint.pprint(board)

count = 0 

winner = False

while not winner:

    # Getting player move
    player_position = input("where do you want to put it - Enter 1 - 9: ")

    # Only update board if the position is empty
    if board[player_position] == " ":

        # Updating player move on the board
        if player_position == '1':
            board["1"] = player_move
        elif player_position == '2':
            board["2"] = player_move
        elif player_position == '3':
            board["3"] = player_move
        elif player_position == '4':
            board["4"] = player_move
        elif player_position == '5':
            board["5"] = player_move
        elif player_position == '6':
            board["6"] = player_move
        elif player_position == '7':
            board["7"] = player_move
        elif player_position == '8':
            board["8"] = player_move
        else:
            board["9"] = player_move
    else:
        print("Select a different position")
        player_position = input("where do you want to put it - Enter 1 - 9: ")

    #show board after player move
    show_board()

    print("*" * 20)

    # Getting Computer move
    computer_position = str(random.randint(1, 9))
    print(f"Computer position is {computer_position}")

    # Only update if the space is empty
    if board[computer_position] == " ":

        # Updating player position on the board
        if computer_position == '1':
            board["1"] = computer_move
        elif computer_position == '2':
            board["2"] = computer_move
        elif computer_position == '3':
            board["3"] = computer_move
        elif computer_position == '4':
            board["4"] = computer_move
        elif computer_position == '5':
            board["5"] = computer_move
        elif computer_position == '6':
            board["6"] = computer_move
        elif computer_position == '7':
            board["7"] = computer_move
        elif computer_position == '8':
            board["8"] = computer_move
        else:
            board["9"] = computer_move
    else:
        computer_position = str(random.randint(1, 9))
        print(f"Computer position is {computer_position}")


    show_board()

    print("*" * 20)

    # checking win
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
    
    
    # Only check for winner after 3 rounds
    
    if count >= 3:

        for combo in winning_combination:
            # Unpack each tuple
            a, b, c = combo

            # Check if you have the same symbol in a row
            if (board[a] == board[b] == board[c]) and board[a] != " ":

                if board[a] == player_move:
                    print("player_one won")
                elif board[a] == computer_move:
                    print("computer won")

    show_board()

    count += 1
            






