import unittest
from tabulate import tabulate

class HistoryLogger:
    def __init__(self):
        self.history = []

    def log_request(self, request, response):
        # Додаємо новий запис в історію
        self.history.append({
            'request': request,
            'response': response
        })
    
    def display_history(self):
        # Виводимо історію у форматі таблиці
        result = ""
        for history_entry in self.history:
            result += f"Request: {history_entry['request']}\n"
            table_data = [
                [post['id'], post['userId'], post['title'], post['body'].replace('\n', ' ')]
                for post in history_entry['response']
            ]
            result += tabulate(
                table_data,
                headers=["Post ID", "User ID", "Title", "Body"],
                tablefmt="fancy_grid"
            ) + "\n"
        return result

class TestHistoryLogger(unittest.TestCase):

    def test_log_request(self):
        # Тест для методу log_request
        history_logger = HistoryLogger()
        users = [
            {'userId': 1, 'id': 1, 'title': 'Post 1', 'body': 'This is the body of post 1'}
        ]
        history_logger.log_request("Fetch Users", users)

        # Перевіряємо, чи додано 1 запис в історію
        self.assertEqual(len(history_logger.history), 1)

    def test_display_history(self):
        # Тест для методу display_history
        history_logger = HistoryLogger()
        users = [
            {'userId': 1, 'id': 1, 'title': 'Post 1', 'body': 'This is the body of post 1'}
        ]
        history_logger.log_request("Fetch Users", users)
        
        # Перевіряємо, чи коректно відображається історія
        expected_output = (
            "Request: Fetch Users\n"
            + tabulate([[1, 1, 'Post 1', 'This is the body of post 1']], headers=["Post ID", "User ID", "Title", "Body"], tablefmt="fancy_grid") + "\n"
        )
        self.assertEqual(history_logger.display_history(), expected_output)

    def test_multiple_log_requests(self):
        # Тест для декількох запитів
        history_logger = HistoryLogger()
        users1 = [
            {'userId': 1, 'id': 1, 'title': 'Post 1', 'body': 'This is the body of post 1'}
        ]
        users2 = [
            {'userId': 2, 'id': 2, 'title': 'Post 2', 'body': 'This is the body of post 2'}
        ]
        
        history_logger.log_request("Fetch Users", users1)
        history_logger.log_request("Fetch Posts", users2)

        # Перевіряємо, чи зберігаються 2 записи в історії
        self.assertEqual(len(history_logger.history), 2)

    def test_empty_history(self):
        # Тест для порожньої історії
        history_logger = HistoryLogger()
        
        # Перевіряємо, чи історія порожня на старті
        self.assertEqual(len(history_logger.history), 0)
        self.assertEqual(history_logger.display_history(), "")

if __name__ == "__main__":
    unittest.main()
