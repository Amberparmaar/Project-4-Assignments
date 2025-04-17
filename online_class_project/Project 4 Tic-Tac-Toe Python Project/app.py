# Tic Tac Toe Game
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Board print function
def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

#win position
def check_winner(player):
    wins = [[0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True
    return False

# Game start
def play_game():
    turn = "X"
    moves = 0
    show_board()

    while True:
        choice = input(f"Player {turn}, choose a number (1-9): ")

        if choice not in board:
            print("❌ Wrong move, try again.")
            continue

        index = board.index(choice)
        board[index] = turn
        show_board()
        moves += 1

        if check_winner(turn):
            print(f"🎉 Player {turn} wins!")
            break

        if moves == 9:
            print("😐 It's a draw!")
            break

        turn = "O" if turn == "X" else "X"

play_game()
