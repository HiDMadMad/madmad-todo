import models as tm  # tm : todo-models
import ui
from messages import MESSAGES as msg

ToDo = tm.ToDoManager()

ui.app_starter()
ui.display_main_menu()

user_request = ""
while(user_request != 'exit' or user_request!='8'):
    user_request = input(">> ")
    match(user_request):
        case '1'|'create task list':
            ui.do_and_refresh_main_menu(lambda:ui.create_tl(ToDo))
        case '2'|'display task lists':
            ui.do_and_refresh_main_menu(lambda:ui.display_task_lists(ToDo))
        case '3'|'open task list':
            ui.do_and_refresh_main_menu(lambda:ui.open_tl(ToDo))
        case '4'|'delete task list':
            ui.do_and_refresh_main_menu(lambda:ui.delete_tl(ToDo))
        case '5'|'export as Excel':
            pass
        case '6'|'export as CSV':
            pass
        case '7'|'import from CSV':
            pass
        # case '8'|'exit':
        #     pass
        case _:
            print(msg["wrong input"])

#MadMad_33


# # def what_to_do_tl_menu(user_request):
# match(user_request):
#     case '1'|'add task':
#         pass
#     case '2','select task':
#         pass
#     case '3'|'delete task':
#         pass
#     case '4'|'export tasks as CSV':
#         pass
#     case '5'|'import tasks from CSV':
#         pass
#     case '6'|'return to main menu':
#         pass
#     case '7'|'exit':
#         pass
#     case _:
#         print(msg["wrong input"])


# # def what_to_do_task_menu(user_request):
# match(user_request):
#     case '1'|'change task status':
#         pass
#     case '2'|'change task name':
#         pass
#     case '3'|'change task description':
#         pass
#     case '4'|'change task importance':
#         pass
#     case '5'|'return to task list menu':
#         pass
#     case '6'|'return to main menu':
#         pass
#     case '7'|'exit':
#         pass
#     case _:
#         print(msg["wrong input"])

#MadMad_75