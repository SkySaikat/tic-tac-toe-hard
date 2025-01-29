import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return all(cell != " " for cell in board)

# Function to get available moves
def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]

# Bot logic for Level 1 (Random moves)
def bot_level_1(board):
    return random.choice(get_available_moves(board))

# Bot logic for Level 2 (Win if possible, otherwise random)
def bot_level_2(board, bot_symbol):
    available_moves = get_available_moves(board)
    for move in available_moves:
        board_copy = board.copy()
        board_copy[move] = bot_symbol
        if check_winner(board_copy, bot_symbol):
            return move
    return random.choice(available_moves)

# Bot logic for Level 3 (Win or block, otherwise random)
def bot_level_3(board, bot_symbol, player_symbol):
    available_moves = get_available_moves(board)
    # Check if bot can win
    for move in available_moves:
        board_copy = board.copy()
        board_copy[move] = bot_symbol
        if check_winner(board_copy, bot_symbol):
            return move
    # Check if player can win and block them
    for move in available_moves:
        board_copy = board.copy()
        board_copy[move] = player_symbol
        if check_winner(board_copy, player_symbol):
            return move
    return random.choice(available_moves)

# Bot logic for Level 4 (Control center and corners, in addition to winning/blocking)
def bot_level_4(board, bot_symbol, player_symbol):
    available_moves = get_available_moves(board)
    # Check if bot can win
    for move in available_moves:
        board_copy = board.copy()
        board_copy[move] = bot_symbol
        if check_winner(board_copy, bot_symbol):
            return move
    # Check if player can win and block them
    for move in available_moves:
        board_copy = board.copy()
        board_copy[move] = player_symbol
        if check_winner(board_copy, player_symbol):
            return move
    # Prefer center and corners
    priority_moves = [4, 0, 2, 6, 8]  # Center, then corners
    for move in priority_moves:
        if move in available_moves:
            return move
    return random.choice(available_moves)

# Bot logic for Level 5 (Minimax algorithm - unbeatable)
def bot_level_5(board, bot_symbol):
    def minimax(board, depth, is_maximizing):
        if check_winner(board, bot_symbol):
            return 1
        if check_winner(board, "X" if bot_symbol == "O" else "O"):
            return -1
        if check_tie(board):
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for move in get_available_moves(board):
                board_copy = board.copy()
                board_copy[move] = bot_symbol
                score = minimax(board_copy, depth + 1, False)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in get_available_moves(board):
                board_copy = board.copy()
                board_copy[move] = "X" if bot_symbol == "O" else "O"
                score = minimax(board_copy, depth + 1, True)
                best_score = min(score, best_score)
            return best_score

    best_move = -1
    best_score = -float("inf")
    for move in get_available_moves(board):
        board_copy = board.copy()
        board_copy[move] = bot_symbol
        score = minimax(board_copy, 0, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game function
def tic_tac_toe():
    # Initialize the board
    board = [" " for _ in range(9)]
    player_symbol = "X"
    bot_symbol = "O"
    difficulty = int(input("Select bot difficulty level (1-5, 5 being the hardest): "))

    print("Welcome to Tic-Tac-Toe!")
    print("Player: X | Bot: O")
    print("Enter positions (1-9) as shown below:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    while True:
        # Player's turn
        print_board(board)
        try:
            position = int(input("Player X, enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid position! Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        if board[position] != " ":
            print("This position is already taken! Try again.")
            continue

        board[position] = player_symbol

        # Check if player wins
        if check_winner(board, player_symbol):
            print_board(board)
            print("Player X wins! Congratulations!")
            break

        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Bot's turn
        print("Bot's turn...")
        if difficulty == 1:
            bot_move = bot_level_1(board)
        elif difficulty == 2:
            bot_move = bot_level_2(board, bot_symbol)
        elif difficulty == 3:
            bot_move = bot_level_3(board, bot_symbol, player_symbol)
        elif difficulty == 4:
            bot_move = bot_level_4(board, bot_symbol, player_symbol)
        elif difficulty == 5:
            bot_move = bot_level_5(board, bot_symbol)

        board[bot_move] = bot_symbol

        # Check if bot wins
        if check_winner(board, bot_symbol):
            print_board(board)
            print("Bot O wins! Better luck next time.")
            break

        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
