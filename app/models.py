from typing import List, Dict, Union
from enum import Enum
class Status(Enum):
    NOT_COMPLETED = 0  # False
    COMPLETED = 1  # True
    SUCCESS = 2
    CONTINUE = 3
    # all numbers lower than zero are error codes
    ERROR = -1
    DUPLICATE = -2
    STOP = -3
    EMPTY = -4
    NOT_FOUND = -404


class Task:
    # importance must be between 1 and 10
    min_importance:int = 1
    max_importance:int = 10

    def __init__(self, name:str, description:str, importance:int) -> None:
        # all checked in ui.py
        self.task_status = Status.NOT_COMPLETED
        self.name = name
        self.description = description
        self.importance = importance
        
    def __str__(self) -> str:
        return f" {self.name} ({self.importance}/{Task.max_importance}) [{self.task_status.name}] : \"{self.description}\"\n"

    def change_status(self) -> Status:
        if(self.task_status == Status.NOT_COMPLETED):
            self.task_status = Status.COMPLETED
        elif(self.task_status == Status.COMPLETED):
            self.task_status = Status.NOT_COMPLETED
        else:
            return Status.ERROR
        return self.task_status

    def is_complete(self) -> bool:
        #return Status.COMPLETED if self.task_status==Status.COMPLETED else Status.NOT_COMPLETED
        #return True if self.task_status==Status.COMPLETED else False
        return self.task_status==Status.COMPLETED
        
    def change_task_description(self, new_description:str) -> Status:
        if(self.description != new_description):
            self.description = new_description
            return Status.SUCCESS
        else:
            return Status.DUPLICATE

    def change_task_importance(self, new_importance:int) -> Status:  # is_int must be checked in ui.py
        if(not (Task.min_importance <=new_importance<= Task.max_importance)):  # new<1 || new>10 --> ERROR
            return Status.ERROR
        if(self.importance != new_importance):
            self.importance = new_importance
            return Status.SUCCESS
        else:
            return Status.DUPLICATE
    
    def task_to_dict(self) -> Dict[str, Union[str, int]]:
        return {
                "name": self.name,
                "description": self.description,
                "importance": self.importance,
                "task_status": self.task_status.value
                }
    

class TaskList:
    def __init__(self, name:str) -> None:
        self.list_of_tasks:List[Task] = []
        self.name = name
        
    def __str__(self) -> str:
        if(len(self.list_of_tasks)<=0):
            return f" {self.name}: (empty)\n"
        else:
            result = f" {self.name}:\n"
            for task in self.list_of_tasks:
                result+=('\t'+str(task))
            return f"{result}\n"
    
    def find_task(self, t_name:str) -> Union[Task, Status]:
        if(len(self.list_of_tasks)<=0):
            return Status.EMPTY
        for task in self.list_of_tasks:
            if(task.name == t_name):
                return task
        else:
            return Status.NOT_FOUND

    def add_task(self, task:Task) -> Status:
        if(isinstance(self.find_task(task.name), Task)):
            return Status.DUPLICATE
        self.list_of_tasks.append(task)
        return Status.SUCCESS
    
    def delete_task(self, t_name:str) -> Status:
        for i, task in enumerate(self.list_of_tasks):
            if task.name == t_name:
                del self.list_of_tasks[i]
                return Status.SUCCESS
        return Status.NOT_FOUND

    def change_task_name(self, task:Task, new_name:str) -> Status:
        if(isinstance(self.find_task(new_name), Task)):
            return Status.DUPLICATE
        if(len(new_name)<=0):
            return Status.EMPTY
        task.name = new_name
        return Status.SUCCESS
        
    def tasklist_to_dict(self) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
        #                                              |--------List of Tasks-------|
        return {
                "name": self.name,
                "list_of_tasks": [task.task_to_dict() for task in self.list_of_tasks]
                }


class ToDoManager:
    def __init__(self) -> None:
        self.list_of_tasklists:List[TaskList] = []

    def __str__(self) -> str:
        if(len(self.list_of_tasklists)<=0):
            return "\n over view :\n   (empty)\n"
        result = ""
        for tasklist in self.list_of_tasklists:
            result+=(str(tasklist))
        return f" over view :\n{result}\n"

    def find_tasklist(self, tl_name:str) -> Union[TaskList, Status]:
        if(len(self.list_of_tasklists)<=0):
            return Status.EMPTY
        for tasklist in self.list_of_tasklists:
            if(tasklist.name == tl_name):
                return tasklist
        else:
            return Status.NOT_FOUND

    def add_tasklist(self, tasklist:TaskList) -> Status:
        if(isinstance(self.find_tasklist(tasklist.name), TaskList)):
            return Status.DUPLICATE
        self.list_of_tasklists.append(tasklist)
        return Status.SUCCESS
    
    def delete_tasklist(self, tl_name:str) -> Status:
        for i, tasklist in enumerate(self.list_of_tasklists):
            if tasklist.name == tl_name:
                del self.list_of_tasklists[i]
                return Status.SUCCESS
        return Status.NOT_FOUND
    
    def change_tasklist_name(self, tasklist:TaskList, new_name:str) -> Status:
        if(isinstance(self.find_tasklist(new_name), TaskList)):
            return Status.DUPLICATE
        if(len(new_name)<=0):
            return Status.EMPTY
        tasklist.name = new_name
        return Status.SUCCESS
        
    def todo_manager_to_dict(self) -> Dict[str, List[Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]]]:
        #                                       |                         |--------List of Tasks-------| |
        #                                       |--------------------List of TaskLists-------------------|
        return {
                "list_of_tasklists": [tl.tasklist_to_dict() for tl in self.list_of_tasklists]
               }


if(__name__ == '__main__'):
    print("\nuse this file as module.\n")

#MadMad_175