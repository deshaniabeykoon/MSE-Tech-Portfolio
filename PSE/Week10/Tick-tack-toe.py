import random

def new_board():
    return [' '] * 9

def display_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")
    print("\n")

def get_O_or_X():
    choice = ''
    while choice not in ['O', 'X']:
        choice = input("Do you want to be 'O' or 'X'? ").upper()
    return choice

def switch_player(current, human, computer):
    return computer if current == human else human

def game_over(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or ' ' not in board

def get_human_move(board):
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

def get_computer_move(board):
    available = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(available)

def make_move(board, move, player):
    board[move] = player

def check_winner(board, player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_positions)

def get_outcome(board, human, computer):
    if check_winner(board, human):
        return "You win!"
    elif check_winner(board, computer):
        return "Computer wins!"
    else:
        return "It's a draw!"

def print_result(outcome):
    print(outcome)

def main():
    """Play a game of noughts and crosses"""
    board = new_board()
    # Ensure the computer player is the opposite of the human player
    human_player = get_O_or_X()
    if human_player == 'X':
        computer_player = 'O'
    else:
        computer_player = 'X'
    current_player = human_player

    while not game_over(board):
        display_board(board)
        if current_player == human_player:
            move = get_human_move(board)
        else:
            move = get_computer_move(board)
        make_move(board, move, current_player)
        current_player = switch_player(current_player, human_player, computer_player)

    display_board(board)
    outcome = get_outcome(board, human_player, computer_player)
    print_result(outcome)

# Run the game
if __name__ == "__main__":
    main()
