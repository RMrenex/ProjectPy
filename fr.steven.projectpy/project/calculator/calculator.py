import PyQt5.QtWidgets as qtw


class Calculator(qtw.QWidget):

    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calcultor")
        self.setLayout(qtw.QVBoxLayout())
        self.initkeyPad()
        self.show()

    def initkeyPad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # create label for resultat
        self.result = qtw.QLineEdit()
        self.result.setReadOnly(True)
        """self.operator = qtw.QLabel()
        self.number = qtw.QLineEdit()
        self.number_2 = qtw.QLineEdit()"""

        # create the buttons
        btn_0 = qtw.QPushButton('0')
        btn_1 = qtw.QPushButton('1')
        btn_2 = qtw.QPushButton('2')
        btn_3 = qtw.QPushButton('3')
        btn_4 = qtw.QPushButton('4')
        btn_5 = qtw.QPushButton('5')
        btn_6 = qtw.QPushButton('6')
        btn_7 = qtw.QPushButton('7')
        btn_8 = qtw.QPushButton('8')
        btn_9 = qtw.QPushButton('9')
        btn_more = qtw.QPushButton('+')
        btn_minus = qtw.QPushButton('-')
        btn_times = qtw.QPushButton('*')
        btn_divided = qtw.QPushButton('/')
        btn_enter = qtw.QPushButton('=')
        btn_clear = qtw.QPushButton('C')

        # add buttons event click
        btn_0.clicked.connect(lambda: self.onClick(btn_0))
        btn_1.clicked.connect(lambda: self.onClick(btn_1))
        btn_2.clicked.connect(lambda: self.onClick(btn_2))
        btn_3.clicked.connect(lambda: self.onClick(btn_3))
        btn_4.clicked.connect(lambda: self.onClick(btn_4))
        btn_5.clicked.connect(lambda: self.onClick(btn_5))
        btn_6.clicked.connect(lambda: self.onClick(btn_6))
        btn_7.clicked.connect(lambda: self.onClick(btn_7))
        btn_8.clicked.connect(lambda: self.onClick(btn_8))
        btn_9.clicked.connect(lambda: self.onClick(btn_9))
        btn_more.clicked.connect(lambda: self.onClick(btn_more))
        btn_minus.clicked.connect(lambda: self.onClick(btn_minus))
        btn_times.clicked.connect(lambda: self.onClick(btn_times))
        btn_divided.clicked.connect(lambda: self.onClick(btn_divided))
        btn_enter.clicked.connect(lambda: self.onClick(btn_enter))
        btn_clear.clicked.connect(lambda: self.onClick(btn_clear))

        # add label for display result
        container.layout().addWidget(self.result, 0, 0, 1, 4)
        """container.layout().addWidget(self.operator, 0, 1)
        container.layout().addWidget(self.number_2, 0, 2)
        container.layout().addWidget(self.result, 0, 3)"""

        container.layout().addWidget(btn_enter, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)

        # add buttons to layout
        container.layout().addWidget(btn_7, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_9, 2, 2)
        container.layout().addWidget(btn_more, 2, 3)

        container.layout().addWidget(btn_4, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_6, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)

        container.layout().addWidget(btn_1, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_3, 4, 2)
        container.layout().addWidget(btn_times, 4, 3)

        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divided, 5, 3)

        self.layout().addWidget(container)

    def onClick(self, button):

        if button.text().__eq__("="):
            self.calcul()
        elif button.text().__eq__("C"):
            self.result.setText("")
        else:
            self.result.setText(self.result.text() + button.text())

    def calcul(self):
        if self.result.text().__contains__("+"):
            number = int(self.result.text().split("+")[0])
            number_2 = int(self.result.text().split("+")[1])
            res = number + number_2
            self.result.setText(str(res))
        elif self.result.text().__contains__("-"):
            number = int(self.result.text().split("-")[0])
            number_2 = int(self.result.text().split("-")[1])
            res = number - number_2
            self.result.setText(str(res))
        elif self.result.text().__contains__("*"):
            number = int(self.result.text().split("*")[0])
            number_2 = int(self.result.text().split("*")[1])
            res = number * number_2
            self.result.setText(str(res))
        elif self.result.text().__contains__("/"):
            number = int(self.result.text().split("/")[0])
            number_2 = int(self.result.text().split("/")[1])
            res = number / number_2
            self.result.setText(str(res))


def launch():
    app = qtw.QApplication([])
    Calculator()
    app.exec()


launch()
