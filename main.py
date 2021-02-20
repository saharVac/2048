from random import choice

# don't show tiles with value 0

tiles = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

new_num = choice([2, 4])
new_row = choice([0, 1, 2, 3])
new_col = choice([0, 1, 2, 3])
tiles[new_row][new_col] = new_num

for row in tiles:
    for line in range(5):
        if line == 2:
            print("|     " + (str(row[0]) if row[0] else " ") + "     |     " + (
                str(row[1]) if row[1] else " ") + "     |     " + (str(
                row[2]) if row[2] else " ") + "     |     " + (str(row[3]) if row[3] else " ") + "     |")
        else:
            print("|           |           |           |           |")
    print("-------------------------------------------------")