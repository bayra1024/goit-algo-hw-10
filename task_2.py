import scipy.integrate as spi

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Задана функція
def f(x):
    return x**2 + 12 * x + 5


# Діапазон інтегрування
a = 0
b = 2

# Генерація значень x для графіка
x_values = np.linspace(a - 1, b + 1, 1000)
y_values = f(x_values)

# Графік функції
plt.plot(x_values, y_values, label=r"$x^2 + 12x + 5$")

# Заштрихована область під кривою
x_fill = np.linspace(a, b, 100)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, alpha=0.3, color="gray", label="Площа під кривою")

# Налаштування графіка
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.title("Графік функції та площа під кривою")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Відображення графіка
plt.show()

# Обчислення інтегралу методом Монте-Карло
# Максимальне значення функції на обраному діапазоні
max_y = max(f(np.linspace(a, b, 1000)))

# Кількість випадкових точок
num_points = 10000

# Генерація випадкових точок
random_x = np.random.uniform(a, b, num_points)
random_y = np.random.uniform(0, max_y, num_points)

# Кількість точок, що попадають під криву
points_under_curve = np.sum(random_y <= f(random_x))

# Відношення кількості точок під кривою до загальної кількості точок
ratio = points_under_curve / num_points

# Обчислення оцінки інтегралу
integral_estimate = (b - a) * max_y * ratio

# Виведення результату
print("Інтеграл методом Монте-Карло:", integral_estimate)

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)
