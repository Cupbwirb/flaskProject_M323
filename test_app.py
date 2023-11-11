import unittest
from app import app, tasks

class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        tasks.clear()  # Leert Aufgabenliste nach jedem Test

    def test_sort_tasks(self):
        tasks.extend([
            {'description': 'Task C', 'completed': False},
            {'description': 'Task A', 'completed': True},
            {'description': 'Task B', 'completed': False}
        ])

        response = self.app.get('/sort_tasks')

        # Assertion
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Parse JSON response
        result = response.get_json()

        sorted_tasks = result['sorted_tasks']

        # Überprüfung, ob Aufgaben korrekt sortiert
        self.assertEqual(sorted_tasks, [
            {'description': 'Task A', 'completed': True},
            {'description': 'Task B', 'completed': False},
            {'description': 'Task C', 'completed': False}
        ])

if __name__ == '__main__':
    unittest.main()
