from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow
import sys


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("UI.ui", self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())