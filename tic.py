board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

def is_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i] == player for i in pos) for pos in win_positions)

def get_empty_positions():
    return [i for i in range(9) if board[i] == ' ']

# Rule-based AI
def ai_move():
    # 1. Try to win
    for i in get_empty_positions():
        board[i] = 'O'
        if is_winner(board, 'O'):
            return
        board[i] = ' '

    # 2. Block opponent
    for i in get_empty_positions():
        board[i] = 'X'
        if is_winner(board, 'X'):
            board[i] = 'O'
            return
        board[i] = ' '

    # 3. Take center
    if board[4] == ' ':
        board[4] = 'O'
        return

    # 4. Take corners
    for i in [0,2,6,8]:
        if board[i] == ' ':
            board[i] = 'O'
            return

    # 5. Take sides
    for i in [1,3,5,7]:
        if board[i] == ' ':
            board[i] = 'O'
            return

def play():
    while True:
        print_board()

        # Player move
        move = int(input("Enter position (0-8): "))
        if board[move] != ' ':
            print("Invalid move!")
            continue
        board[move] = 'X'

        if is_winner(board, 'X'):
            print_board()
            print("You win!")
            break

        if ' ' not in board:
            print("Draw!")
            break

        # AI move
        ai_move()

        if is_winner(board, 'O'):
            print_board()
            print("AI wins!")
            break

        if ' ' not in board:
            print_board()
            print("Draw!")
            break

play()