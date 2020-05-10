n, m, k = [int(i) for i in input().split()]
table = [[0 for i in range(m + 2)] for j in range(n + 2)]

for i in range(k):
    x, y = [int(i) for i in input().split()]
    table[x][y] = '*'
    for dx, dy in [(-1, 0), (-1, -1), (-1, 1), (0, 1)]:
        x = x + dx
        y = y + dy
        table[x][y] = 1

    # table[x - 1][y - 1] += 1 if not table[x - 1][y - 1] == '*' else ''
    # table[x + 1][y + 1] += 1 if not table[x + 1][y + 1] == '*' else ''
    # table[x - 1][y] += 1 if not table[x - 1][y] == '*' else ''
    # table[x][y - 1] += 1 if not table[x][y - 1] == '*' else ''
    # table[x][y + 1] += 1 if not table[x][y + 1] == '*' else ''
    # table[x + 1][y] += 1 if not table[x + 1][y] == '*' else ''
    # table[x + 1][y - 1] += 1 if not table[x + 1][y - 1] == '*' else ''
    # table[x - 1][y + 1] += 1 if not table[x - 1][y + 1] == '*' else ''

for i in range(1, len(table) - 1):
    for j in range(1, len(table[i]) - 1):
        print(table[i][j], end=" ")
    print()
