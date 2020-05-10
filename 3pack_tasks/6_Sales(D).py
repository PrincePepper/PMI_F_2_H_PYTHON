fin = open('input.txt', 'r')
goods = {}
dictionary = {}

for i in fin:
    buyer, product, amount = i.split()
    if buyer in dictionary:
        dictionary[buyer].append((product, amount))
    else:
        dictionary[buyer] = [(product, amount)]

for i in sorted(dictionary):
    print(i + ':')
    aa = sorted(dictionary[i])
    g = 0
    for j in aa:
        if g != len(aa) - 1 and aa[g][0] == aa[g + 1][0]:
            j = (j[0], str(int(j[1]) + int(aa[g + 1][1])))
            del aa[g + 1]
        print(j[0] + " " + j[1])
        g += 1