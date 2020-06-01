def gematria(letter):
    return sum([ord(letter) - ord('A') for letter in letter.upper()])


fin = open('../3pack_tasks/input.txt')
line = fin.read().splitlines()

print(*sorted(line, key=lambda i: (gematria(i), i)), sep='\n')
