# https://informatics.mccme.ru/mod/statements/view3.php?id=11250&chapterid=112351#1
# Напишите программу, которая переводит число (возможно, отрицательное),
# записанное в шестнадцатеричной системе, в десятичную систему.

# def convert_base(num, to_base=10, from_base=10):
#     # first convert to decimal number
#     if isinstance(num, str):
#         n = int(num, from_base)
#     else:
#         n = int(num)
#     # now convert decimal to 'to_base' base
#     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if n < to_base:
#         return alphabet[n]
#     else:
#         return convert_base(n // to_base, to_base) + alphabet[n % to_base]
#
#
# print(convert_base(10))

print(int(input(), 16))
