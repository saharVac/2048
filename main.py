from random import choice

# generate random 2 or 4 in tile at random row and column

tile = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

new_num = choice([2, 4])
new_row = choice([0, 1, 2, 3])
new_col = choice([0, 1, 2, 3])
tile[new_row][new_col] = new_num

print("|         |         |         |         |")
print("|    " + str(tile[0][0]) + "    |    " + str(tile[0][1]) + "    |    " + str(tile[0][2]) + "    |    " + str(tile[0][3]) + "    |")
print("|         |         |         |         |")
print("-----------------------------------------")
print("|         |         |         |         |")
print("|    " + str(tile[1][0]) + "    |    " + str(tile[1][1]) + "    |    " + str(tile[1][2]) + "    |    " + str(tile[1][3]) + "    |")
print("|         |         |         |         |")
print("-----------------------------------------")
print("|         |         |         |         |")
print("|    " + str(tile[2][0]) + "    |    " + str(tile[2][1]) + "    |    " + str(tile[2][2]) + "    |    " + str(tile[2][3]) + "    |")
print("|         |         |         |         |")
print("-----------------------------------------")
print("|         |         |         |         |")
print("|    " + str(tile[3][0]) + "    |    " + str(tile[3][1]) + "    |    " + str(tile[3][2]) + "    |    " + str(tile[3][3]) + "    |")
print("|         |         |         |         |")
