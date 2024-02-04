import numpy as np
from scipy.integrate import quad


def monte_carlo(num_points):
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, f(b), num_points)
    # Обчислення кількості точок, які потрапили під криву
    points_under_curve = sum(random_y <= f(random_x))
    # Обчислення відсотка площі під кривою
    area_ratio = points_under_curve / num_points
    # Обчислення площі області
    total_area = (b - a) * f(b)
    # Обчислення значення інтегралу
    integral_value = total_area * area_ratio

    return integral_value


# Функція, для якої ми обчислюємо інтеграл
def f(x):
    return x ** 3


# Параметри для обчислення інтеграла
a = 0
b = 2
# Обчислення інтеграла за допомогою методу Монте-Карло
num_points = [10000, 20000, 50000, 10, 100, 1000]

analytical_solution_quad, _ = quad(f, a, b)

print("Обчислення інтеграла за допмогою метод Монте-Карло: ")
for points in num_points:
    estimate = monte_carlo(points)
    error = np.abs(estimate - analytical_solution_quad)
    print(f"Кількість точок: {points}, інтеграл: {estimate}, помилка: {error}")
