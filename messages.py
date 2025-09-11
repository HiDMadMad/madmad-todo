ASCII_ART = """
 __  __           _ __  __           _ _       _____     ____
|  \\/  | __ _  __| |  \\/  | __ _  __| ( )___  |_   _|__ |  _ \\  ___
| |\\/| |/ _` |/ _` | |\\/| |/ _` |/ _` |// __|   | |/ _ \\| | | |/ _ \\
| |  | | (_| | (_| | |  | | (_| | (_| | \\__ \\   | | (_) | |_| | (_) |
|_|  |_|\\__,_|\\__,_|_|  |_|\\__,_|\\__,_| |___/   |_|\\___/|____/ \\___/


"""  # \\ are for fix the warning



if __name__ == "__main__":
    print(ASCII_ART,"use this file as a module!\n")



MESSAGES = {"first welcome":"welcome to MadMad's ToDo app <3\n",
            #--------------------------------------------------------------------------------------------
            "continued":"\nwhat do you want to do now?",
            #--------------------------------------------------------------------------------------------
            "main menu":"\n1.create a task list\n2.show task lists\n3.open a task list\
                         \n4.delete task list\n5.import from CSV\n6.export as CSV\n7.exit\n",
            #--------------------------------------------------------------------------------------------
            "task list menu":"\n1.add task\n2.show tasks\n3.show task details\n4.delete task\
                              \n5.import from CSV\n6.export as CSV\n7.return to main menu\n8.exit",
            #-------------------------------------TASK LISTS OUTPUTS-------------------------------------
            "add task list":"\nyour task list was added successfully!",
            "delete task list":"\nyour task list was deleted successfully!",
            "task lists import":"\nyour task lists was imported successfully!",
            "task lists export":"\nyour task lists was exported successfully!",
            #-------------------------------------TASK LISTS INPUTS--------------------------------------
            "task list name input":"\nenter name of task list :\n>> ",
            "task list id input":"\nenter id of task list :\n>> ",
            #---------------------------------------TASKS OUTPUTS----------------------------------------
            "add task":"\nyour task was added successfully!",
            "delete task":"\nyour task was deleted successfully!",
            "import tasks":"\nyour tasks was imported successfully!",
            "export tasks":"\nyour tasks was exported successfully!",
            #---------------------------------------TASKS INPUTS-----------------------------------------
            "task name input":"\nenter name of task :\n>> ",
            "task id input":"\nenter id of task :\n>> ",
            #-----------------------------------------ERRORS---------------------------------------------
            "wrong input":"your input means you are a failure =)\ngo to your room and think about your bad works :)\n\n",
            "wrong importance" : "wrong importance value. importance must be an integer between 1 and 10"}

#MadMad_47