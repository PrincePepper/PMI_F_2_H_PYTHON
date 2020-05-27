# Есть два способа подключить дизайн
# Способ первый: подключить ui-файл.
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('HTML_editor.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.output.setText(self.input.toPlainText())


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
