n = int(input())

fruits = {}
for i in range(n):
    word, *explanation = input().replace(',', '').split()
    del explanation[0]
    for j in explanation:
        if j not in fruits:
            fruits[j] = []
        fruits[j].append(word)

print(len(fruits))

sorted_string = sorted(fruits.items())
# print(*[i for i in sorted_string])
for i, j in sorted_string:
    print(i, '-', ', '.join(j))
