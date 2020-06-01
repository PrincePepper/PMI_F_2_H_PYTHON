def sorted2(data, key):
    sort_data = []
    for i in data:
        sort_data.append(sorted(i, key=key))
    return sorted(sort_data, key=lambda x: x[-1])


data = [[6, 5, 4], [1], [3, 2]]
key = lambda x: -x
print(sorted2(data, key=key))
