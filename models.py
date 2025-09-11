from messages import MESSAGES

class Task():
    task_id_counter = 0
    min_importance = 1
    max_importance = 10

    def __init__(self, name:str, description:str, importance:int):
        self.task_status = False
        self.name = name
        self.description = description
        self.importance = importance  # control in app.py or ui.py (int, 1<imp<=10)
        Task.task_id_counter += 1
        self.id = Task.task_id_counter
        
    def __str__(self):
        return f"{self.id}.{self.name}({self.importance}/{Task.max_importance}) : {self.description}\n"

    def change_status(self):
        self.task_status = not self.task_status
        # if(self.task_status):
        #     self.task_status = False
        # else:
        #     self.task_status = True

    def change_name(self, new_name):  # control in app.py or ui.py (str)
        self.name = new_name

    def change_description(self, new_description):  # control in app.py or ui.py (str)
        self.description = new_description

    def change_importance(self, new_importance):  # control in app.py or ui.py (int, 1<imp<=10)
        self.importance = new_importance


class TaskList():
    def __init__(self):
        pass
        
class Manager():
    def __init__(self):
        pass

#MadMad_44