def my_map(func, iterator):
    return [func(i) for i in iterator]


values = [int(i) for i in input().split()]
operation = lambda x: x + 5

exit(my_map(operation, values))

