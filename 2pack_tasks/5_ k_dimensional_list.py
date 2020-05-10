# def rec(n , line):
#     if n > 0:
#         return rec(n - 2, [line] * 2)
#     return line

k = int(input())
a = list([0, 0])
for i in range(1, k):
    b = list([a, a])
    a = b
print(a)
