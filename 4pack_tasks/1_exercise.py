N = int(input())
for i in range(N):
    K = int(input())
    dictionary = dict()
    for j in range(K):
        people, num = input().split()
        dictionary[people] = int(num)

    if not all(key > 0 for key in dictionary.values()):
        exit("\nНЕТ")
exit("\nДА")
