import unittest
import os
from day1._2generation.exercise3_todo_list import TodoList

class TestTodoListApplication(unittest.TestCase):
    def setUp(self):
        self.todo_file = 'data/todo_list.txt'
        if os.path.exists(self.todo_file):
            os.remove(self.todo_file)
        self.todo_list = TodoList(self.todo_file)

    def test_add_task(self):
        self.todo_list.add_task('Task 1')
        self.todo_list.add_task('Task 2')
        tasks = self.todo_list.get_tasks()
        self.assertEqual(tasks, ['Task 1', 'Task 2'])

    def test_persistence(self):
        self.todo_list.add_task('Task 1')
        # Reload todo list from file
        new_todo_list = TodoList(self.todo_file)
        tasks = new_todo_list.get_tasks()
        self.assertEqual(tasks, ['Task 1'])

    def tearDown(self):
        if os.path.exists(self.todo_file):
            os.remove(self.todo_file)

if __name__ == '__main__':
    unittest.main()
