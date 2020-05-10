fout = open('output.txt', 'w')

N = int(input())

file_name = {}
for i in range(N):
    name, *value = input().split()
    file_name[name] = value

N = int(input())

for i in range(N):
    arg_list, new_name = input().split()
    values = file_name.get(new_name)
    if arg_list == 'write':
        arg_list = 'W'
    elif arg_list == 'read':
        arg_list = 'R'
    elif arg_list == 'execute':
        arg_list = 'X'
    if arg_list in values:
        fout.write('OK' + '\n')
    else:
        fout.write('Access denied' + '\n')
