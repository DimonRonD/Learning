"""
Игра "Крестики-нолики в терминале
"""
from colorama import Fore, Back, Style

def draw_board(board, player):
    for i in range(3):
        print(Fore.BLUE, "-------------")
        print(Fore.BLUE, "|", end="")
        for j in range(3):
            if board[i][j] == " ":
                print(Fore.BLUE, board[i][j], end="")
            elif board[j][i] == player:
                print(Fore.RED, board[i][j], end="")
            print(Fore.BLUE, "|", end="")
        print("")
    print(Fore.BLUE, "-------------", end="")
    print(Fore.WHITE, "")


def initialize_player():
    player = input("Введите ваш символ: ")
    return player

def new_move(board, player, x, y):
    if board[x][y] == " ":
        board[x][y] = player
        return True
    else:
        return False

def ask_move(board, player):
    print(Fore.LIGHTWHITE_EX, "Введите x, y через проблем в диапазоне (1..3): ", end="")
    x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    if (0 <= x < 3) and (0 <= y < 3) and board[x][y] == " ":
        return x, y
    else:
        print(Fore.RED, "Клетка занята, введите другие координаты")
        return ask_move(board, player)

def make_move(board, player):
    x, y = ask_move(board, player)
    new_move(board, player, x, y)
    draw_board(board, player)
    game_over = check_game_over(board, player)
    if game_over:
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
    print(Fore.WHITE, f"Игрок {player} победил!")
    tmp = input("Хотите сыграть ещё раз? (yes/no) ")
    if tmp == "yes":
        main()
    else:
        exit(0)

# def enemy_turn(board, player, enemy):
#     enemy_move = False
#     player_flag_x = 0
#     player_flag_y = 0
#
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == player:
#                 player_flag_x += 1
#             if board[j][i] == player:
#                 player_flag_y += 1
#
#     if player_flag_x == 2:





        # Инициируем переменные
def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game_over = False
    player = initialize_player()
    while True:
        make_move(board, player)

main()









