fin = open('input.txt')

all_files = fin.read().split()

dictionary = dict()
for word in all_files:
    dictionary[word] = dictionary.get(word, 0) + 1


sorted_dict = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))

for i in range((len(sorted_dict))):
    print(sorted_dict[i][0])
