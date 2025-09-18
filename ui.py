from messages import MESSAGES as msg
from messages import ASCII_ART, PROGRESS
from models import *
import os 
import platform

def app_starter():
    print(ASCII_ART, msg["first welcome"])


def show_main_menu():
    print(msg["main menu"])

def create_tl(td_manager:ToDoManager):
    while(True):
        tl_name = input(msg["tl name input"])
        if(td_manager.add_task_list(TaskList(tl_name)) == Status.SUCCESS):
            print(msg["tl added"], td_manager)
            return Status.SUCCESS
        else:
            print(msg["tl duplicated"])

def delete_tl(tl_manager:ToDoManager):
    while(True):
        tl_name = input(msg["tl name input"])
        if(tl_manager.delete_task_list(tl_name) == Status.SUCCESS):
            print(msg['tl deleted'])
            return Status.SUCCESS
        else:
            print(msg["tl not found"].format(tl_name))
            want_to_continue = input(msg["tl name input again"])
            if(want_to_continue.upper() in PROGRESS["ALL"]):  # for fun
                if(want_to_continue.upper() in PROGRESS["STOP"]):  # many ways to write lines 32&33
                    return Status.NOT_FOUND
            else:
                print(msg["wrong input"])
                return Status.ERROR


def show_task_list_menu():
    print(msg["task list menu"])



def show_task_menu():
    print(msg["task menu"])



def what_platform():
    return platform.system()

def clear_command_line():
    if(what_platform() == 'Windows'):
        os.system("cls")
        return Status.SUCCESS
    elif(what_platform() == 'Linux' or what_platform() == 'Darwin'):
        os.system("clear")
        return Status.SUCCESS
    return Status.ERROR

#MadMad_62