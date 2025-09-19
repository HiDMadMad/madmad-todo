from messages import MESSAGES as msg
from messages import ASCII_ART, PROGRESS
from models import *
import os 
import platform
from typing import Callable



# constants :
USER_PLATFORM = platform.system()
USER_NAME = os.getlogin()



# OS functions :
def clear_command_line():
    if(USER_PLATFORM == 'Windows'):
        os.system("cls")
        return Status.SUCCESS
    elif(USER_PLATFORM == 'Linux' or USER_PLATFORM == 'Darwin'):
        os.system("clear")
        return Status.SUCCESS
    return Status.ERROR



# app lifecycle functions :
def app_starter():
    clear_command_line()
    print(ASCII_ART, msg["first welcome"].format(USER_NAME))

def do_and_refresh_main_menu(func:Callable):
    clear_command_line()
    print(ASCII_ART)
    func()
    display_main_menu()



# user interaction functions :
def display_returned_message(error_message:str, *vars_in_err_msg):  # var_in_err_msg:any = None
    if(vars_in_err_msg):  # if(var_in_err_msg is not None)
        print(error_message.format(*vars_in_err_msg))
    else:
        print(error_message)

def want_to_continue(continue_or_not_message:str):
    while(True):
        want_to_continue_input = input(continue_or_not_message).strip().upper()
        if(want_to_continue_input in PROGRESS["ALL"]):  # for fun
            if(want_to_continue_input in PROGRESS["STOP"]):  # many ways to write lines 32&33
                return Status.STOP
            else:  # if PROGRESS has more keys it must be changed
                return Status.CONTINUE
        else:
            print(msg["wrong input"])



# menu operations functions :
def display_main_menu():
    print(msg["main menu"])

def display_task_list_menu():
    print(msg["task list menu"])

def display_task_menu():
    print(msg["task menu"])

def create_tl(td_manager:ToDoManager):
    while(True):
        tl_name = input(msg["tl name input"])
        if(td_manager.add_task_list(TaskList(tl_name)) == Status.SUCCESS):
            display_returned_message(msg["tl added"], tl_name)
            print(td_manager)
            return Status.SUCCESS
        else:
            display_returned_message(msg["tl duplicated"], tl_name)
            if(want_to_continue(msg["tl name input again"]) == Status.STOP):
                return Status.DUPLICATE

def display_task_lists(td_manager:ToDoManager):
    print(td_manager)

def open_tl(td_manager:ToDoManager):
    while(True):
        tl_name = input(msg["tl name input"])
        if(isinstance(td_manager.find_task_list(tl_name), int)):
            print(ASCII_ART,tl_name)
            display_task_list_menu()
            return Status.SUCCESS
        else:
            display_returned_message(msg["tl not found"], tl_name)
            if(want_to_continue(msg["tl name input again"]) == Status.STOP):
                return Status.NOT_FOUND

def delete_tl(td_manager:ToDoManager):
    while(True):
        tl_name = input(msg["tl name input"])
        if(td_manager.delete_task_list(tl_name) == Status.SUCCESS):
            display_returned_message(msg['tl deleted'], tl_name)
            return Status.SUCCESS
        else:
            display_returned_message(msg["tl not found"], tl_name)
            if(want_to_continue(msg["tl name input again"]) == Status.STOP):
                return Status.NOT_FOUND

#MadMad_109