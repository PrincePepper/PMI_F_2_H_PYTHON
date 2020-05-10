# https://informatics.mccme.ru/mod/statements/view3.php?id=11145&chapterid=112212#1
# Напишите программу, которая считает количество чётных цифр введённого числа.
print(len([i for i in input() if int(i) %2 == 0]))

