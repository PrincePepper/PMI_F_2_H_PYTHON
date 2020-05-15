a = [0]
for i in range(10, 100):
    a.append(i)
print(sum(map(lambda i: i ** 2, filter(lambda i: i % 9 == 0, a))))
