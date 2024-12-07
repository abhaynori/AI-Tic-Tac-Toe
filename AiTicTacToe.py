import math

# Constants
AI_PLAYER = 'O'
HUMAN_PLAYER = 'X'

def print_board(board):
    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell is not None for row in board for cell in row)

def evaluate(board):
    if is_winner(board, AI_PLAYER):
        return 10
    elif is_winner(board, HUMAN_PLAYER):
        return -10
    return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    
    if score == 10 or score == -10:
        return score
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = AI_PLAYER
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = None
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = HUMAN_PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = None
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = AI_PLAYER
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = None
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main Game Loop
def tic_tac_toe():
    board = [[None, None, None] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("You are X. AI is O.")
    print_board(board)

    while True:
        # Player Move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] is None:
            board[row][col] = HUMAN_PLAYER
        else:
            print("Invalid move. Try again.")
            continue

        if is_winner(board, HUMAN_PLAYER):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI Move
        print("AI is making a move...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = AI_PLAYER
        print_board(board)

        if is_winner(board, AI_PLAYER):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
tic_tac_toe()

