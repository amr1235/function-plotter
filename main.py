from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow
import sys
import lib.interface as interface
import lib.plot as plt
from PyQt5.QtWidgets import QMessageBox

class Ui(QMainWindow):
    def __init__(self) -> None :
        super(Ui, self).__init__()
        uic.loadUi("UI.ui", self)
        self.plotButton.clicked.connect(self.plot_button_clicked)

    def error(self, error_message) -> None:
        QMessageBox.critical(self, "Error", error_message)

    def plot_button_clicked(self) -> None:

        # check the funtion string
        if(not interface.isFunction(self.functionText.text())) :
            self.error("Invalide Function")
            return 
        
        # check minimum and maximum value
        valide_min_max = interface.valide_min_max(self.minValue.value(),self.maxValue.value())
        if(not valide_min_max) :
            self.error("Minimum value should be smaller than the maximum value")
            return
        
        # plot function
        graph = plt.PLOT(self.functionText.text(),self.minValue.value(),self.maxValue.value())
        graph.plot()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())