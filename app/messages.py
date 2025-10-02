ASCII_ART = """
  __  __           _ __  __           _ _       _____     ____
 |  \\/  | __ _  __| |  \\/  | __ _  __| ( )___  |_   _|__ |  _ \\  ___
 | |\\/| |/ _` |/ _` | |\\/| |/ _` |/ _` |// __|   | |/ _ \\| | | |/ _ \\
 | |  | | (_| | (_| | |  | | (_| | (_| | \\__ \\   | | (_) | |_| | (_) |
 |_|  |_|\\__,_|\\__,_|_|  |_|\\__,_|\\__,_| |___/   |_|\\___/|____/ \\___/
 ============================ 0.1.0 (MVP) ============================

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
    #-------------------------------------------MENUS--------------------------------------------
    "main menu" : "\n 0.toggle auto save (current:{})\n 1.create task list\n 2.display task lists\
                   \n 3.open task list\n 4.delete task list\n 5.export as Excel\n 6.export as CSV\
                   \n 7.import from CSV\n 8.save and exit\n ",
                   
    "task list menu" : "\n 1.add task\n 2.display tasks\n 3.select task\n 4.delete task\
                        \n 5.return to main menu\n 6.save and exit\n ",

    "task menu" : "\n 1.change task status\n 2.change task name\n 3.change task description\
                    \n 4.change task importance\n 5.return to task list menu\
                    \n 6.return to main menu\n 7.save and exit\n ",

    "wrong input" : " your input means you are a failure =)\
                     \n go to your room and think about your mistakes :)\n\n",
    #-------------------------------------TASK LIST INPUTS---------------------------------------
    "tl name input" : "\n enter the name of task list :\n >> ",
    "tl name input again" : " do you want to enter name again?(y/n): ",
    "tl delete confirm" : " you are about to delete \"{}\". are you sure? this can not be undone(y/n): ",
    "tl delete cancelled" : " deletion cancelled.\n",
    #-------------------------------------TASK LIST ERRORS---------------------------------------
    "tl duplicated" : " task list \"{}\" already exists!\n",
    "tl not found" : " task list \"{}\" was not found.\n",
    "tl empty" : " task list was empty. go and add some tasks to it!\n",
    #-------------------------------------TASK LIST OUTPUTS--------------------------------------
    "tl added" : " task list \"{}\" was added successfully!\n",
    "tl deleted" : " task list \"{}\" was deleted successfully!\n",
    "tl imported" : " your task lists were imported successfully!\n",
    "tl exported" : " your task lists were exported successfully!\n",
    #-------------------------------------TASK INPUTS--------------------------------------------
    "t name input" : "\n enter name of task :\n >> ",
    "t new name input" : "\n enter new name of task :\n >> ",
    "t name input again" : " do you want to enter name again?(y/n): ",
    "t desc input" : "\n enter description for \"{}\" :\n >> ",
    "t new desc input" : "\n enter new description of task :\n >> ",
    "t desc input again" : " do you want to enter description again?(y/n): ",
    "t imp input" : "\n enter importance of \"{}\" :\n >> ",
    "t new imp input" : "\n enter new importance of task :\n >> ",
    "t imp input again" : " do you want to enter importance again?(y/n): ",
    "t delete confirm" : "\n you are about to delete \"{}\".\n are you sure? this can not be undone(y/n): ",
    #-------------------------------------TASK OUTPUTS-------------------------------------------
    "t added" : " task \"{}\" was added successfully!\n",
    "t deleted" : " task \"{}\" was deleted successfully!\n",
    "t delete cancelled" : " deletion cancelled.\n",
    "t status changed" : " status of \"{}\" changed to \"{}\".\n",
    "t name changed" : " renamed to \"{}\" successfully!\n",
    "t desc changed" : " task \"{}\" description changed successfully!\n",
    "t imp changed" : " task \"{}\" importance changed successfully!\n",
    "t imported" : " your tasks were imported successfully!\n",
    "t exported" : " your tasks were exported successfully!\n",
    #-------------------------------------TASK ERRORS--------------------------------------------
    "t duplicated" : " task \"{}\" already exists!\n",
    "t not found" : " task \"{}\" was not found.\n",
    "t name duplicated" : " task name is already \"{}\"!\n",
    "t name empty" : " name can not be empty\n",
    "t desc duplicated" : " task with this dicription already exists!\n",
    "t imp duplicated" : " task already have that importance!\n",
    "t wrong imp" : " wrong importance value. importance must be an integer between 1 and 10.\n",
    "t imp not int" : " wrong importance value. importance must be an integer\n",
    "t imp out of range" : " wrong importance value. importance must be between 1 and 10.\n",
    "t status not change" : " have a problem with status of \"{}\"\n",
    #-------------------------------------DATA INPUTS--------------------------------------------
    "export to excel path input" : "\n enter the path (\\path) :\n >>",
    "export to excel name input" : "\n enter the path (file_name.xls) :\n >>",
    "export to csv path input" : "\n enter the path (\\path) :\n >>",
    "export to csv name input" : "\n enter the file name (file_name.csv) :\n >>",
    "export input again" : " do you want enter path again?(y/n): ",
    "export to default path" : " do you want to export to default path?(y/n): ",
    "import csv path input" : "\n enter CSV file path (\\path) :\n >>",
    #-------------------------------------DATA OUTPUTS-------------------------------------------
    "excel exported" : " excel file exported to \"{}\" named \"{}\" successfully!\n",
    "csv exported" : " csv file exported to \"{}\" named \"{}\" successfully!\n",
    "data saved" : " data saved successfully!\n",
    "backup created" : " backup created successfully.\n",
    #-------------------------------------DATA ERRORS--------------------------------------------
    "wrong path" : " the path you entered does not exists!\n",
    "import csv not found" : " file not found!\n",
    "import csv error" : " error importing CSV : {}\n",
    "save error" : " error saving data : {}\n",
    "backup warning" : " warning: could not create backup : {}\n",
    "load warning importance" : " warning: invalid importance {} for task {}, setting to 5\n",
    "load warning status" : " warning: invalid status {} for task {}, setting to NOT_COMPLETED\n",
    "can not load data" : " we can not load data from \"{}\".\n check that file and make sure its contents are correct.\n",
    "data not found" : " no saved data found. starting fresh.\n",
    #-----------------------------------ANOTHER OUTPUTS------------------------------------------
    "opening menu" : " opening menu :",
    "deleting menu" : " deleting menu :",
    #-----------------------------------ANOTHER ERRORS-------------------------------------------
    "not sup os" : " OS \"{}\" is not supported.\n",
    "empty dir" : " your directory is empty from task list!\n",
    "unk error":" unknown error!\n"
}


if(__name__ == '__main__'):
    print("\n use this file as module.\n")

#MadMad_121