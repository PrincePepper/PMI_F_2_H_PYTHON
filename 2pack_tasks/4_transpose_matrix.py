n, m = [int(i) for i in input().split()]
mass = [[int(i) for i in input().split()] for i in range(n)]
# a = np.array(mass, dtype=int)
# a = a.transpose()

for i in range(len(mass[0])):
    for g in range(len(mass)):
        print(mass[g][i], end=" ")
    print()
