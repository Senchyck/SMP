import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.api_client import APIClient
from presistance.repository import Repository
from app.unit_of_work import UnitOfWork
from ui.user_interface import UserInterface
from presistance.data_saver import DataSaver
from presistance.history_logger import HistoryLogger

def main():
    # Ініціалізація об'єктів
    api_client = APIClient()
    user_repository = Repository()#Repository
    history_logger = HistoryLogger() #Singletone

    # Отримання даних
    users = api_client.fetch_users()
    posts = api_client.fetch_posts()

    # Збереження даних за допомогою Unit of Work
    uow = UnitOfWork(user_repository)
    for user in users:
        uow.register_new(user)
    uow.commit()

    # Виведення даних в таблиці
    ui = UserInterface()
    ui.display_table(
        [(user['id'], user['name'], user['email']) for user in users],
        ["ID", "Name", "Email"]
    )

    # Збереження даних у файл JSON
    DataSaver.save_to_json(users, "users.json")

    # Логування історії
    history_logger.log("Fetch Users", users)#Поліморфізм можна викликати для об'єктів різних типів, якщо вони мають однакові назви і сигнатури:
    history_logger.log("Fetch Posts", posts)

    # Перегляд історії
    print("\nHistory:")
    for log in history_logger.get_history():
        print(log)

if __name__ == "__main__":
    main()
