def sorted2(data, key):
    sort_data = []
    for i in data:
        sort_data.append(sorted(i))
    return sorted(sort_data, key=key)


data = [[6, 5, 4], [3, 2], [1]]
key = lambda x: x
print(sorted2(data, key=key))
