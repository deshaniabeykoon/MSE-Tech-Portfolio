import random


def new_board():
    """Create and return a new empty 3x3 board."""
    return [" " for _ in range(9)]

def display(board):
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

def play_game(board, player): 
    """Play until a win or a draw""" 
    current_player = player 
    while not game_over(board): 
        display(board)
        play_one_turn(board, current_player, player)
        current_player = other_player(current_player)

def other_player(current_player):
    """Given the current player ('O' or 'X') return the other player""" 
    return 'X' if current_player == 'O' else 'O'

def play_one_turn(board, current_player, human_player): 
    """Given a board state and the current player ('O' or 'X'), play one move""" 
    if current_player == human_player: 
        make_human_move(board, current_player) 
    else: 
        make_computer_move(board, current_player)

def make_human_move(board, current_player): 
    """Given a board state and the human piece ('O' or 'X') ask the player for a location to play in. Repeat until a valid response is given.""" 
    while True: 
        move = input(f"Player {current_player}, enter your move (1-9): ") 
        if move.isdigit(): 
            move = int(move) - 1 
            if 0 <= move < 9 and board[move] == ' ': 
                board[move] = current_player 
                break 
            else: 
                print("Invalid move. Try again.") 
        else: 
            print("Invalid input. Please enter a number between 1 and 9.")

def make_computer_move(board, current_player): 
    """Given a board state and the computer piece ('O' or 'X') choose a square for the computer to play in""" 
    candidates = empty_squares(board) 
    choice = random.randrange(0, len(candidates))
    row, column = candidates[choice] 
    index = row * 3 + column
    board[index] = current_player

def empty_squares(board):
    """Return a list of (row, column) tuples for empty squares on the board."""
    return [(i // 3, i % 3) for i, v in enumerate(board) if v == " "]

def won_game(board):
    """Return True if either player has won the game."""
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(
        board[pos[0]] == board[pos[1]] == board[pos[2]]
        and board[pos[0]] != " "
        for pos in win_positions
    )

def game_over(board): 
    """Given a board state return true iff there's a winner or if the game is drawn.""" 
    return won_game(board) or is_full(board)

def is_full(board):
    """Return True if the board is full (no empty spaces), otherwise False."""
    return all(square != " " for square in board)

def game_over(board): 
    """Return true iff there's a winner""" 
    return won_game(board)

def main():
    """Play a game of noughts and crosses"""
    board = new_board()
    # Ensure the computer player is the opposite of the human player
    human_player = get_O_or_X()
    computer_player = 'O' if human_player == 'X' else 'X'
    outcome =  play_game(board, human_player)
    print_result(outcome)

def print_result(outcome):
    """Print the result of the game based on the outcome."""
    if outcome == "draw":
        print("It's a draw!")
    elif outcome == "X":
        print("Player X wins!")
    elif outcome == "O":
        print("Player O wins!")
    else:
        print("Game over.")

# Run the game
if __name__ == "__main__":
    main()