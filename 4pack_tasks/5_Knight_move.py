def trantformStr_to_int(cell):  # B1
    list_all_cell_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    for i in list_all_cell_number.keys():
        if cell[0] == i:
            return list_all_cell_number[i], int(cell[1])
    return exit("Ошибка входных данных")


def transtfomInt_to_str(cell):
    list_all_cell_number = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    for i in list_all_cell_number.keys():
        if cell[0] == i:
            return str(list_all_cell_number[i]) + str(cell[1])


def cheak_cell(cell):
    step_letter, step_num = trantformStr_to_int(cell)
    list_true = []
    all_steps = [(step_letter + 2, step_num + 1),
                 (step_letter + 2, step_num - 1),
                 (step_letter - 2, step_num + 1),
                 (step_letter - 2, step_num - 1),
                 (step_letter + 1, step_num + 2),
                 (step_letter - 1, step_num + 2),
                 (step_letter + 1, step_num - 2),
                 (step_letter - 1, step_num - 2)]

    for i in range(0, 7):
        if 1 <= all_steps[i][0] <= 8 and 1 <= all_steps[i][1] <= 8:
            list_true.append(transtfomInt_to_str(all_steps[i]))
    return sorted(list_true, key=lambda x: x[0])


print(cheak_cell("B1"))
