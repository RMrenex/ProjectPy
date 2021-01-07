import PyQt5.QtWidgets as qtw


class Calculator(qtw.QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calcultor")
        self.show()


app = qtw.QApplication([])
calculator = Calculator()
app.exec()
