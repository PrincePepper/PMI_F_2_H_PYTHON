def middle_of_3(a, b, c):
    if a <= b & a <= c:
        middle = b if b <= c else c
    else:
        if b <= a & b <= c:
            middle = a if a <= c else c
        else:
            middle = a if a <= b else b


fin = open("input.txt", "r")
fout = open("output.txt", "w")
val_filter = 0
while fin:

