import json

import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

initial_todos = []
json_todos = []


class Todo:

    def __init__(self, label: str, state: bool, checkbox: qtw.QCheckBox = None, button: qtw.QPushButton = None):
        self.label_ = label
        self.state_ = state
        self.checkbox_ = checkbox
        self.button_ = button

    def getLabel(self):
        return self.label_

    def getState(self):
        return self.state_

    def getCheckBox(self):
        return self.checkbox_

    def getButton(self):
        return self.button_

    def setLabel(self, label):
        self.label_ = label

    def setState(self, state):
        self.state_ = state

    def setCheckBox(self, checkbox):
        self.checkbox_ = checkbox

    def setButton(self, button):
        self.button_ = button

    def toJson(self):
        return {
            "label": self.label_,
            "state": self.state_,
            "checkbox": f"{self.checkbox_}",
            "button": f"{self.button_}"
        }


class FileManager:
    fileName = "data.json"

    def loadFile(self):
        try:

            file = open(self.fileName, "r")
            todo = json.load(file)
            file.close()
            return todo
        except FileNotFoundError:
            file = open(self.fileName, "w")
            json.dump([], file)
            file.close()
            return []

    def save(self):
        file = open(self.fileName, "w")
        json.dump(json_todos, file)
        file.close()


class Apps(qtw.QWidget):
    file = FileManager()

    def __init__(self):
        super(Apps, self).__init__()
        self.initTodo()
        self.todos = initial_todos
        self.setWindowTitle("ToDoApps")
        self.setLayout(qtw.QVBoxLayout())
        self.initUI()
        self.show()

    def initUI(self):

        self.setStyleSheet("background-color: #f4d58d;")

        newTodoContainer = qtw.QWidget()
        newTodoContainer.setLayout(qtw.QHBoxLayout())

        buttonAdd = qtw.QPushButton("Add")
        buttonAdd.setFlat(True)
        buttonAdd.setStyleSheet("color: #001427; border: 3px solid #001427; width: 50px; font-size: 15px;")
        newTodoContainer.layout().addWidget(buttonAdd)

        labelInput = qtw.QLineEdit()
        labelInput.setStyleSheet("QLineEdit { "
                                 "border: 3px solid #001427; "
                                 "color : #001427;"
                                 "font-size: 15px;"
                                 "}")
        newTodoContainer.layout().addWidget(labelInput)

        buttonAdd.clicked.connect(lambda: self.addTodo(labelInput))

        self.layout().addWidget(newTodoContainer)

        if self.todos:

            for i in range(len(self.todos)):
                todoContainer = qtw.QWidget()
                todoContainer.setLayout(qtw.QHBoxLayout())

                # Button
                button = qtw.QPushButton("Remove")
                button.setFlat(True)
                button.setStyleSheet("color: #001427; border: 3px solid #001427; width: 50px; font-size: 15px;")
                button.setObjectName(f"bt{i}")
                self.todos[i].setButton(button)
                todoContainer.layout().addWidget(button)
                button.clicked.connect(self.removeTodo)

                # Checkbox
                checkbox = qtw.QCheckBox()
                checkbox.setChecked(self.todos[i].getState())
                todoContainer.layout().addWidget(checkbox)
                self.todos[i].setCheckBox(checkbox)

                # Label
                label = qtw.QLabel(self.todos[i].getLabel())
                label.setStyleSheet("border-bottom: 3px solid #001427; font-size: 15px;")
                todoContainer.layout().addWidget(label)

                self.layout().addWidget(todoContainer)

                json_todos.append(self.todos[i].toJson())

            FileManager().save()

        """else:

            self.labelContainer = qtw.QWidget()
            self.labelContainer.setLayout(qtw.QHBoxLayout())

            labelNone = qtw.QLabel("No todo for the moment")
            labelNone.setAlignment(Qt.AlignCenter)
            self.labelContainer.layout().addWidget(labelNone)
            self.layout().addWidget(self.labelContainer)"""

    def removeTodo(self, data=None):

        if not data:

            target = self.sender()
            data = target.objectName()
            index = 0

            for todo in self.todos:

                if todo.getButton().objectName() == data:
                    self.layout().removeWidget(target.parentWidget())
                    self.todos.remove(todo)

                    try:
                        json_todos.pop(index)
                        FileManager().save()
                    except IndexError:
                        print("Index bound of exception")

                index += 1

    def addTodo(self, label):

        error = qtw.QMessageBox()
        error.setIcon(qtw.QMessageBox.Warning)
        error.setText("Error")
        error.setWindowTitle("Error")

        if label.text() != "":

            if not self.todoIsPresent(label.text()):

                todo = Todo(label.text(), False)

                todoContainer = qtw.QWidget()
                todoContainer.setLayout(qtw.QHBoxLayout())

                buttonRemove = qtw.QPushButton("Remove")
                buttonRemove.setFlat(True)
                buttonRemove.setStyleSheet("color: #001427; border: 3px solid #001427; width: 50px; font-size: 15px;")
                buttonRemove.setObjectName(f"bt{(len(self.todos) - 1) + 1}")
                todoContainer.layout().addWidget(buttonRemove)
                buttonRemove.clicked.connect(self.removeTodo)

                checkbox = qtw.QCheckBox()
                todoContainer.layout().addWidget(checkbox)

                checkbox.stateChanged.connect(self.checkboxStateChanged)

                labeltext = qtw.QLabel(label.text())
                labeltext.setStyleSheet("border-bottom: 3px solid #001427; font-size: 15px;")
                todoContainer.layout().addWidget(labeltext)

                self.layout().addWidget(todoContainer)

                todo.setButton(buttonRemove)
                todo.setCheckBox(checkbox)
                self.todos.append(todo)

                json_todos.append(todo.toJson())

                FileManager().save()

                label.setText("")

            else:
                error.setInformativeText('Todo is already present')
                error.exec()
                label.setText("")

        else:
            error.setInformativeText('Label cannot not be null')
            error.exec()

    def todoIsPresent(self, label):

        for todo in self.todos:

            if todo.getLabel().lower() == label.lower():
                return True

        return False

    def checkboxStateChanged(self):

        for i in range(len(self.todos)):

            if self.todos[i].getCheckBox():
                self.todos[i].setState(self.todos[i].getCheckBox().isChecked())
                json_todos[i]["state"] = self.todos[i].getCheckBox().isChecked()
                FileManager().save()

    def initTodo(self):

        file = FileManager()
        json_object = file.loadFile()

        if not json_object == []:

            for element in json_object:
                initial_todos.append(Todo(element["label"], element["state"], element["checkbox"], element["button"]))


def launch():
    app = qtw.QApplication([])
    application = Apps()
    app.exec_()


launch()
