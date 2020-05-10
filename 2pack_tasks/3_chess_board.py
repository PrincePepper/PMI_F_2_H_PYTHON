# Код подрузумевает написать основой алгоритм построения шахматной доски
# задача: https://informatics.mccme.ru/mod/statements/view3.php?id=4898&chapterid=111203#1
# m - столбцы, n - строки
# пример матрицы при n =5, m=5
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

import numpy as np

# n = 5
# m = 5
# Z = np.zeros((m, n), dtype=int)
# Z[1::2, ::2] = 1
# Z[::2, 1::2] = 1
# print(Z)

m = 5
n = 6
[[(1 if ((i + j) % 2 == 0) else 0) for i in range(m)] for j in range(n)]
