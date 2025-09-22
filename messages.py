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
    "first welcome" : "hi {}, welcome to MadMad's ToDo app!\n",
    "continued" : "\nwhat do you want to do now?",
    #-------------------------------------------MENUS--------------------------------------------
    "main menu" : "\n1.create task list\n2.display task lists\n3.open task list\
                   \n4.delete task list\n5.export as Excel\n6.export as CSV\n7.import from CSV\
                   \n8.exit\n",

    "task list menu" : "\n1.add task\n2.display tasks\n3.select task\n4.delete task\
                        \n5.export as Excel\n6.export as CSV\n7.import from CSV\
                        \n8.return to main menu\n9.exit\n",

    "task menu" : "\n1.change task status\n2.change task name\n3.change task description\
                    \n4.change task importance\n5.return to task list menu\
                    \n6.return to main menu\n7.exit\n",

    "wrong input" : "your input means you are a failure =)\
                     \ngo to your room and think about your mistakes :)\n\n",
    #-------------------------------------TASK LIST INPUTS---------------------------------------
    "tl name input" : "\nenter the name of task list :\n>> ",
    "tl name input again" : "do you want to enter name again?(y/n) ",
    #-------------------------------------TASK LIST ERRORS---------------------------------------
    "tl duplicated" : "task list \"{}\" already exists!\n",
    "tl not found" : "task list \"{}\" was not found.\n",
    "tl empty" : "task list was empty. go and add some tasks to it!\n",
    #-------------------------------------TASK LIST OUTPUTS--------------------------------------
    "tl added" : "task list \"{}\" was added successfully!\n",
    "tl deleted" : "task list \"{}\" was deleted successfully!\n",
    "tl imported" : "your task lists were imported successfully!\n",
    "tl exported" : "your task lists were exported successfully!\n",
    #-------------------------------------TASK INPUTS--------------------------------------------
    "t name input" : "\nenter name of task :\n>> ",
    "t name input again" : "do you want to enter name again?(y/n) ",
    "t desc input" : "\nenter description for \"{}\" :\n>> ",
    "t imp input" : "\nenter importance of \"{}\" :\n>> ",
    "t imp input again" : "do you want to enter importance again?(y/n) ",
    #-------------------------------------TASK OUTPUTS-------------------------------------------
    "t added" : "task \"{}\" was added successfully!\n",
    "t deleted" : "task \"{}\" was deleted successfully!\n",
    "t name changed" : "renamed to \"{}\" successfully!\n",
    "t desc changed" : "task \"{}\" description changed successfully!\n",
    "t imp changed" : "task \"{}\" importance changed successfully!\n",
    "t imported" : "your tasks were imported successfully!\n",
    "t exported" : "your tasks were exported successfully!\n",
    #-------------------------------------TASK ERRORS--------------------------------------------
    "t imp not int" : "wrong importance value. importance must be an integer\n",
    "t imp out of range" : "wrong importance value. importance must be between 1 and 10.\n",
    "t duplicated" : "task \"{}\" already exists!\n",
    "t not found" : "task \"{}\" was not found.\n",
    #-----------------------------------ANOTHER ERRORS-------------------------------------------
    "not sup os" : " OS \"{}\" is not supported.",
    "empty dir" : "your directory is empty from task list!",
    "":""
}

#MadMad_78