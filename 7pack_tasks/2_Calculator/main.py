# Есть два способа подключить дизайн
# Способ первый: подключить ui-файл.
import sys

import PyQt5.QtWidgets
from PyQt5 import uic


class MyWidget(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.operations = ('+', '-', '*', '/', '=', '.')
        self.brackets = ('(', ')')
        self.expression = str()
        self.bracketsNumber = [0, 0]
        uic.loadUi('calculator.ui', self)
        self.__temp = True

        self.pushButton_0.clicked.connect(lambda: self.push_digit_0(0))
        self.pushButton_1.clicked.connect(lambda: self.push_digit(1))
        self.pushButton_2.clicked.connect(lambda: self.push_digit(2))
        self.pushButton_3.clicked.connect(lambda: self.push_digit(3))
        self.pushButton_4.clicked.connect(lambda: self.push_digit(4))
        self.pushButton_5.clicked.connect(lambda: self.push_digit(5))
        self.pushButton_6.clicked.connect(lambda: self.push_digit(6))
        self.pushButton_7.clicked.connect(lambda: self.push_digit(7))
        self.pushButton_8.clicked.connect(lambda: self.push_digit(8))
        self.pushButton_9.clicked.connect(lambda: self.push_digit(9))
        self.pushButton_addition.clicked.connect(lambda: self.push_operation('+'))
        self.pushButton_minus.clicked.connect(lambda: self.push_operation('-'))
        self.pushButton_multiplication.clicked.connect(lambda: self.push_operation('*'))
        self.pushButton_division.clicked.connect(lambda: self.push_operation('/'))
        self.pushButton_comma.clicked.connect(self.float)
        self.pushButton_hooks.clicked.connect(self.push_bracket)
        self.pushButton_delete.clicked.connect(self.push_delete)
        self.pushButton_C.clicked.connect(self.push_C)
        self.pushButton_equally.clicked.connect(self.push_answer)

    def push_digit_0(self, digit):
        if len(self.expression) != 0 and self.expression[-1::] == ')':
            self.expression += '*'
        if len(self.expression) == 1 and self.expression[0] == '0':
            pass
        else:
            self.expression += str(digit)
            self.textBrowser.setText(self.expression)

    def push_digit(self, digit):
        if len(self.expression) != 0 and self.expression[-1::] == ')':
            self.expression += '*'
        if len(self.expression) != 0 and self.expression[0] == '0':
            self.expression = str(digit)
        else:
            self.expression += str(digit)
        self.textBrowser.setText(self.expression)

    def push_operation(self, operation):
        if self.expression[-1::] not in self.operations:
            if operation == '-' or (self.expression[-1::] != '(' and len(self.expression)):
                self.expression += str(operation)
                self.textBrowser.setText(self.expression)

    def float(self):
        i = len(self.expression) - 1
        while (i > 0):
            if self.expression[i] in self.operations or self.expression[i] in self.brackets:
                break
            i -= 1
        if i != -1:
            if (self.expression[i] != '.' and i != len(self.expression) - 1) or (
                    len(self.expression) == 1 and str.isdigit(self.expression[0])):
                self.expression += '.'
                self.textBrowser.setText(self.expression)

    def push_bracket(self):
        if self.expression[-1::] == '.':
            return
        if (str.isdigit(self.expression[-1::]) or self.expression[-1::] == ')') and self.bracketsNumber[0] == \
                self.bracketsNumber[1]:
            self.expression += str('*(')
            self.bracketsNumber[0] += 1
        elif len(self.expression) == 0 or self.expression[-1::] == '(':
            self.expression += str('(')
            self.bracketsNumber[0] += 1
        elif self.bracketsNumber[0] - self.bracketsNumber[1] == 0:
            pass
        elif self.bracketsNumber[0] - self.bracketsNumber[1] != 0:
            self.expression += str(')')
            self.bracketsNumber[1] += 1

        #     if len(self.expression) and (str.isdigit(self.expression[-1::]) or self.expression[-1::] == ')'):
        #         self.expression += '*'
        # else:
        #     if not len(self.expression) or self.expression[-1::] == '(' or self.expression[-1::] in self.operations:
        #         return
        #     self.bracketsNumber[1] += 1
        # self.expression += str(bracket)
        self.textBrowser.setText(self.expression)

    def push_answer(self):
        if not len(self.expression):
            self.textBrowser.setText('Введите выражение')
            return
        for i in range(0, len(self.expression)):
            if self.expression[0] != '(':
                break
            self.expression = self.expression[1:]
            self.bracketsNumber[0] = self.bracketsNumber[0] - 1

        for i in range(len(self.expression) - 1, 0, -1):
            if self.expression[0] != ')':
                break
            self.expression = self.expression[:-1:]
            self.bracketsNumber[1] = self.bracketsNumber[1] - 1

        if self.bracketsNumber[0] != self.bracketsNumber[1]:
            self.textBrowser.setText('Проверьте скобки')
            return

        try:
            eval_result = eval(self.expression)
        except ZeroDivisionError:
            self.textBrowser.setText('На ноль делить нельзя')
        except:
            self.textBrowser.setText('Ошибка')
        else:
            output_result = str(round(eval_result, 10))
            if output_result[-2::] == '.0':
                output_result = output_result[:-2:]
            self.expression = str(output_result)
            self.textBrowser.setText(output_result)

    def push_C(self):
        if len(self.expression) == 1:
            self.expression = ''
        else:
            self.expression = self.expression[:-1:]
        self.textBrowser.setText(self.expression)

    def push_delete(self):
        self.expression = ''
        self.textBrowser.setText(self.expression)


app = PyQt5.QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
