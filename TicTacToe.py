import math

PLAYER = 'X'
AI = 'O'
EMPTY = ' '
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, AI):
        return 1
    if check_winner(board, PLAYER):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            user_input = input("Enter your move (row and column, separated by space): ")
            try:
                row, col = map(int, user_input.split())
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid move! Row and column must be between 0 and 2. Try again.")
                    continue
                if board[row][col] != EMPTY:
                    print("Invalid move! Cell already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input format. Please enter two numbers separated by space.")

        board[row][col] = PLAYER

        print_board(board)
        if check_winner(board, PLAYER):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = AI

        print_board(board)
        if check_winner(board, AI):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

play_game()