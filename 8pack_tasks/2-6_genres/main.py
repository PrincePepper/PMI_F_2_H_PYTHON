import sqlite3
import sys

from PyQt5 import Qt, QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QDialog, QDialogButtonBox


class MyWidget(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('films.ui', self)
        self.con = sqlite3.connect("../films.db")
        self.cur = self.con.cursor()
        self.reader = []
        self.genre = []
        self.loadTable()
        self.updateB.clicked.connect(self.edit_cell)
        self.findB.clicked.connect(lambda: self.pushB(self.genre))
        self.addB.clicked.connect(lambda: AddFilms.show())

    def loadTable(self):
        self.genre = self.cur.execute("SELECT * FROM genres").fetchall()
        self.genreBox.addItem('Все')
        for i in self.genre:
            self.genreBox.addItem(i[1])
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['id', 'Название', 'Год', 'Жанр', 'Длительность'])
        self.table.setRowCount(0)
        self.reader = self.cur.execute("SELECT * FROM films").fetchall()
        for i, row in enumerate(self.reader):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    elem = self.genres(self.genre, elem)
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()

    def pushB(self, genres):
        title = '%'
        genre_name = 0
        year_name = '%'
        duraction_name = 0
        if self.name.toPlainText():
            title = self.name.toPlainText() + '%'
        for i in genres:
            if self.genreBox.currentText() == i[1]:
                genre_name = i[0]
                break
        if self.yearEdit.toPlainText().isdigit():
            year_name = self.yearEdit.toPlainText() + '%'
        if self.duractionEdit.toPlainText().isdigit():
            duraction_name = int(self.duractionEdit.toPlainText())
        if genre_name != 0:
            self.reader = self.cur.execute(
                "SELECT * FROM Films WHERE genre == ? and title LIKE ? and year LIKE ? and duration >= ?",
                (genre_name, title, year_name, duraction_name)).fetchall()
        else:
            self.reader = self.cur.execute(
                "SELECT * FROM Films WHERE genre LIKE '%' and title LIKE ? and year LIKE ? and duration >= ?",
                (title, year_name, duraction_name)).fetchall()
        self.table.setRowCount(0)
        for i, row in enumerate(self.reader):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    elem = self.genres(genres, elem)
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()

    def edit_cell(self):
        new_table = []
        old_table = self.reader
        for i in range(len(old_table)):
            id = self.table.item(i, 0).text()
            name = self.table.item(i, 1).text()
            year = self.table.item(i, 2).text()
            time = self.table.item(i, 3).text()
            new_table.append((id, name, year, time))
        for n, i in enumerate(new_table):
            if i[1] != old_table[n][1]:
                self.cur.execute(f'UPDATE films SET title = \'{i[1]}\' WHERE id = \'{i[0]}\'')
            if i[2] != str(old_table[n][2]):
                self.cur.execute(f'UPDATE films SET year = \'{i[2]}\' WHERE id = \'{i[0]}\'')
            if i[3] != str(self.genres(self.genre, old_table[n][3])):
                self.cur.execute(f'UPDATE films SET duration = \'{i[3]}\' WHERE id = \'{i[0]}\'')
        self.con.commit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            DeleteFilms.show()

    @staticmethod
    def genres(genres, genre):
        for i in genres:
            if genre == i[0]:
                return i[1]
        return "NOPE"


class AddFilms(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addfilms.ui', self)
        for i in ex.genre:
            self.genre.addItem(i[1])
        self.pushButton.clicked.connect(lambda: self.load())

    def load(self):
        name = self.name.toPlainText()
        genre = 0
        for i in ex.genre:
            if self.genre.currentText() == i[1]:
                genre = i[0]
                break
        year = int(self.year.toPlainText())
        dur = int(self.dur.toPlainText())
        bd = ex.cur.execute("SELECT * FROM Films WHERE genre == ? and title == ? and year == ? and duration == ?",
                            (genre, name, year, dur)).fetchall()
        if len(name) != 0 and year != 0 and dur != 0 and len(bd) == 0:
            ex.cur.execute("INSERT INTO films(title, genre,year,duration) VALUES(?,?,?,?)", (name, genre, year, dur))
        self.name.clear()
        self.year.clear()
        self.dur.clear()
        ex.con.commit()
        self.close()


class DeleteFilms(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('deletefilms.ui', self)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        indexes = ex.table.selectionModel().selectedIndexes()
        for i in range(0, len(indexes)):
            ex.cur.execute("DELETE from Films WHERE id = ?", (ex.reader[indexes[i].row()][0],))
            ex.table.removeRow(indexes[i].row())
        ex.con.commit()
        self.close()


app = Qt.QApplication(sys.argv)
ex = MyWidget()
ex.show()
AddFilms = AddFilms()
DeleteFilms = DeleteFilms()
sys.exit(app.exec_())
