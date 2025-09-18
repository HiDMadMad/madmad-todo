ASCII_ART = """
 __  __           _ __  __           _ _       _____     ____
|  \\/  | __ _  __| |  \\/  | __ _  __| ( )___  |_   _|__ |  _ \\  ___
| |\\/| |/ _` |/ _` | |\\/| |/ _` |/ _` |// __|   | |/ _ \\| | | |/ _ \\
| |  | | (_| | (_| | |  | | (_| | (_| | \\__ \\   | | (_) | |_| | (_) |
|_|  |_|\\__,_|\\__,_|_|  |_|\\__,_|\\__,_| |___/   |_|\\___/|____/ \\___/


"""  # \\ are for fix the warning


if __name__ == "__main__":
    print(ASCII_ART,"use this file as a module!\n")


PROGRESS = {
    "ALL" : ["Y","YES","CONTINUE","GO","OK","SURE","N","NO","STOP","QUIT","EXIT","NOT CONTINUE"],
    "CONTINUE": ["Y", "YES", "CONTINUE", "GO", "OK", "SURE"],
    "STOP": ["N", "NO", "STOP", "QUIT", "EXIT", "NOT CONTINUE"]
}


MESSAGES = {
    "first welcome" : "welcome to MadMad's ToDo app!\n",
    "continued" : "\nwhat do you want to do now?",
    #-------------------------------------------MENUS--------------------------------------------
    "main menu" : "\n1.create task list\n2.show task lists\n3.open task list\
                   \n4.delete task list\n5.export as Excel\n6.export as CSV\n7.import from CSV\
                   \n8.exit\n",

    "task list menu" : "\n1.add task\n2.select task\n3.delete task\n4.export as Excel\
                        \n5.export as CSV\n6.import from CSV\n7.return to main menu\n8.exit\n",

    "task menu" : "\n1.change task status\n2.change task name\n3.change task description\
                    \n4.change task importance\n5.return to task list menu\
                    \n6.return to main menu\n7.exit\n",

    "wrong input" : "your input means you are a failure =)\
                     \ngo to your room and think about your mistakes :)\n\n",
    #-------------------------------------TASK LIST INPUTS---------------------------------------
    "tl name input" : "\nenter the name of task list :\n>> ",
    "tl name input again" : "do you want to enter name again?(Y/N) ",
    #-------------------------------------TASK LIST ERRORS---------------------------------------
    "tl duplicated" : "task list name you input already exists! enter another one.\n",
    "tl not found" : "task list {} was not found.\n",  # .format()
    #-------------------------------------TASK LIST OUTPUTS--------------------------------------
    "tl added" : "your task list was added successfully!\n",
    "tl deleted" : "your task list was deleted successfully!\n",
    "tl imported" : "your task lists were imported successfully!\n",
    "tl exported" : "your task lists were exported successfully!\n",
#✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔
#MadMad_52

    #---------------------------------------TASKS INPUTS-----------------------------------------
    "task name input" : "\nenter name of task :\n>> ",
    "task id input" : "\nenter id of task :\n>> ",
    #---------------------------------------TASKS OUTPUTS----------------------------------------
    "add task" : "your task was added successfully!\n",
    "delete task" : "your task was deleted successfully!\n",
    "import tasks" : "your tasks were imported successfully!\n",
    "export tasks" : "your tasks were exported successfully!\n",
    #-----------------------------------------ERRORS---------------------------------------------
    "wrong importance" : "wrong importance value. importance must be an integer between 1 and 10.\n",
    "empty task list" : "list was empty. go and add some tasks to it!\n",
    "empty directory" : "your directory is empty from task list!",
    "task not found" : "task \"{}\" was not found.\n",  # .format()
    "task list not found" : "task list \"{}\" was not found.\n",  # .format()
    "duplicate task" : "task with name \"{}\" already exists!\n",  # .format()
    "duplicate task list" : "task list with name \"{}\" already exists!\n",  # .format()
    #-----------------------------------------WARNINGS-------------------------------------------
    "importance warning" : "importance must be an integer between 1 to 10",
    "":""
}

#MadMad_75