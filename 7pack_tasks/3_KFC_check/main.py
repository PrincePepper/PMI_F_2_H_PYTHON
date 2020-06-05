# Есть два способа подключить дизайн
# Способ первый: подключить ui-файл.
import sys

import PyQt5.QtWidgets
from PyQt5 import uic


class MyWidget(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('check.ui', self)
        self.__temp = True
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.__temp = True
        self.__cost = [self.cost_1, self.cost_2, self.cost_3, self.cost_4, self.cost_5]
        self.__spinBox = [self.spinBox_1, self.spinBox_2, self.spinBox_3, self.spinBox_4, self.spinBox_5]
        self.__checkBox = [self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5]
        self.__finalCost = 0
        self.check = ''
        for i in range(len(self.__checkBox)):
            if self.__checkBox[i].isChecked() and self.__spinBox[i].value() != 0:
                self.__temp = False
                self.check += str('Товар: ' + self.__checkBox[i].text() + '\nЦена за шт.: ' + self.__cost[
                    i].text() + '\nКол-во: ' + str(self.__spinBox[i].value()) + '\n')
                self.check += '   ' + self.__cost[i].text() + ' * ' + str(self.__spinBox[i].value()) + ' = ' + str(
                    self.__spinBox[i].value() * int(self.__cost[i].text())) + '\n\n'
                self.__finalCost += self.__spinBox[i].value() * int(self.__cost[i].text())

        if self.__temp:
            self.plainTextEdit.setPlainText(self.check)
        else:
            self.check += '\n\n\n\n' + 'Итого: ' + str(self.__finalCost)
            if self.check[-2::] != ' 0':
                self.plainTextEdit.setPlainText(self.check)


app = PyQt5.QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
