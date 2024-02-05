import scipy.integrate as spi

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return x**2 + 12 * x + 5


a = 0
b = 2

x_values = np.linspace(a - 1, b + 1, 1000)
y_values = f(x_values)

plt.plot(x_values, y_values, label=r"$x^2 + 12x + 5$")

x_fill = np.linspace(a, b, 100)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, alpha=0.3, color="gray", label="Площа під кривою")

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.title("Графік функції та площа під кривою")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()

max_y = max(f(np.linspace(a, b, 1000)))

num_points = 10000

random_x = np.random.uniform(a, b, num_points)
random_y = np.random.uniform(0, max_y, num_points)

points_under_curve = np.sum(random_y <= f(random_x))

ratio = points_under_curve / num_points

integral_estimate = (b - a) * max_y * ratio

print("Інтеграл методом Монте-Карло:", integral_estimate)

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)
