import json
import os
import sys
from distutils.command.build_py import build_py_2to3

import PyQt5.QtWidgets as qtw

initial_todos = []


class Todo:

    def __init__(self, label: str, state: bool):
        self.label_ = label
        self.state_ = state
        self.checkbox_ = ""
        self.button_ = ""

    def removeTodo(self, todoList, todo):
        print(todo.label_)
        # todoList.remove(todo)

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

    def setCheckBox(self, checbox):
        self.checkbox_ = checbox

    def setButton(self, button):
        self.button_ = button

    def __str__(self):
        return f"{self.label_} {self.state_}"


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
            json.dump("", file)
            file.close()
            return []

    def save(self, todo):
        file = open(self.fileName, "w")
        json.dump(todo, file)
        file.close()


class Apps(qtw.QWidget):
    file = FileManager()

    def __init__(self):
        super(Apps, self).__init__()
        # self.file.loadFile()
        self.initTodo()
        self.todos = initial_todos
        self.setWindowTitle("ToDoApps")
        self.setLayout(qtw.QVBoxLayout())
        self.initUI()
        self.show()

    def initUI(self):

        newTodoContainer = qtw.QWidget()
        newTodoContainer.setLayout(qtw.QHBoxLayout())

        buttonAdd = qtw.QPushButton("Add")
        newTodoContainer.layout().addWidget(buttonAdd)

        labelInput = qtw.QLineEdit()
        newTodoContainer.layout().addWidget(labelInput)

        buttonAdd.clicked.connect(lambda: self.addTodo(labelInput.text()))

        self.layout().addWidget(newTodoContainer)

        for i in range(len(self.todos)):
            todoContainer = qtw.QWidget()
            todoContainer.setLayout(qtw.QHBoxLayout())

            # Button remove
            button = qtw.QPushButton("Remove")
            button.setObjectName(f"bt{i}")
            self.todos[i].setButton(button)
            todoContainer.layout().addWidget(button)
            button.clicked.connect(self.removeTodo)

            checkbox = qtw.QCheckBox()
            # initialiser les checkbox
            checkbox.setChecked(self.todos[i].getState())
            todoContainer.layout().addWidget(checkbox)
            # Add CheckBox Object
            self.todos[i].setCheckBox(checkbox)
            # Update State
            checkbox.stateChanged.connect(self.checkboxStateChanged)

            # label
            label = qtw.QLabel(self.todos[i].getLabel())
            todoContainer.layout().addWidget(label)

            self.layout().addWidget(todoContainer)

    def removeTodo(self, data=None):

        if not data:
            target = self.sender()
            data = target.objectName()

            for i in range(len(self.todos)):

                if self.todos[i].getButton().objectName() == data:

                    self.layout().removeWidget(target.parentWidget())

    def addTodo(self, label):

        error = qtw.QMessageBox()
        error.setIcon(qtw.QMessageBox.Warning)
        error.setText("Error")
        error.setWindowTitle("Error")

        if label != "":

            if not self.todoIsPresent(label):

                todo = Todo(label, False)

                todoContainer = qtw.QWidget()
                todoContainer.setLayout(qtw.QHBoxLayout())

                buttonRemove = qtw.QPushButton("Remove")
                # Get last id and set here
                buttonRemove.setObjectName(f"bt{(len(self.todos) - 1) + 1}")
                todoContainer.layout().addWidget(buttonRemove)

                checkbox = qtw.QCheckBox()
                todoContainer.layout().addWidget(checkbox)

                labeltext = qtw.QLabel(label)
                todoContainer.layout().addWidget(labeltext)

                self.layout().addWidget(todoContainer)

                self.todos.append(todo)

            else:
                error.setInformativeText('Todo is already present')
                error.exec()

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

            print(self.todos[i].getState())

    def initTodo(self):

        task = Todo("Faire a manger", True)
        task_2 = Todo("Faire ses devoirs", False)
        task_3 = Todo("Sortir le chien", True)

        initial_todos.append(task)
        initial_todos.append(task_2)
        initial_todos.append(task_3)


def launch():
    app = qtw.QApplication([])
    application = Apps()
    app.exec_()


launch()
