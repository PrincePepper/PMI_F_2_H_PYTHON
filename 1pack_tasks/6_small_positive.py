# https://informatics.mccme.ru/mod/statements/view3.php?id=4163&chapterid=3835#1
# Выведите значение наименьшего из всех положительных элементов в списке.

print(min(int(i) for i in input().split() if int(i) > 0))
