import csv
import sys

from PyQt5 import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem


class MyWidget(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('table.ui', self)
        self.mass = []

        self.loadTable('rat.csv')

    def loadTable(self, table_name):

        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            title = next(reader)[2:]
            title.append('N')
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for index, row in enumerate(reader):
                if index > 0:
                    self.mass.append(row[2:])

        for i, row in enumerate(self.mass):
            aaa = 0
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(elem))
                if j > 0:
                    if row[j].isdigit():
                        aaa += float(row[j])
                    else:
                        my_str = row[j].replace(',', '.')
                        aaa += float(my_str)
            self.table.setItem(i, self.table.columnCount() - 1, QTableWidgetItem(str(round(aaa / 8))))
            self.colorRow(i, int(round(aaa / 8)))
        self.table.resizeColumnsToContents()

    def colorRow(self, row, value):
        if value > 95:
            self.table.item(row, 0).setBackground(Qt.QColor('green'))
        elif value > 80:
            self.table.item(row, 0).setBackground(Qt.QColor('yellow'))
        else:
            self.table.item(row, 0).setBackground(Qt.QColor('red'))


app = Qt.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
