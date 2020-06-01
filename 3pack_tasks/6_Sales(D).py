fin = open('input.txt', 'r')

dictionary = {}

for i in fin:
    buyer, product, amount = i.split()
    if buyer in dictionary:
        if product in dictionary[buyer]:
            dictionary[buyer][product] = int(dictionary[buyer][product]) + int(amount)
        else:
            dictionary[buyer][product] = amount
    else:
        dictionary[buyer] = {}
        dictionary[buyer][product] = amount

for i in sorted(dictionary):
    print(i + ':')
    for j in sorted(dictionary[i]):
        print(j + " " + str(dictionary[i][j]))
