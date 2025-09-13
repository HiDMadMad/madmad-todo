from models import *
import unittest

class TestFullSystem(unittest.TestCase):

    def setUp(self):
        # Reset counter for consistency in testing
        Task.task_id_counter = 0

        self.task1 = Task("Task1", "Desc1", 5)
        self.task2 = Task("Task2", "Desc2", 8)
        self.task3 = Task("Task3", "Desc3", 10)
        self.task_list = TaskList("My List")
        self.manager = ToDoManager()

    # ------------------ TASK TESTS ------------------

    def test_task_initialization(self):
        self.assertEqual(self.task1.name, "Task1")
        self.assertEqual(self.task1.description, "Desc1")
        self.assertEqual(self.task1.importance, 5)
        self.assertEqual(self.task1.task_status, Status.NOT_COMPLETED)
        self.assertIsInstance(self.task1.id, int)

    def test_task_str_format(self):
        string_output = str(self.task1)
        self.assertIn("Task1", string_output)
        self.assertIn("Desc1", string_output)
        self.assertIn("NOT_COMPLETED", string_output)

    def test_task_status_toggle(self):
        self.assertEqual(self.task1.change_status(), Status.COMPLETED)
        self.assertEqual(self.task1.change_status(), Status.NOT_COMPLETED)

    def test_task_is_complete(self):
        self.task1.task_status = Status.COMPLETED
        self.assertEqual(self.task1.is_complete(), Status.COMPLETED)
        self.task1.task_status = Status.NOT_COMPLETED
        self.assertEqual(self.task1.is_complete(), Status.NOT_COMPLETED)

    def test_change_name_success(self):
        result = self.task1.change_name("NewTask1")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task1.name, "NewTask1")

    def test_change_name_duplicate(self):
        self.task1.change_name("NewName")
        result = self.task1.change_name("NewName")
        self.assertEqual(result, Status.DUPLICATE)

    def test_change_description_success(self):
        result = self.task1.change_description("New Desc")
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task1.description, "New Desc")

    def test_change_description_duplicate(self):
        self.task1.change_description("New Desc")
        result = self.task1.change_description("New Desc")
        self.assertEqual(result, Status.DUPLICATE)

    def test_change_importance_success(self):
        result = self.task1.change_importance(7)
        self.assertEqual(result, Status.SUCCESS)
        self.assertEqual(self.task1.importance, 7)

    def test_change_importance_invalid_low(self):
        result = self.task1.change_importance(0)
        self.assertEqual(result, Status.ERROR)

    def test_change_importance_invalid_high(self):
        result = self.task1.change_importance(11)
        self.assertEqual(result, Status.ERROR)

    def test_change_importance_duplicate(self):
        result = self.task1.change_importance(5)
        self.assertEqual(result, Status.DUPLICATE)

    # ------------------ TASK-LIST TESTS ------------------

    def test_task_list_str_empty(self):
        empty_list = TaskList("EmptyList")
        self.assertIn("(empty)", str(empty_list))

    def test_task_list_str_with_tasks(self):
        self.task_list.add_task(self.task1)
        self.assertIn("Task1", str(self.task_list))

    def test_add_task_success(self):
        result = self.task_list.add_task(self.task1)
        self.assertEqual(result, Status.SUCCESS)

    def test_add_task_duplicate(self):
        self.task_list.add_task(self.task1)
        duplicate = Task("Task1", "Different", 6)
        result = self.task_list.add_task(duplicate)
        self.assertEqual(result, Status.DUPLICATE)

    def test_find_by_name_existing(self):
        self.task_list.add_task(self.task1)
        idx = self.task_list.find_by_name_in_tl("Task1")
        self.assertIsInstance(idx, int)

    def test_find_by_name_not_found(self):
        self.assertEqual(self.task_list.find_by_name_in_tl("GhostTask"), Status.EMPTY)

        self.task_list.add_task(self.task1)
        self.assertEqual(self.task_list.find_by_name_in_tl("NotHere"), Status.NOT_FOUND)

    def test_find_by_id_existing(self):
        self.task_list.add_task(self.task1)
        idx = self.task_list.find_by_id_in_tl(self.task1.id)
        self.assertIsInstance(idx, int)

    def test_find_by_id_not_found(self):
        self.assertEqual(self.task_list.find_by_id_in_tl(12345), Status.EMPTY)

        self.task_list.add_task(self.task1)
        self.assertEqual(self.task_list.find_by_id_in_tl(99999), Status.NOT_FOUND)

    def test_delete_task_by_id_success(self):
        self.task_list.add_task(self.task1)
        result = self.task_list.delete_task_by_id(self.task1.id)
        self.assertEqual(result, Status.SUCCESS)

    def test_delete_task_by_id_not_found(self):
        self.task_list.add_task(self.task1)
        result = self.task_list.delete_task_by_id(9999)
        self.assertEqual(result, Status.NOT_FOUND)

    def test_delete_task_by_name_success(self):
        self.task_list.add_task(self.task1)
        result = self.task_list.delete_task_by_name("Task1")
        self.assertEqual(result, Status.SUCCESS)

    def test_delete_task_by_name_not_found(self):
        self.task_list.add_task(self.task1)
        result = self.task_list.delete_task_by_name("Ghost")
        self.assertEqual(result, Status.NOT_FOUND)

    # ------------------ TODO-MANAGER TESTS ------------------

    def test_manager_str_empty(self):
        self.assertIn("(empty)", str(self.manager))

    def test_manager_str_with_lists(self):
        self.manager.add_task_list(self.task_list)
        self.assertIn("My List", str(self.manager))

    def test_add_task_list_success(self):
        result = self.manager.add_task_list(self.task_list)
        self.assertEqual(result, Status.SUCCESS)

    def test_add_task_list_duplicate(self):
        self.manager.add_task_list(self.task_list)
        result = self.manager.add_task_list(self.task_list)
        self.assertEqual(result, Status.DUPLICATE)

    def test_find_task_list_empty(self):
        result = self.manager.find_task_list("AnyList")
        self.assertEqual(result, Status.EMPTY)

    def test_find_task_list_not_found(self):
        self.manager.add_task_list(TaskList("Work"))
        result = self.manager.find_task_list("NonExistent")
        self.assertEqual(result, Status.NOT_FOUND)

    def test_find_task_list_success(self):
        self.manager.add_task_list(TaskList("Work"))
        idx = self.manager.find_task_list("Work")
        self.assertIsInstance(idx, int)

    def test_delete_task_list_success(self):
        self.manager.add_task_list(TaskList("Work"))
        result = self.manager.delete_task_list("Work")
        self.assertEqual(result, Status.SUCCESS)

    def test_delete_task_list_not_found(self):
        result = self.manager.delete_task_list("NotHere")
        self.assertEqual(result, Status.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()