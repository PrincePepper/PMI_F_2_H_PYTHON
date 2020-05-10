fout = open('output.txt', 'w')

n = int(input())

cities = {}
for i in range(n):
    country, *city = input().split()
    for i in range((len(city))):
        cities[city[i]] = country

m = int(input())
print()
for i in range(m):
    fout.write(cities[input()] + '\n')
