# Есть два способа подключить дизайн
# Способ первый: подключить ui-файл.
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('check.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):

        self.check = ''
        self.finalCost = 0

        self.checkBox = [self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5]
        self.spinBox = [self.spinBox_1, self.spinBox_2, self.spinBox_3, self.spinBox_4, self.spinBox_5]
        self.cost = [self.cost_1, self.cost_2, self.cost_3, self.cost_4, self.cost_5]

        for i in range(len(self.checkBox)):
            if self.checkBox[i].isChecked() and self.spinBox[i].value() != 0:
                self.check += str('Товар: ' + self.checkBox[i].text() + '\nЦена за шт.: ' + self.cost[
                    i].text() + '\nКол-во: ' + str(self.spinBox[i].value()) + '\n')
                self.check += '   ' + self.cost[i].text() + ' * ' + str(self.spinBox[i].value()) + ' = ' + str(
                    self.spinBox[i].value() * int(self.cost[i].text())) + '\n\n'
                self.finalCost += self.spinBox[i].value() * int(self.cost[i].text())

        self.check += '\n\n\n\n' + 'Итого: ' + str(self.finalCost)
        if self.check[-2::] != ' 0':
            self.plainTextEdit.setPlainText(self.check)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
