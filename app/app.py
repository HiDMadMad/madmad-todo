import models as tm  # tm : todo-models
import ui
from messages import MESSAGES as msg

def app():
    ToDo = tm.ToDoManager()
    ui.load_data(ToDo)

    if(ui.app_starter() == tm.Status.ERROR):
        return tm.Status.ERROR
    
    AUTO_SAVE = True
    ui.display_main_menu(AUTO_SAVE)

    main_user_request = ""
    tl_user_request = ""
    exit_from_tl_menu = False
    exit_from_t_menu = False
    return_to_main_from_t = False

    while(True):
        if(exit_from_tl_menu == True):
            exit_from_tl_menu = False
            break
        main_user_request = input(" >> ")
        match(main_user_request):
            case '0'|'change auto save':
                AUTO_SAVE = not AUTO_SAVE
                ui.do_and_refresh_menu(ui.nothing, lambda:ui.display_main_menu(AUTO_SAVE))
            case '1'|'create task list':
                ui.do_and_refresh_menu(lambda:ui.create_tl(ToDo), lambda:ui.display_main_menu(AUTO_SAVE))
                if(AUTO_SAVE):
                    ui.save_data(ToDo)
            case '2'|'display task lists':
                ui.do_and_refresh_menu(lambda:ui.display_tasklists(ToDo), lambda:ui.display_main_menu(AUTO_SAVE))
            case '3'|'open task list':
                #opened_tl = ui.do_and_refresh_menu(lambda:ui.open_tl(ToDo), ui.display_tl_menu)
                # in the line above, if the function doesn’t return a tl and goes back to the main-menu, it still shows the tl-menu
                ui.refresh_only()
                tl_is_open = ui.open_tl(ToDo)
                if(isinstance(tl_is_open, tm.TaskList)):
                    ui.display_tl_menu()
                    while(True):
                        if(exit_from_t_menu == True):
                            exit_from_t_menu = False
                            exit_from_tl_menu = True
                            break
                        if(return_to_main_from_t == True):
                            return_to_main_from_t = False
                            break
                        tl_user_request = input(" >> ")
                        match(tl_user_request):
                            case '1'|'add task':
                                ui.do_and_refresh_menu(lambda:ui.create_t(tl_is_open), ui.display_tl_menu)
                                if(AUTO_SAVE):
                                    ui.save_data(ToDo)
                            case '2'|'display tasks':
                                ui.do_and_refresh_menu(lambda:ui.display_tasks(tl_is_open), ui.display_tl_menu)
                            case '3'|'select task':
                                ui.refresh_only()
                                t_is_open = ui.open_t(tl_is_open)
                                if(isinstance(t_is_open, tm.Task)):
                                    ui.display_t_menu()
                                    while(True):
                                        t_user_request = input(" >> ")
                                        match(t_user_request):
                                            case '1'|'change task status':
                                                ui.do_and_refresh_menu(lambda:ui.change_t_status(t_is_open), ui.display_t_menu, t_is_open)
                                                if(AUTO_SAVE):
                                                    ui.save_data(ToDo)
                                            case '2'|'change task name':
                                                ui.do_and_refresh_menu(lambda:ui.change_t_name(tl_is_open, t_is_open), ui.display_t_menu, t_is_open)
                                                if(AUTO_SAVE):
                                                    ui.save_data(ToDo)
                                            case '3'|'change task description':
                                                ui.do_and_refresh_menu(lambda:ui.change_t_desc(t_is_open), ui.display_t_menu, t_is_open)
                                                if(AUTO_SAVE):
                                                    ui.save_data(ToDo)
                                            case '4'|'change task importance':
                                                ui.do_and_refresh_menu(lambda:ui.change_t_imp(t_is_open), ui.display_t_menu, t_is_open)
                                                if(AUTO_SAVE):
                                                    ui.save_data(ToDo)
                                            case '5'|'return to task list menu':
                                                ui.do_and_refresh_menu(ui.nothing, ui.display_tl_menu)
                                                break
                                            case '6'|'return to main menu':
                                                ui.do_and_refresh_menu(ui.nothing, lambda:ui.display_main_menu(AUTO_SAVE))
                                                return_to_main_from_t = True
                                                break
                                            case '7'|'save and exit':
                                                ui.save_data(ToDo)
                                                exit_from_t_menu = True
                                                break
                                            case _:
                                                print(msg["wrong input"])
                                else:
                                    ui.display_tl_menu()
                            case '4'|'delete task'  :
                                ui.do_and_refresh_menu(lambda:ui.delete_t(tl_is_open), ui.display_tl_menu)
                                if(AUTO_SAVE):
                                    ui.save_data(ToDo)
                            case '5'|'return to main menu':
                                ui.do_and_refresh_menu(ui.nothing, lambda:ui.display_main_menu(AUTO_SAVE))
                                break
                            case '6'|'save and exit':
                                ui.save_data(ToDo)
                                exit_from_tl_menu = True
                                break
                            case _:
                                print(msg["wrong input"])
                else:
                    ui.display_main_menu(AUTO_SAVE)
            case '4'|'delete task list':
                ui.do_and_refresh_menu(lambda:ui.delete_tl(ToDo), lambda:ui.display_main_menu(AUTO_SAVE))
                if(AUTO_SAVE):
                    ui.save_data(ToDo)
            case '5'|'export as Excel':
                ui.do_and_refresh_menu(lambda:ui.export_to_excel(ToDo), lambda:ui.display_main_menu(AUTO_SAVE))
            case '6'|'export as CSV':
                ui.do_and_refresh_menu(lambda:ui.export_to_csv(ToDo), lambda:ui.display_main_menu(AUTO_SAVE))
            case '7'|'import from CSV':
                print("not ready yet!\n")
                pass
            case '8'|'save and exit':
                ui.save_data(ToDo)
                break
            case _:
                print(msg["wrong input"])


if(__name__ == '__main__'):
    app()

#MadMad_134