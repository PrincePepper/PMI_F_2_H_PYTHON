# https://informatics.mccme.ru/mod/statements/view3.php?id=11145&chapterid=112227#1

# 1 пример нахождения последовательности чисел фибоначи

# fib1 = 1
# fib2 = 1
# n = int(input())
#
# print(fib1, end=' ')
# print(fib2, end=' ')
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#     print(fib2, end=' ')

# 1 пример, компактный вид

# n = int(input("Номер элемента ряда Фибоначчи: ")) - 2
# fib1 = fib2 = 1
# print(fib1, end=' ')
# print(fib2, end=' ')
# while n > 0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
#     print(fib2, end=' ')

# 2 пример нахождения последовательности чисел фибоначи
# fib1 = fib2 = 1
#
# n = int(input())
#
# if n < 2:
#     quit()
#
# print(fib1, end=' ')
# print(fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# 3 пример нахождения последовательности чисел фибоначи
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
for i in range(n):
    print(fibonacci(i + 1), end=' ')
