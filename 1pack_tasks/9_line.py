# https://informatics.msk.ru/mod/statements/view3.php?id=208&chapterid=1456#1


# N = int(input())
# s = list([int(i) for i in input().split()])
# value = int(input())  # искомое число
#
#
# def binpoisk(s, value):
#     left = s[0:len(s) // 2]
#     right = s[len(s) // 2:len(s)]
#     if left[len(left) - 1] < value > right[0]:
#         print(left, right)
#         return binpoisk(left, value)
#     elif left[len(left) - 1] > value > right[0]:
#         print(left, right)
#         return binpoisk(right, value)
#
#
# binpoisk(s, value)


n = int(input())
line = [int(i) for i in input().split()]
petya = int(input())
line = [int(i) for i in range(n) if petya <= line[i]]
print(len(line) + 1)

# N = int(input())
# class_height = list([int(i) for i in input().split()])
# value = int(input())  # искомое число
# class_height.insert(0, value)
# class_height.sort()
# idx = class_height.index(value)
# print(len(class_height) - idx)
