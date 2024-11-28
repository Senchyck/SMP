import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Завдання 2: Завантаження даних з CSV
def load_data(file_path):
    """Функція для завантаження даних з CSV."""
    try:
        data = pd.read_csv(file_path)
        print("Дані успішно завантажені!")
        print(data.head())
        return data
    except Exception as e:
        print("Помилка при завантаженні даних:", e)
        return None

# Завдання 3: Дослідження даних
def explore_data(data):
    """Функція для дослідження даних."""
    print("\nОпис даних:")
    print(data.describe())
    print("\nМаксимальні значення:\n", data.max())
    print("\nМінімальні значення:\n", data.min())

# Завдання 4: Вибір типів візуалізацій (приклад обраних — описано нижче)

# Завдання 5: Підготовка даних
def prepare_data(data):
    """Функція для очищення та підготовки даних."""
    print("\nПеревірка пропущених значень:")
    print(data.isnull().sum())
    
    # Видалення пропусків
    data = data.dropna()
    print("Пропуски видалено.")
    return data

# Завдання 6: Базова візуалізація
def basic_visualization(data, column):
    """Функція для створення базової візуалізації."""
    plt.plot(data[column], color='blue')
    plt.title(f'Базова візуалізація: {column}')
    plt.xlabel('Індекс')
    plt.ylabel(column)
    plt.show()

# Завдання 7: Розширені візуалізації
def advanced_visualizations(data, column1, column2):
    """Функція для створення більш складних візуалізацій."""
    # Гістограма
    plt.hist(data[column1], bins=20, color='skyblue')
    plt.title(f'Гістограма {column1}')
    plt.xlabel(column1)
    plt.ylabel('Частота')
    plt.show()

    # Діаграма розсіювання
    plt.scatter(data[column1], data[column2], c='green', alpha=0.5)
    plt.title(f'Діаграма розсіювання {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

# Завдання 8: Декілька піддіаграм
def multiple_subplots(data, columns):
    """Функція для створення кількох піддіаграм."""
    fig, axs = plt.subplots(1, len(columns), figsize=(15, 5))

    for i, column in enumerate(columns):
        axs[i].plot(data[column], label=column, color='orange')
        axs[i].set_title(f'Графік {column}')
        axs[i].legend()

    plt.tight_layout()
    plt.show()

# Завдання 9: Експорт і інтерактивні візуалізації
def export_visualization(data, column1, column2):
    """Функція для експорту графіків."""
    # Інтерактивний графік
    fig = px.scatter(data, x=column1, y=column2, title=f'Інтерактивна діаграма: {column1} vs {column2}')
    fig.write_html('interactive_plot.html')
    print("Інтерактивна діаграма збережена як interactive_plot.html")
    fig.show()

# Головна функція
if __name__ == "__main__":
    file_path = 'your_dataset.csv'  # Замість цього вкажіть шлях до вашого файлу CSV

    # Завантаження даних
    data = load_data(file_path)
    if data is None:
        exit()

    # Дослідження даних
    explore_data(data)

    # Підготовка даних
    data = prepare_data(data)

    # Базова візуалізація
    basic_visualization(data, column='column_name')  # Вкажіть ім'я стовпця

    # Розширені візуалізації
    advanced_visualizations(data, column1='column_name1', column2='column_name2')  # Вкажіть назви стовпців

    # Кілька піддіаграм
    multiple_subplots(data, columns=['column_name1', 'column_name2', 'column_name3'])  # Вкажіть потрібні стовпці

    # Експорт візуалізацій
    export_visualization(data, column1='column_name1', column2='column_name2')
