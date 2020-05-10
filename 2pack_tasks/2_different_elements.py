# https://informatics.mccme.ru/mod/statements/view3.php?id=4163&chapterid=3838#1
# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.

print(len(set([int(i) for i in input().split()])))
