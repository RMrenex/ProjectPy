class Todo:

    def __init__(self, label, state):
        self.label_ = label
        self.state_ = state

    def getLabel(self):
        return self.label_

    def getState(self):
        return self.state_

    def setLabel(self, label):
        self.label_ = label

    def setState(self, state):
        self.state_ = state
