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
                result+=('\t'+str(task))
            return f"{result}\n"
    
    def find_by_name_in_tl(self, t_name:str):  # tl : task-list
        if(len(self.list_of_tasks)<=0):
            return Status.EMPTY #  print("list was empty. go and add some tasks to it!")  IN UI.PY 
        # for i in range(len(self.list_of_tasks)):
        #     if(self.list_of_tasks[i].name == t_name):
        #         return i
        for index, task in enumerate(self.list_of_tasks):
            if(task.name == t_name):
                return index
        else:
            return Status.NOT_FOUND #  print(f"task \"{t_name}\" was not found")  #  OR print(f' "{variable}"  ')  IN UI.PY

    def find_by_id_in_tl(self, t_id:any):
        if(len(self.list_of_tasks)<=0):
            return Status.EMPTY  #  print("list was empty. go and add some tasks to it!")  IN UI.PY
        # for i in range(len(self.list_of_tasks)):
        #     if(self.list_of_tasks[i].id == int(t_id)):
        #         return i
        for index, task in enumerate(self.list_of_tasks):
            if(task.id == t_id):
                return index
        else:
            return Status.NOT_FOUND #  print(f"task with ID:{t_id} was not found")  IN UI.PY

    def add_task(self, task:Task):
        result = self.find_by_name_in_tl(task.name)
        if(not isinstance(result, Status)):  # type(result)!=Status
            return Status.DUPLICATE #  print(f"task with name \"{task.name}\" already exists!\n")
        self.list_of_tasks.append(task)
        return Status.SUCCESS
    
    def delete_task_by_id(self, t_id:any):
        result = self.find_by_id_in_tl(t_id) 
        if(not isinstance(result, Status)):  # type(result)!=Status
            del self.list_of_tasks[result]
            return Status.SUCCESS
        return Status.NOT_FOUND
    
    def delete_task_by_name(self, t_name:str):
        result = self.find_by_name_in_tl(t_name) 
        if(not isinstance(result, Status)):  # type(result)!=Status
            del self.list_of_tasks[result]
            return Status.SUCCESS
        return Status.NOT_FOUND
    
        
class ToDoManager():
    def __init__(self):
        self.list_of_task_lists = []
    
    def find_task_list(self, tl_name:str):
        if(len(self.list_of_task_lists)<=0):
            return Status.EMPTY
        for index, task_list in enumerate(self.list_of_task_lists):
            if(task_list.name == tl_name):
                return index
        else:
            return Status.NOT_FOUND

    def add_task_list(self, task_list:TaskList):
        result = self.find_task_list(task_list.name)
        if(not isinstance(result, Status)):
            return Status.DUPLICATE
        self.list_of_task_lists.append(task_list)
        return Status.SUCCESS
    
    def delete_task_list(self, tl_name:str):
        result = self.find_task_list(tl_name)
        if(not isinstance(result, Status)):
            del self.list_of_task_lists[result]
            return Status.SUCCESS
        return Status.NOT_FOUND

#MadMad_131