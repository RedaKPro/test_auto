class TaskManager:
    def __init__(self):
        self.tasks = [2]

    def parse(self, command):
        return Action("delete", command[2:])


class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description

