WHITE = 1
BLACK = 2


def print_board(board):  # Распечатать доску в текстовом виде
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row + 1, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(chr(col + 65), end='    ')
    print()


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def parse_coords(coords):
    """функция должна принимать список координат в шахматном виде и возвращает row, col, row1, col1"""
    coords_in_digits = []
    for col, row in coords.upper().split():
        coords_in_digits.extend([int(row) - 1, ord(col) - ord('A')])
    return coords_in_digits


class Board:
    """Класс доски"""

    def __init__(self):
        self.color = WHITE
        self.field = [[None] * 8 for row in range(8)]
        ''' Задаем начальное расположение фигур на доске: '''
        # Верх
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]

        # Вниз
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]
        self.white_king = (0, 4)
        self.black_king = (7, 4)
        self.white_pieces = self.field[0] + self.field[1]
        self.black_pieces = self.field[7] + self.field[6]

    def get_king(self):
        return self.white_king if self.color == WHITE else self.black_king

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]

    def move_piece(self, row, col, row1, col1):
        """ Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False """

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False

        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        else:
            """Если мы перемещаемся на фигуру"""
            if self.field[row1][col1].get_color() == self.color:
                return False
            if not piece.can_attack(self, row, col, row1, col1):
                return False

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)  # поменять цвет
        return True

    def __swap(self, row, col, row1, col1):
        piece = self.field[row][col]
        enemy = self.field[row1][col1]
        # удаляем enemy
        if not enemy is None:
            if self.color == BLACK:
                self.white_pieces.remove(enemy)
            else:
                self.black_pieces.remove(enemy)
        # ходим
        self.field[row][col] = None
        self.field[row1][col1] = piece
        # координаты короля
        if type(piece) is King:
            if self.color == WHITE:
                self.white_king = (row1, col1)
            else:
                self.black_king = (row1, col1)
        # проверяем, что после хода
        # король не попадает под шах
        if self.is_under_attack(*self.get_king(), opponent(self.color)):
            self.field[row][col] = piece
            self.field[row1][col1] = enemy
            if type(piece) is King:
                if self.color == WHITE:
                    self.white_king = (row, col)
                else:
                    self.black_king = (row, col)
            if not enemy is None:
                if self.color == BLACK:
                    self.white_pieces.append(enemy)
                else:
                    self.black_pieces.append(enemy)
            return False

        # изменяем координаты фигуры
        piece.row = row1
        piece.col = col1

        # меняем флаг not_moved у короля или ладьи
        if type(piece) in [King, Rook]:
            piece.not_moved = False

        # меняем цвет ходящего игрока
        self.color = opponent(self.color)
        return True

    def clean_row(self, row, start, stop, color):
        for col in range(start, stop + 1):
            if self.is_under_attack(row, col, color):
                return False
        return True

    # def is_under_attack(self, row, col, color):
    #     pieces = self.white_pieces if color == WHITE else self.black_pieces
    #     row_old = 0 if self.color == WHITE else 7
    #     for col_old, figure in enumerate(pieces):
    #         if pieces[col_old] != '-':
    #             if col_old % 7 == 1: row_old += 1
    #             if figure.can_attack(self, row_old, col_old % 7, row, col):
    #                 return True
    #     return False

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for k in range(8):
                if self.field[i][k] is not None:
                    currentPiece = self.field[i][k]
                    pieces = 1 if color == WHITE else 2
                    if currentPiece.color == pieces and currentPiece.can_move(self, i, k, row, col):
                        if isinstance(currentPiece, Pawn) and not currentPiece.can_attack(self, i, k, row, col):
                            continue
                        return True
        return False

    def castling0(self):
        row = 0 if self.color == WHITE else 7
        king = self.field[row][4]
        left_rook = self.field[row][0]
        right_rook = self.field[row][7]
        if type(king) is King and king.not_moved:
            # рокировка с левой ладьей
            if (type(left_rook) is Rook and left_rook.not_moved
                    and left_rook.can_move(self, row, 0, row, 3)
                    and self.clean_row(row, 1, 4, opponent(self.color))):
                self.field[row][2] = self.field[row][4]  # Поставить на новое место.
                self.field[row][4] = None  # Снять фигуру.
                self.field[row][3] = self.field[row][0]  # Поставить на новое место.
                self.field[row][0] = None
                self.color = opponent(self.color)
                return True

            # рокировка с правой ладьей
            if (type(right_rook) is Rook and right_rook.not_moved
                    and right_rook.can_move(self, row, 7, row, 5)
                    and self.clean_row(row, 4, 6, opponent(self.color))):
                self.field[row][6] = self.field[row][4]  # Поставить на новое место.
                self.field[row][4] = None  # Снять фигуру.
                self.field[row][5] = self.field[row][7]  # Поставить на новое место.
                self.field[row][7] = None
                self.color = opponent(self.color)
                return True
        return False

    def castling7(self):
        return self.castling0()


class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Rook(Piece):
    # Ладья ходит только по вертикали и только по диоганали
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        self.not_moved = False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(Piece):
    # Пешка ходит на 2 клетки вперед при 1-м ходе или на 1 клетку всегда
    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1 and board.field[row1][col1] is None:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    # "взятие на проходе" не реализовано
    def can_attack(self, board, row, col, row1, col1):
        if not (board.field[row1][col1] and board.field[row1][col1].color == opponent(self.color)):
            return False
        if self.color == WHITE and abs(col - col1) == row1 - row == 1:
            return True
        if self.color == BLACK and abs(col - col1) == row - row1 == 1:
            return True

        return False


class Knight(Piece):
    # Конь может ходить буквой "Г"
    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        # конь не может ходить по вертикали\горизонтали
        if row == row1 or col == col1:
            return False
        if abs(row1 - row) + abs(col1 - col) == 3:
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Bishop(Piece):
    # может ходить только по диагонали
    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        # Слон не может ходить по вертикали\горизонтали
        if row == row1 or col == col1:
            return False

        # в ходе по диагонали
        # смещение по горизонтали == смещению по вертикали
        if abs(row - row1) != abs(col - col1):
            return False

        step_row = 1 if (row1 >= row) else -1
        step_col = 1 if (col1 >= col) else -1
        for r, c in zip(range(row + step_row, row1, step_row), range(col + step_col, col1, step_col)):
            # Если на пути по диагонали есть фигура
            if board.get_piece(r, c) is not None:
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Queen(Piece):
    # может ходить как по вертикали/горизонтали, так и по диагонали
    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        # клетки совпадают
        if row == row1 and col == col1:
            return False

        # ход по вертикали
        if col == col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                # Если на пути по вертикали есть фигура
                if not (board.get_piece(r, col) is None):
                    return False
            return True

        # ход по горизонтали
        if row == row1:
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                # Если на пути по горизонтали есть фигура
                if not (board.get_piece(row, c) is None):
                    return False
            return True

        # ход по диагонали
        if row != row1 and col != col1:
            # в ходе по диагонали
            # смещение по горизонтали == смещению по вертикали
            if abs(row - row1) != abs(col - col1):
                return False

            step_row = 1 if (row1 >= row) else -1
            step_col = 1 if (col1 >= col) else -1
            for r, c in zip(range(row + step_row, row1, step_row),
                            range(col + step_col, col1, step_col)):
                # Если на пути по диагонали есть фигура
                if not (board.get_piece(r, c) is None):
                    return False
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True

    # может сходить на 1 клетку вокруг себя
    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if abs(row - row1) > 1 or abs(col - col1) > 1:
            return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


def main():
    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    board.field[0][0] = Rook(WHITE)
    board.field[0][4] = King(WHITE)
    board.field[0][7] = Rook(WHITE)

    board.field[7][0] = Rook(BLACK)
    board.field[7][4] = King(BLACK)
    board.field[7][7] = Rook(BLACK)

    print('before:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    print("Сдвиги ладей")
    board.move_piece(0, 0, 0, 1)
    board.move_piece(7, 0, 7, 1)
    print(board.castling0())
    print(board.castling7())

    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    print(board.castling0())
    print(board.castling7())

    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()


if __name__ == '__main__':
    main()
