from math import sqrt

import PyQt5.QtWidgets as qtw


class Calculator(qtw.QWidget):
    buttons = []
    #history = []

    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calcultor")
        self.setLayout(qtw.QVBoxLayout())
        self.initkeyPad()
        self.initUI()
        self.setFixedSize(410, 420)
        self.show()

    def initUI(self):
        self.result.setStyleSheet("QLineEdit { "
                                  "border: 1px solid #ef233c; "
                                  "color : #ef233c;"
                                  "font-size: 15px;"
                                  "}")
        self.setStyleSheet("background-color: #2b2d42;")
        for btn in self.buttons:
            btn.setFlat(True)
            btn.setStyleSheet("color: #ef233c; border: 1px solid #ef233c; font-size: 15px;")

    def initkeyPad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # create input for resultat
        self.result = qtw.QLineEdit()
        self.result.setReadOnly(True)

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
        btn_point = qtw.QPushButton('.')
        btn_more = qtw.QPushButton('+')
        btn_minus = qtw.QPushButton('-')
        btn_times = qtw.QPushButton('*')
        btn_divided = qtw.QPushButton('/')
        btn_enter = qtw.QPushButton('=')
        btn_clear = qtw.QPushButton('C')
        btn_erase = qtw.QPushButton('←')
        btn_modulo = qtw.QPushButton('%')
        btn_squareRoot = qtw.QPushButton('√')
        #btn_history = qtw.QPushButton("H", clicked=self.historyList)

        # Add buttons to list
        self.buttons.append(btn_0)
        self.buttons.append(btn_1)
        self.buttons.append(btn_2)
        self.buttons.append(btn_3)
        self.buttons.append(btn_4)
        self.buttons.append(btn_5)
        self.buttons.append(btn_6)
        self.buttons.append(btn_7)
        self.buttons.append(btn_8)
        self.buttons.append(btn_9)
        self.buttons.append(btn_point)
        self.buttons.append(btn_more)
        self.buttons.append(btn_minus)
        self.buttons.append(btn_times)
        self.buttons.append(btn_divided)
        self.buttons.append(btn_enter)
        self.buttons.append(btn_clear)
        self.buttons.append(btn_erase)
        self.buttons.append(btn_modulo)
        self.buttons.append(btn_squareRoot)
        #self.buttons.append(btn_history)

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
        btn_point.clicked.connect(lambda: self.onClick(btn_point))
        btn_more.clicked.connect(lambda: self.onClick(btn_more))
        btn_minus.clicked.connect(lambda: self.onClick(btn_minus))
        btn_times.clicked.connect(lambda: self.onClick(btn_times))
        btn_divided.clicked.connect(lambda: self.onClick(btn_divided))
        btn_enter.clicked.connect(lambda: self.onClick(btn_enter))
        btn_clear.clicked.connect(lambda: self.onClick(btn_clear))
        btn_erase.clicked.connect(lambda: self.onClick(btn_erase))
        btn_modulo.clicked.connect(lambda: self.onClick(btn_modulo))
        btn_squareRoot.clicked.connect(lambda: self.onClick(btn_squareRoot))

        # add label for display result
        container.layout().addWidget(self.result, 0, 0, 1, 4)

        container.layout().addWidget(btn_modulo, 1, 0)
        container.layout().addWidget(btn_squareRoot, 1, 1)
        container.layout().addWidget(btn_erase, 1, 2)
        container.layout().addWidget(btn_clear, 1, 3)

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

        container.layout().addWidget(btn_0, 5, 0, 1, 2)
        container.layout().addWidget(btn_point, 5, 2)
        container.layout().addWidget(btn_divided, 5, 3)

        container.layout().addWidget(btn_enter, 6, 0, 1, 4)
        #container.layout().addWidget(btn_history, 6, 3)

        self.layout().addWidget(container)

    def onClick(self, button):

        if button.text().__eq__("="):
            self.checkError()
            self.calcul()

        elif button.text().__eq__("←"):
            self.result.setText(self.result.text()[:-1])

        elif button.text().__eq__("C"):
            self.result.setText("")

        else:
            self.result.setText(self.result.text() + button.text())

    def checkError(self):
        if self.result.text().__eq__("0/0"):
            self.result.setText("Erreur : division impossible")

        elif self.result.text().__contains__("√") and self.result.text().__contains__("+") \
                or self.result.text().__contains__("√") and self.result.text().__contains__("-") \
                or self.result.text().__contains__("√") and self.result.text().__contains__("*") \
                or self.result.text().__contains__("√") and self.result.text().__contains__("/") \
                or self.result.text().__contains__("√") and self.result.text().__contains__("%"):
            self.result.setText("Erreur : impossible d'effectuer ce calcul")

        elif self.result.text().__eq__("√") or self.result.text().__eq__("*") or self.result.text().__eq__("/") \
                or self.result.text().__eq__("+") or self.result.text().__eq__("-") or self.result.text().__eq__("%"):
            self.result.setText("Erreur : impossible d'effectuer ce calcul")

        elif self.result.text().count("√") >= 2 or self.result.text().count("+") >= 2 or self.result.text().count("-") >= 2 \
                or self.result.text().count("*") >=2 or self.result.text().count("/") >=2 or self.result.text().count("%") >= 2:
            self.result.setText("Erreur : calcul invalide")

    def calcul(self):

        if self.result.text().__contains__("+"):

            if self.result.text().__contains__("."):
                number = float(self.result.text().split("+")[0])
                number_2 = float(self.result.text().split("+")[1])
            else:
                number = int(self.result.text().split("+")[0])
                number_2 = int(self.result.text().split("+")[1])

            res = number + number_2
            self.result.setText(str(res))
            #self.history.append(f"{number} + {number_2} = {res}")

        elif self.result.text().__contains__("-"):

            if self.result.text().__contains__("."):
                number = float(self.result.text().split("-")[0])
                number_2 = float(self.result.text().split("-")[1])
            else:
                number = int(self.result.text().split("-")[0])
                number_2 = int(self.result.text().split("-")[1])

            res = number - number_2
            self.result.setText(str(res))

        elif self.result.text().__contains__("*"):

            if self.result.text().__contains__("."):
                number = float(self.result.text().split("*")[0])
                number_2 = float(self.result.text().split("*")[1])
            else:
                number = int(self.result.text().split("*")[0])
                number_2 = int(self.result.text().split("*")[1])

            res = number * number_2
            self.result.setText(str(res))

        elif self.result.text().__contains__("/"):

            if self.result.text().__contains__("."):
                number = float(self.result.text().split("/")[0])
                number_2 = float(self.result.text().split("/")[1])
            else:
                number = int(self.result.text().split("/")[0])
                number_2 = int(self.result.text().split("/")[1])

            res = number / number_2
            self.result.setText(str(res))

        elif self.result.text().__contains__("%"):

            if self.result.text().__contains__("."):
                number = float(self.result.text().split("%")[0])
                number_2 = float(self.result.text().split("%")[1])
            else:
                number = int(self.result.text().split("%")[0])
                number_2 = int(self.result.text().split("%")[1])

            res = number % number_2
            self.result.setText(str(res))

        elif self.result.text().__contains__("√"):

            if self.result.text().__contains__("."):
                number = float(self.result.text()[1:len(self.result.text())])
            else:
                number = int(self.result.text()[1:len(self.result.text())])

            res = sqrt(number)
            self.result.setText(str(res))


def launch():
    app = qtw.QApplication([])
    Calculator()
    app.exec()


launch()
