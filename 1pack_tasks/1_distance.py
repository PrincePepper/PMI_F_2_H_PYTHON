# задача: https://informatics.mccme.ru/mod/statements/view3.php?id=11098&chapterid=112149#1
# Напишите программу, которая вводит координаты двух точек на числовой оси
# и выводит расстояние между ними.
# ВхД:
# 1. 1.
# 2. 2.
# ВыД:
# 1.414
x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(i) for i in input().split()]
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'{a:.3f}')
