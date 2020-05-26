import sys

import HTML_editor
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, HTML_editor.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
