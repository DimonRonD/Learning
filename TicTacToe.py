"""
Игра "Крестики-нолики в терминале
"""

def draw_board(board):
    for i in range(3):
        print("|".join(board[i]))
        print("------")


def initialize_player():
    player = input("Enter figure: ")
    return player

def new_move(board, player, x, y):
    if board[x][y] == " ":
        board[x][y] = player
        return True
    else:
        return False

def ask_move(board, player):
    x, y = input("Enter x, y over space: ").split()
    x, y = int(x) - 1, int(y) - 1
    if (0 <= x < 3) and (0 <= y < 3) and board[x][y] == " ":
        return x, y
    else:
        print("Клетка занята, введите другие координаты")
        return ask_move(board, player)

def make_move(board, player):
    x, y = ask_move(board, player)
    new_move(board, player, x, y)
    draw_board(board)
    game_over = check_game_over(board, player)
    print(game_over)
    if game_over:
        print("Inside IF", game_over)
        congr(player)


def check_game_over(board, player):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
    return False

def congr(player):
    print(f"Игрок {player} победил!")
    tmp = input("Хотите сыграть ещё раз? (yes/no) ")
    if tmp == "yes":
        main()
    else:
        exit(0)


# Инициируем переменные
def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game_over = False
    player = initialize_player()
    while True:
        make_move(board, player)

main()









