import PyQt5.QtWidgets as qtw


class Apps(qtw.QWidget):
    initial_todos = []

    def __init__(self):
        super(Apps, self).__init__()
        self.setWindowTitle("ToDoApps")
        self.setLayout(qtw.QVBoxLayout())
        self.show()
        len(self.initial_todos)

    def initUI(self):
        print("test")

    def initTodo(self):
        task = Todo("Faire a manger", True)
        task_2 = Todo("Faire ses devoirs", False)
        task_3 = Todo("Sortir le chien", False)

        self.initial_todos.append(task)
        self.task_2.initial_todos.append(task)
        self.task_3.initial_todos.append(task)


def launch():
    app = qtw.QApplication([])
    Apps()
    app.exec_()


launch()
