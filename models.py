from messages import MESSAGES
from enum import Enum

class Status(Enum):
    SUCCESS = 1
    NOT_FOUND = -1
    DUPLICATE = -2
    EMPTY = 0


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
        return f"{self.id}.{self.name}({self.importance}/{Task.max_importance})\t: {self.description}\n"

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
    def __init__(self, name:str):
        self.list_of_tasks = []
        self.name = name
    
    def __str__(self):
        if(len(self.list_of_tasks)<=0):
            return f"{self.name}: (empty)\n"
        else:
            result = f"{self.name}:\n"
            for task in self.list_of_tasks:
                result+=str(task)
            return f"{result}\n"
    
    def search_by_name_in_tl(self, task_name:str):  # tl : task-list
        if(len(self.list_of_tasks)<=0):
            return Status.EMPTY #  print("list was empty. go and add some tasks to it!")  IN UI.PY
        else: 
            # for i in range(len(self.list_of_tasks)):
            #     if(self.list_of_tasks[i].name == task_name):
            #         return i
            for index, task in enumerate(self.list_of_tasks):
                if(task.name == task_name):
                    return index
            else:
                return Status.NOT_FOUND #  print(f"task \"{task_name}\" was not found")  #  OR print(f' "{variable}"  ')  IN UI.PY

    def search_by_id_in_tl(self, task_id:any):
        if(len(self.list_of_tasks)<=0):
            return Status.EMPTY  #  print("list was empty. go and add some tasks to it!")  IN UI.PY
        else: 
            # for i in range(len(self.list_of_tasks)):
            #     if(self.list_of_tasks[i].id == int(task_id)):
            #         return i
            for index, task in enumerate(self.list_of_tasks):
                if(task.id == task_id):
                    return index
            else:
                return Status.NOT_FOUND #  print(f"task with ID:{task_id} was not found")  IN UI.PY

    def add_task(self, task:Task):
        result = self.search_by_name_in_tl(task.name)
        if(not isinstance(result, Status)):  # type(result)!=Status
            return Status.DUPLICATE #  print(f"task with name \"{task.name}\" already exists!\n")
        self.list_of_tasks.append(task)
        return Status.SUCCESS
    
    def delete_task_by_id(self, task_id:any):
        result = self.search_by_id_in_tl(task_id) 
        if(not isinstance(result, Status)):  # type(result)!=Status
            del self.list_of_tasks[result]
            return Status.SUCCESS
        return Status.NOT_FOUND
    
    def delete_task_by_name(self, task_name:str):
        result = self.search_by_name_in_tl(task_name) 
        if(not isinstance(result, Status)):  # type(result)!=Status
            del self.list_of_tasks[result]
            return Status.SUCCESS
        return Status.NOT_FOUND

        
class Manager():
    def __init__(self):
        pass

#MadMad_110