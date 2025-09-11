from messages import *

def app_starter():
    print(ASCII_ART, MESSAGES["first welcome"])

def show_main_menu():
    print(MESSAGES["main menu"])

def what_to_do_main_menu():
    user_request = input(">> ")
    match(user_request):
        case '1'|'add task':
            pass
        case '2'|'delete task':
            pass
        case '3'|'export tasks as csv':
            pass
        case '4'|'import tasks from csv':
            pass
        case _:
            print(MESSAGES["wrong input"])

def show_task_list_menu():
    print(MESSAGES["task list menu"])

#MadMad_26