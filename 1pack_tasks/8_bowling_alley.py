# https://informatics.mccme.ru/mod/statements/view3.php?id=4163&chapterid=3851#1

a, n = [int(i) for i in input().split()]
a = ['I'] * a
for i in range(n):
    d, c = [int(i) for i in input().split()]
    f = c - d
    a[d - 1:c] = ['.'] * (f + 1)
print(*a, sep="")
