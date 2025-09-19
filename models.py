from enum import Enum
class Status(Enum):
    NOT_COMPLETED = 0  # False
    COMPLETED = 1  # True
    SUCCESS = 2
    CONTINUE = 3
    # all numbers lower than zero are error codes
    ERROR = -1
    DUPLICATE = -2
    EMPTY = -3
    STOP = -4
    NOT_FOUND = -404


class Task():
    task_id_counter = 0

    # importance must be between 1 and 10
    min_importance = 1
    max_importance = 10

    def __init__(self, name:str, description:str, importance:int):
        self.task_status = Status.NOT_COMPLETED
        self.name = name
        self.description = description
        self.importance = importance  # must be checked in app.py or ui.py (int, 1<imp<=10)
        Task.task_id_counter += 1
        self.id = Task.task_id_counter
        
    def __str__(self):
        return f"{self.id}. {self.name} ({self.importance}/{Task.max_importance}) [{self.task_status.name}] : {self.description}\n"

    def change_status(self):
        if(self.task_status == Status.NOT_COMPLETED):
            self.task_status = Status.COMPLETED
        else:
            self.task_status = Status.NOT_COMPLETED
        return self.task_status

    def is_complete(self):
        #return Status.COMPLETED if self.task_status==Status.COMPLETED else Status.NOT_COMPLETED
        return True if self.task_status==Status.COMPLETED else False
    
    def change_name(self, new_name:str):  # must be checked in app.py or ui.py (str)
        if(self.name != new_name):
            self.name = new_name
            return Status.SUCCESS
        elif(self.name == new_name):
            return Status.DUPLICATE
        return Status.ERROR

    def change_description(self, new_description:str):  # must be checked in app.py or ui.py (str)
        if(self.description != new_description):
            self.description = new_description
            return Status.SUCCESS
        elif(self.description == new_description):
            return Status.DUPLICATE
        return Status.ERROR

    def change_importance(self, new_importance:int):
        if(not (Task.min_importance <=new_importance<= Task.max_importance)):  # new<1 && new>10 --> ERROR
            return Status.ERROR
        if(self.importance != new_importance):
            self.importance = new_importance
            return Status.SUCCESS
        elif(self.importance == new_importance):
            return Status.DUPLICATE
        return Status.ERROR


class TaskList():
    task_list_id_counter = 0
    def __init__(self, name:str):
        self.list_of_tasks = []
        self.name = name
        TaskList.task_list_id_counter+=1
        self.id = TaskList.task_list_id_counter
    
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
            return Status.EMPTY
        # for i in range(len(self.list_of_tasks)):
        #     if(self.list_of_tasks[i].name == t_name):
        #         return i
        for index, task in enumerate(self.list_of_tasks):
            if(task.name == t_name):
                return index
        else:
            return Status.NOT_FOUND

    def find_by_id_in_tl(self, t_id:any):
        if(len(self.list_of_tasks)<=0):
            return Status.EMPTY
        for index, task in enumerate(self.list_of_tasks):
            if(task.id == t_id):
                return index
        else:
            return Status.NOT_FOUND
        # if a non-integer is entered instead of the ID, it raises an error
        # it's will be checked in ui.py or app.py

    def add_task(self, task:Task):
        result = self.find_by_name_in_tl(task.name)
        if(not isinstance(result, Status)):  # type(result)!=Status --> result==index_of_a_task
            return Status.DUPLICATE
        self.list_of_tasks.append(task)
        return Status.SUCCESS
    
    def delete_task_by_id(self, t_id:any):
        result = self.find_by_id_in_tl(t_id) 
        if(not isinstance(result, Status)):
            del self.list_of_tasks[result]  # result is index --> so function is found it --> so it deletes it
            return Status.SUCCESS
        return Status.NOT_FOUND
    
    def delete_task_by_name(self, t_name:str):
        result = self.find_by_name_in_tl(t_name) 
        if(not isinstance(result, Status)):
            del self.list_of_tasks[result]
            return Status.SUCCESS
        return Status.NOT_FOUND
    
        
class ToDoManager():
    def __init__(self):
        self.list_of_task_lists = []

    def __str__(self):
        if(len(self.list_of_task_lists)<=0):
            return "\nover view :\n   (empty)\n"
        result = ""
        for task_list in self.list_of_task_lists:
            result+=('   '+str(task_list))
        return f"\nover view :\n{result}\n"

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

#MadMad_168