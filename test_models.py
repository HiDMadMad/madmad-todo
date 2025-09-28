import unittest
from models import *

class TestStatus(unittest.TestCase):
    """Testing Status Enum"""
    
    def test_all_status_values(self):
        """Test all Status enum values are correct"""
        self.assertEqual(Status.NOT_COMPLETED.value, 0)
        self.assertEqual(Status.COMPLETED.value, 1)
        self.assertEqual(Status.SUCCESS.value, 2)
        self.assertEqual(Status.CONTINUE.value, 3)
        self.assertEqual(Status.ERROR.value, -1)
        self.assertEqual(Status.DUPLICATE.value, -2)
        self.assertEqual(Status.STOP.value, -3)
        self.assertEqual(Status.EMPTY.value, -4)
        self.assertEqual(Status.NOT_FOUND.value, -404)

class TestTask(unittest.TestCase):
    """Testing Task class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.task = Task("Test Task", "Test description", 5)
    
    def test_task_initialization(self):
        """Test Task creation"""
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.description, "Test description")
        self.assertEqual(self.task.importance, 5)
        self.assertEqual(self.task.task_status, Status.NOT_COMPLETED)
    
    def test_task_str_representation(self):
        """Test Task string representation"""
        expected = "Test Task (5/10) [NOT_COMPLETED] : \"Test description\"\n"
        self.assertEqual(str(self.task), expected)
    
    def test_change_status_toggle(self):
        """Test status change toggle"""
        # NOT_COMPLETED -> COMPLETED
        result = self.task.change_status()
        self.assertEqual(result, Status.COMPLETED)
        self.assertEqual(self.task.task_status, Status.COMPLETED)
        
        # COMPLETED -> NOT_COMPLETED
        result = self.task.change_status()
        self.assertEqual(result, Status.NOT_COMPLETED)
        self.assertEqual(self.task.task_status, Status.NOT_COMPLETED)
    
    def test_change_status_error(self):
        """Test change_status with invalid status"""
        self.task.task_status = Status.SUCCESS
        result = self.task.change_status()
        self.assertEqual(result, Status.ERROR)
        self.assertEqual(self.task.task_status, Status.SUCCESS)  # Unchanged
    
    def test_is_complete(self):
        """Test is_complete method"""
        self.assertFalse(self.task.is_complete())
        
        self.task.task_status = Status.COMPLETED
        self.assertTrue(self.task.is_complete())
    
    def test_change_description_success(self):
        """Test successful description change"""
        result = self.task.change_task_description("New description")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task.description, "New description")
    
    def test_change_description_duplicate(self):
        """Test changing to same description"""
        result = self.task.change_task_description("Test description")
        self.assertEqual(result, Status.DUPLICATE)
    
    def test_change_description_empty_allowed(self):
        """Test changing to empty description is allowed"""
        result = self.task.change_task_description("")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task.description, "")
    
    def test_change_importance_success(self):
        """Test successful importance change"""
        result = self.task.change_task_importance(8)
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task.importance, 8)
    
    def test_change_importance_duplicate(self):
        """Test changing to same importance"""
        result = self.task.change_task_importance(5)
        self.assertEqual(result, Status.DUPLICATE)
    
    def test_change_importance_invalid(self):
        """Test invalid importance values"""
        # Below minimum
        result = self.task.change_task_importance(0)
        self.assertEqual(result, Status.ERROR)
        self.assertEqual(self.task.importance, 5)  # Unchanged
        
        # Above maximum
        result = self.task.change_task_importance(11)
        self.assertEqual(result, Status.ERROR)
        self.assertEqual(self.task.importance, 5)  # Unchanged
    
    def test_change_importance_boundary_values(self):
        """Test boundary importance values"""
        # Minimum valid
        result = self.task.change_task_importance(1)
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task.importance, 1)
        
        # Maximum valid
        result = self.task.change_task_importance(10)
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task.importance, 10)
    
    def test_task_to_dict(self):
        """Test Task to dictionary conversion"""
        expected = {
            "name": "Test Task",
            "description": "Test description",
            "importance": 5,
            "task_status": 0
        }
        result = self.task.task_to_dict()
        self.assertEqual(result, expected)
    
    def test_task_to_dict_completed(self):
        """Test Task to dictionary with COMPLETED status"""
        self.task.task_status = Status.COMPLETED
        result = self.task.task_to_dict()
        self.assertEqual(result["task_status"], 1)

class TestTaskList(unittest.TestCase):
    """Testing TaskList class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.task_list = TaskList("My Tasks")
        self.task1 = Task("Task 1", "First task", 3)
        self.task2 = Task("Task 2", "Second task", 7)
    
    def test_tasklist_initialization(self):
        """Test TaskList creation"""
        self.assertEqual(self.task_list.name, "My Tasks")
        self.assertEqual(len(self.task_list.list_of_tasks), 0)
    
    def test_tasklist_str_empty(self):
        """Test string representation of empty TaskList"""
        expected = "My Tasks: (empty)\n"
        self.assertEqual(str(self.task_list), expected)
    
    def test_tasklist_str_with_tasks(self):
        """Test string representation with tasks"""
        self.task_list.add_task(self.task1)
        result = str(self.task_list)
        self.assertIn("My Tasks:", result)
        self.assertIn("Task 1", result)
        self.assertTrue(result.endswith("\n"))
    
    def test_find_task_empty_list(self):
        """Test finding task in empty list"""
        result = self.task_list.find_task("Task 1")
        self.assertEqual(result, Status.EMPTY)
    
    def test_find_task_found(self):
        """Test finding existing task"""
        self.task_list.add_task(self.task1)
        result = self.task_list.find_task("Task 1")
        self.assertIsInstance(result, Task)
        self.assertEqual(result, self.task1)
    
    def test_find_task_not_found(self):
        """Test finding non-existing task"""
        self.task_list.add_task(self.task1)
        result = self.task_list.find_task("Nonexistent")
        self.assertEqual(result, Status.NOT_FOUND)
    
    def test_add_task_success(self):
        """Test successful task addition"""
        result = self.task_list.add_task(self.task1)
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(len(self.task_list.list_of_tasks), 1)
        self.assertEqual(self.task_list.list_of_tasks[0], self.task1)
    
    def test_add_task_duplicate(self):
        """Test adding duplicate task"""
        self.task_list.add_task(self.task1)
        duplicate_task = Task("Task 1", "Different description", 8)
        result = self.task_list.add_task(duplicate_task)
        self.assertEqual(result, Status.DUPLICATE)
        self.assertEqual(len(self.task_list.list_of_tasks), 1)
    
    def test_delete_task_success(self):
        """Test successful task deletion"""
        self.task_list.add_task(self.task1)
        result = self.task_list.delete_task("Task 1")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(len(self.task_list.list_of_tasks), 0)
    
    def test_delete_task_not_found(self):
        """Test deleting non-existing task"""
        result = self.task_list.delete_task("Nonexistent")
        self.assertEqual(result, Status.NOT_FOUND)
    
    def test_change_task_name_success(self):
        """Test successful task name change"""
        self.task_list.add_task(self.task1)
        result = self.task_list.change_task_name(self.task1, "New Name")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task1.name, "New Name")
    
    def test_change_task_name_duplicate(self):
        """Test changing task name to existing name"""
        self.task_list.add_task(self.task1)
        self.task_list.add_task(self.task2)
        result = self.task_list.change_task_name(self.task1, "Task 2")
        self.assertEqual(result, Status.DUPLICATE)
        self.assertEqual(self.task1.name, "Task 1")  # Unchanged
    
    def test_change_task_name_empty(self):
        """Test changing task name to empty string"""
        self.task_list.add_task(self.task1)
        result = self.task_list.change_task_name(self.task1, "")
        self.assertEqual(result, Status.EMPTY)
        self.assertEqual(self.task1.name, "Task 1")  # Unchanged
    
    def test_tasklist_to_dict_empty(self):
        """Test dictionary conversion of empty TaskList"""
        expected = {
            "name": "My Tasks",
            "list_of_tasks": []
        }
        result = self.task_list.tasklist_to_dict()
        self.assertEqual(result, expected)
    
    def test_tasklist_to_dict_with_tasks(self):
        """Test dictionary conversion with tasks"""
        self.task1.task_status = Status.COMPLETED
        self.task_list.add_task(self.task1)
        self.task_list.add_task(self.task2)
        
        result = self.task_list.tasklist_to_dict()
        self.assertEqual(result["name"], "My Tasks")
        self.assertEqual(len(result["list_of_tasks"]), 2)
        self.assertEqual(result["list_of_tasks"][0]["task_status"], 1)  # COMPLETED
        self.assertEqual(result["list_of_tasks"][1]["task_status"], 0)  # NOT_COMPLETED

class TestToDoManager(unittest.TestCase):
    """Testing ToDoManager class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.manager = ToDoManager()
        self.work_list = TaskList("Work Tasks")
        self.personal_list = TaskList("Personal Tasks")
    
    def test_todomanager_initialization(self):
        """Test ToDoManager creation"""
        self.assertEqual(len(self.manager.list_of_tasklists), 0)
    
    def test_todomanager_str_empty(self):
        """Test string representation of empty ToDoManager"""
        expected = "\nover view :\n   (empty)\n"
        self.assertEqual(str(self.manager), expected)
    
    def test_todomanager_str_with_tasklists(self):
        """Test string representation with tasklists"""
        self.manager.add_tasklist(self.work_list)
        result = str(self.manager)
        self.assertIn("over view :", result)
        self.assertIn("Work Tasks", result)
    
    def test_find_tasklist_empty_manager(self):
        """Test finding tasklist in empty manager"""
        result = self.manager.find_tasklist("Any List")
        self.assertEqual(result, Status.EMPTY)
    
    def test_find_tasklist_found(self):
        """Test finding existing tasklist"""
        self.manager.add_tasklist(self.work_list)
        result = self.manager.find_tasklist("Work Tasks")
        self.assertIsInstance(result, TaskList)
        self.assertEqual(result, self.work_list)
    
    def test_find_tasklist_not_found(self):
        """Test finding non-existing tasklist"""
        self.manager.add_tasklist(self.work_list)
        result = self.manager.find_tasklist("Nonexistent")
        self.assertEqual(result, Status.NOT_FOUND)
    
    def test_add_tasklist_success(self):
        """Test successful tasklist addition"""
        result = self.manager.add_tasklist(self.work_list)
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(len(self.manager.list_of_tasklists), 1)
        self.assertEqual(self.manager.list_of_tasklists[0], self.work_list)
    
    def test_add_tasklist_duplicate(self):
        """Test adding duplicate tasklist"""
        self.manager.add_tasklist(self.work_list)
        duplicate_list = TaskList("Work Tasks")
        result = self.manager.add_tasklist(duplicate_list)
        self.assertEqual(result, Status.DUPLICATE)
        self.assertEqual(len(self.manager.list_of_tasklists), 1)
    
    def test_delete_tasklist_success(self):
        """Test successful tasklist deletion"""
        self.manager.add_tasklist(self.work_list)
        result = self.manager.delete_tasklist("Work Tasks")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(len(self.manager.list_of_tasklists), 0)
    
    def test_delete_tasklist_not_found(self):
        """Test deleting non-existing tasklist"""
        result = self.manager.delete_tasklist("Nonexistent")
        self.assertEqual(result, Status.NOT_FOUND)
    
    def test_change_tasklist_name_success(self):
        """Test successful tasklist name change"""
        self.manager.add_tasklist(self.work_list)
        result = self.manager.change_tasklist_name(self.work_list, "New Work Tasks")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.work_list.name, "New Work Tasks")
    
    def test_change_tasklist_name_duplicate(self):
        """Test changing tasklist name to existing name"""
        self.manager.add_tasklist(self.work_list)
        self.manager.add_tasklist(self.personal_list)
        result = self.manager.change_tasklist_name(self.work_list, "Personal Tasks")
        self.assertEqual(result, Status.DUPLICATE)
        self.assertEqual(self.work_list.name, "Work Tasks")  # Unchanged
    
    def test_change_tasklist_name_empty(self):
        """Test changing tasklist name to empty string"""
        self.manager.add_tasklist(self.work_list)
        result = self.manager.change_tasklist_name(self.work_list, "")
        self.assertEqual(result, Status.EMPTY)
        self.assertEqual(self.work_list.name, "Work Tasks")  # Unchanged
    
    def test_todo_manager_to_dict_empty(self):
        """Test dictionary conversion of empty ToDoManager"""
        expected = {
            "list_of_tasklists": []
        }
        result = self.manager.todo_manager_to_dict()
        self.assertEqual(result, expected)
    
    def test_todo_manager_to_dict_with_tasklists(self):
        """Test dictionary conversion with tasklists"""
        self.manager.add_tasklist(self.work_list)
        self.manager.add_tasklist(self.personal_list)
        
        result = self.manager.todo_manager_to_dict()
        self.assertEqual(len(result["list_of_tasklists"]), 2)
        self.assertEqual(result["list_of_tasklists"][0]["name"], "Work Tasks")
        self.assertEqual(result["list_of_tasklists"][1]["name"], "Personal Tasks")

class TestIntegrationScenarios(unittest.TestCase):
    """Testing integration scenarios"""
    
    def setUp(self):
        """Set up complex test scenario"""
        self.manager = ToDoManager()
        self.work_list = TaskList("Work")
        self.work_task1 = Task("Meeting", "Daily standup", 8)
        self.work_task2 = Task("Code Review", "Review PR", 6)
    
    def test_complete_workflow(self):
        """Test complete workflow"""
        # Add tasklist and tasks
        self.assertEqual(self.manager.add_tasklist(self.work_list), Status.SUCCESS)
        self.assertEqual(self.work_list.add_task(self.work_task1), Status.SUCCESS)
        self.assertEqual(self.work_list.add_task(self.work_task2), Status.SUCCESS)
        
        # Complete a task
        self.assertEqual(self.work_task1.change_status(), Status.COMPLETED)
        self.assertTrue(self.work_task1.is_complete())
        self.assertFalse(self.work_task2.is_complete())
        
        # Modify task properties
        self.assertEqual(self.work_task2.change_task_description("Review new PR"), Status.SUCCESS)
        self.assertEqual(self.work_task2.description, "Review new PR")
        
        # Verify final state
        self.assertEqual(len(self.manager.list_of_tasklists), 1)
        self.assertEqual(len(self.work_list.list_of_tasks), 2)
    
    def test_error_handling(self):
        """Test error handling scenarios"""
        # Setup
        self.manager.add_tasklist(self.work_list)
        self.work_list.add_task(self.work_task1)
        
        # Test duplicate operations
        self.assertEqual(self.manager.add_tasklist(self.work_list), Status.DUPLICATE)
        self.assertEqual(self.work_list.add_task(self.work_task1), Status.DUPLICATE)
        
        # Test not found operations
        self.assertEqual(self.manager.delete_tasklist("Nonexistent"), Status.NOT_FOUND)
        self.assertEqual(self.work_list.delete_task("Nonexistent"), Status.NOT_FOUND)
        
        # Test invalid operations
        self.assertEqual(self.work_task1.change_task_importance(0), Status.ERROR)
        self.assertEqual(self.work_task1.change_task_importance(11), Status.ERROR)
        
        # Test empty string operations
        self.assertEqual(self.work_list.change_task_name(self.work_task1, ""), Status.EMPTY)
        self.assertEqual(self.manager.change_tasklist_name(self.work_list, ""), Status.EMPTY)
    
    def test_complex_dictionary_conversion(self):
        """Test complex dictionary conversion"""
        # Setup complex structure
        self.manager.add_tasklist(self.work_list)
        self.work_task1.task_status = Status.COMPLETED
        self.work_list.add_task(self.work_task1)
        self.work_list.add_task(self.work_task2)
        
        # Convert to dictionary
        result = self.manager.todo_manager_to_dict()
        
        # Verify structure
        self.assertIsInstance(result, dict)
        self.assertIn("list_of_tasklists", result)
        self.assertEqual(len(result["list_of_tasklists"]), 1)
        
        work_dict = result["list_of_tasklists"][0]
        self.assertEqual(work_dict["name"], "Work")
        self.assertEqual(len(work_dict["list_of_tasks"]), 2)
        
        # Verify task statuses
        task_statuses = [task["task_status"] for task in work_dict["list_of_tasks"]]
        self.assertIn(1, task_statuses)  # COMPLETED
        self.assertIn(0, task_statuses)  # NOT_COMPLETED

class TestEdgeCases(unittest.TestCase):
    """Testing edge cases"""
    
    def test_empty_strings(self):
        """Test handling of empty strings"""
        # Empty task name and description
        empty_task = Task("", "", 5)
        self.assertEqual(empty_task.name, "")
        self.assertEqual(empty_task.description, "")
        
        # Empty tasklist name
        empty_list = TaskList("")
        self.assertEqual(empty_list.name, "")
    
    def test_special_characters(self):
        """Test handling of special characters"""
        special_task = Task("Tâsk 中文 🎯", "Déscription with émojis 🚀", 3)
        self.assertEqual(special_task.name, "Tâsk 中文 🎯")
        self.assertIn("émojis 🚀", special_task.description)
        
        special_list = TaskList("Lìst 中文 🎯")
        self.assertEqual(special_list.name, "Lìst 中文 🎯")
    
    def test_very_long_strings(self):
        """Test handling of very long strings"""
        long_name = "A" * 1000
        long_desc = "B" * 2000
        long_task = Task(long_name, long_desc, 7)
        
        self.assertEqual(len(long_task.name), 1000)
        self.assertEqual(len(long_task.description), 2000)
        self.assertEqual(long_task.name, long_name)
        self.assertEqual(long_task.description, long_desc)
    
    def test_boundary_importance_values(self):
        """Test boundary importance values"""
        # Minimum valid importance
        min_task = Task("Min Task", "Minimum importance", 1)
        self.assertEqual(min_task.importance, 1)
        
        # Maximum valid importance
        max_task = Task("Max Task", "Maximum importance", 10)
        self.assertEqual(max_task.importance, 10)

if __name__ == '__main__':
    unittest.main()