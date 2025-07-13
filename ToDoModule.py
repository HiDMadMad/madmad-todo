ASCII_ART = """
 __  __           _ __  __           _ _       _____     ____
|  \\/  | __ _  __| |  \\/  | __ _  __| ( )___  |_   _|__ |  _ \\  ___
| |\\/| |/ _` |/ _` | |\\/| |/ _` |/ _` |// __|   | |/ _ \\| | | |/ _ \\
| |  | | (_| | (_| | |  | | (_| | (_| | \\__ \\   | | (_) | |_| | (_) |
|_|  |_|\\__,_|\\__,_|_|  |_|\\__,_|\\__,_| |___/   |_|\\___/|____/ \\___/


"""  # \\ are for fix the warning


if __name__ == "__main__":
    print(ASCII_ART,"use this file as a module!\n")


MESSAGES = {"first welcome":"\nwelcome to MadMad's ToDo app <3\n",
            
            "continued":"\nwhat do you want to do now?",

            "main menu":"\n1.create a task list\n2.show task lists\n3.open a task list\n4.delete task list\
                         \n5.import from CSV\n6.export as CSV\n7.exit\n",

            "task list menu":"\n1.add task\n2.show tasks\n3.show task details\n4.delete task\n5.import from CSV\n6.export as CSV\
                              \n7.return to main menu\n8.exit",

            "add task list":"\nyour task list was added successfully!",
            "delete task list":"\nyour task list was deleted successfully!",
            "task lists import":"\nyour task lists was imported successfully!",
            "task lists export":"\nyour task lists was exported successfully!",

            "task list name input":"\nenter name of task list :\n>> ",
            "task list id input":"\nenter id of task list :\n>> ",

            "add task":"\nyour task was added successfully!",
            "delete task":"\nyour task was deleted successfully!",
            "import tasks":"\nyour tasks was imoprted successfully!",
            "export tasks":"\nyour tasks was exported successfully!",

            "task name input":"\nenter name of task :\n>> ",
            "task id input":"\nenter id of task :\n>> ",

            "wrong input":"your input means you are a failure =)\ngo to your room and think about your bad works :)"}



#================ classes ================#

class Task():
    id_counter = 0
    def __init__(self, name:str, description:str, importance:int):
        self.name = name
        self.description = description
        self.importance = importance
        Task.id_counter += 1
        self.id = Task.id_counter

    def __str__(self):
        return f"{self.id}. {self.name} : {self.description} ({self.importance})\n\n"

class TaskList():
    task_lists = []
    id_counter = 0
    def __init__(self):
        print(ASCII_ART, MESSAGES["first welcome"])

    def add_task_list(self):
        self.name = input(MESSAGES["task list name input"])

    def delete_task_list_by_name(self, task_list_name):
        pass

    def delete_task_list_by_id(self, task_list_id):
        pass

    def show_task_lists(self):
        pass

    def add_task(self):
        pass

    def delete_task_by_name(self, task_name):
        pass

    def delete_task_by_id(self, task_id):
        pass

    def show_tasks(self):
        pass

    def save_as_csv(self):
        pass

    def import_from_csv(self):
        pass



#================ functions ================#

def show_menu():
    pass

def get_task_values(task_list):
    user_request = input(">> ")
    match(user_request):
        case '1'|'add task':
            task_list.add_task()
        case '2'|'delete task':
            task_list.delete_task()
        case '3'|'save tasks as csv':
            task_list.save_as_csv()
        case '4'|'import tasks from csv':
            task_list.import_from_csv()
        case _:
            print(MESSAGES["wrong input"])
#MadMad_116