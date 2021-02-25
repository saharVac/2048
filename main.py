from random import choice

# move the tiles
from pip._vendor.distlib.compat import raw_input

tiles = [
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0]
]


def add_tile():
    new_num = choice([2, 4])
    while True:
        new_row = choice([0, 1, 2, 3])
        new_col = choice([0, 1, 2, 3])
        if tiles[new_row][new_col] == 0:
            tiles[new_row][new_col] = new_num
            break


def print_board():
    for row in tiles:
        print(row)


def move(direction):
    if direction == "up":
        for col in range(4):
            print("col", col, [tiles[0][col], tiles[1][col], tiles[2][col], tiles[3][col]])
            # if first in column equals second in column
            if tiles[0][col] == tiles[1][col]:
                tiles[0][col] = tiles[0][col] * 2
                tiles[3][col] = 0
                print("third in column equals fourth in column", tiles[2][col] == tiles[3][col], " third", tiles[2][col], " fourth", tiles[3][col])
                # if third in column equals fourth in column
                if tiles[2][col] == tiles[3][col]:
                    print("EQUALS", tiles[2][col])
                    tiles[1][col] = tiles[2][col] * 2
                    tiles[2][col] = 0
                else:
                    tiles[1][col] = tiles[2][col]
                    tiles[2][col] = tiles[3][col]


def game():
    while True:
        print_board()
        next_move = input("Next Move:")
        move(next_move)


game()
