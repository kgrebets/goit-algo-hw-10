import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа


def monte_carlo_area(f, a, b, num_samples=5000):
    x_random = np.random.uniform(a, b, num_samples)
    y_max = max(f(np.linspace(a, b, 1000)))
    y_random = np.random.uniform(0, y_max, num_samples)
    is_under_curve_arr = y_random < f(x_random) #масив що показує чи входит точка до нашої фігури
    area_rectangle = (b - a) * y_max
    monte_carlo_result = area_rectangle * np.sum(is_under_curve_arr) / num_samples
    return monte_carlo_result, x_random, y_random, is_under_curve_arr

monte_carlo_result, x_random, y_random, is_under_curve = monte_carlo_area(f, a, b)

integral_value, error = quad(f, a, b)

# Виведення результатів
print(f"Площа під кривою (інтеграл за методом квадратур) = {integral_value:.4f}")
print(f"Площа під кривою (інтеграл за методом Монте-Карло) = {monte_carlo_result:.4f}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання випадкових точок на графік
ax.scatter(x_random, y_random, color='blue', s=2, label='Над кривою')
ax.scatter(x_random[is_under_curve], y_random[is_under_curve], color='green', s=2, label='Під кривою')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}\n'
             f'Квадратури: {integral_value:.4f}, Монте-Карло: {monte_carlo_result:.4f}')
plt.grid()
plt.legend()
plt.show()