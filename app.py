import models as tm  # tm : todo-models
import ui
from messages import MESSAGES as msg

ToDo = tm.ToDoManager()

ui.app_starter()
ui.display_main_menu()

main_user_request = ""
tl_user_request = ""

while(True):
    main_user_request = input(">> ")
    match(main_user_request):
        case '1'|'create task list':
            ui.do_and_refresh_menu(lambda:ui.create_tl(ToDo), ui.display_main_menu)
        case '2'|'display task lists':
            ui.do_and_refresh_menu(lambda:ui.display_task_lists(ToDo), ui.display_main_menu)
        case '3'|'open task list':
            opened_tl = ui.do_and_refresh_menu(lambda:ui.open_tl(ToDo), ui.display_tl_menu)
            while(True):
                tl_user_request = input(">> ")
                match(tl_user_request):
                    case '1'|'add task':
                        ui.do_and_refresh_menu(lambda:ui.create_t(opened_tl), ui.display_tl_menu)
                    case '2'|'display tasks':
                        pass
                    case '3','select task':
                        pass
                    case '4'|'delete task'  :
                        ui.do_and_refresh_menu(lambda:ui.delete_t(opened_tl), ui.display_tl_menu)
                    case '5'|'export tasks as Excel':
                        pass
                    case '6'|'export tasks as CSV':
                        pass
                    case '7'|'import tasks from CSV':
                        pass
                    case '8'|'return to main menu':
                        ui.do_and_refresh_menu(ui.nothing, ui.display_main_menu)
                        break
                    case '9'|'exit':
                        pass
                    case _:
                        print(msg["wrong input"])
        case '4'|'delete task list':
            ui.do_and_refresh_menu(lambda:ui.delete_tl(ToDo), ui.display_main_menu)
        case '5'|'export as Excel':
            pass
        case '6'|'export as CSV':
            pass
        case '7'|'import from CSV':
            pass
        case '8'|'exit':
            break
        case _:
            print(msg["wrong input"])

#MadMad_59

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

#MadMad_80