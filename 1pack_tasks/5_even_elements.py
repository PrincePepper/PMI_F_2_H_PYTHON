# https://informatics.mccme.ru/mod/statements/view3.php?id=4163&chapterid=3829#1
# Выведите все четные элементы списка.

# n = list(input().split(' '))
# for i in range(len(n)):
#     if int(n[i]) % 2 == 0:
#         print(n[i], end=' ')


print(*[x for x in input().split() if not int(x) % 2])
