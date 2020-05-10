# https://informatics.msk.ru/mod/statements/view3.php?id=208&chapterid=1460#1
# нужно сдвинуть последовательность на заданное число

n = int(input())
s = list(input().split())
step = int(input()) % len(s)
print(*(s[-step:] + s[:-step]))
exit()
