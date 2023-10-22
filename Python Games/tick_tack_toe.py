def print_table(game_table):
    table = []
    for row in game_table:
        table.append(" " + " | ".join(row))
    print(" \n---|---|---\n".join(table))

game_table = [[" ", " ", " "] for _ in range(3)]


print_table(game_table)
for i in range(9):
    num = int(input("Enter cell number: "))
    a, b = divmod(num - 1, 3)
    game_table[a][b] = "O" if (i % 2 == 0) else "X"
    print_table(game_table)
