from random import choice

# move the tiles
from pip._vendor.distlib.compat import raw_input

tiles = [
    [4, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
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
            # tiles[0][col] = tiles[0][col] == tiles[1][col] ? tiles[0][col] * 2 :
            # if first in column isn't 0 [nonzero, ..., ..., ...]
            if tiles[0][col] != 0:
                # if first in column equals second in column [equals, equals, ..., ...]
                if tiles[0][col] == tiles[1][col]:
                    tiles[0][col] = tiles[0][col] * 2
                    # if third in column equals fourth in column [equals1, equals1, equals2, equals2]
                    if tiles[2][col] == tiles[3][col]:
                        tiles[1][col] = tiles[2][col] * 2
                        tiles[2][col] = 0
                    # if third in column doesn't equal fourth in column [equals1, equals1, nonequal, nonequal]
                    else:
                        # if third in column is nonzero 0 [equals1, equals1, nonzero , nonequal]
                        if tiles[2][col] != 0:
                            tiles[1][col] = tiles[2][col]
                            tiles[2][col] = tiles[3][col]
                        # if third in column is  0 [equals1, equals1, 0 , nonzero]
                        else:
                            tiles[1][col] = tiles[3][col]
                            tiles[2][col] = 0
                    tiles[3][col] = 0
                # if first in column doesn't equal second in column
                else:
                    # if second in column isn't 0 [nonzero nonequal, nonzero nonequal, ..., ...]
                    if tiles[1][col] != 0:
                        if tiles[1][col] == tiles[2][col]:
                            tiles[1][col] = tiles[2][col] * 2
                            tiles[2][col] = tiles[3][col]
                            tiles[3][col] = 0
                        else:
                            tiles[1][col] = tiles[2][col]
                            tiles[2][col] = tiles[3][col]
                    # if second in column is 0 [nonzero, 0, ..., ...]
                    else:
                        # if third in column is 0 [nonzero, 0, 0, ...]
                        if tiles[1][col] == tiles[2][col]:

            # if first in column is 0 [0, ..., ..., ...]
            else:
                # if first in column equals second in column [0, 0, ..., ...]
                if tiles[0][col] == tiles[1][col]:
                    # if second in column equals third in column [0, 0, 0, ...]
                    if tiles[1][col] == tiles[2][col]:
                        tiles[0][col] = tiles[3][col]
                    # if second in column doesn't equal third in column [0, 0, nonzero, ...]
                    else:
                        tiles[0][col] = tiles[2][col]
                        tiles[1][col] = tiles[3][col]
                    tiles[2][col] = 0
                    tiles[3][col] = 0
                # if first in column doesn't equal second in column [0, nonzero, ..., ...]
                else:
                    # if second in column equals third in column [0, equal, equal, ...]
                    if tiles[1][col] == tiles[2][col]:
                        tiles[0][col] = tiles[1][col] * 2
                        tiles[1][col] = tiles[3][col]
                    # if second in column doesn't equal third in column [0, nonequal, nonequal, ...]
                    else:
                        tiles[0][col] = tiles[1][col]
                        # if third in column equals fourth in column [0, ..., equal, equal]
                        if tiles[2][col] == tiles[3][col]:
                            tiles[1][col] = tiles[2][col] * 2
                            tiles[2][col] = 0
                        # if third in column doesn't equal fourth in column [0, ..., nonequal, nonequal]
                        else:
                            tiles[1][col] = tiles[2][col]
                            tiles[2][col] = tiles[3][col]
                    tiles[3][col] = 0


def game():
    while True:
        add_tile()
        print_board()
        next_move = input("Next Move: ")
        move(next_move)


game()
