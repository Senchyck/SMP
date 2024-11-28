# 1. Імпортуємо необхідні бібліотеки
import pandas as pd
import matplotlib.pyplot as plt

# 2. Завантаження даних
file_path = 'your_dataset.csv'
data = pd.read_csv(file_path)
print("Дані успішно завантажені!")
print(data)

# 3. Аналіз даних
print("\nОпис даних:")
print(data.describe())

print("\nМаксимальні значення:\n", data.max())
print("\nМінімальні значення:\n", data.min())

# 4. Базова візуалізація
plt.plot(data['column1'], marker='o', label='Column 1')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Лінійний графік для Column 1')
plt.legend()
plt.grid()
plt.show()

# 5. Більш складна візуалізація
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].plot(data['column1'], color='r', label='Column 1')
axs[0].set_title('Column 1')
axs[0].legend()

axs[1].bar(data.index, data['column2'], color='g', label='Column 2')
axs[1].set_title('Column 2')
axs[1].legend()

axs[2].scatter(data['column1'], data['column3'], color='b', label='Column 1 vs Column 3')
axs[2].set_title('Column 1 vs Column 3')
axs[2].legend()

plt.tight_layout()
plt.show()
