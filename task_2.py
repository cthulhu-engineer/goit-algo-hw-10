import random
import scipy.integrate as spi


def monte_carlo_integration(func, a, b, n):
    total_area = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, 2)
        if y <= func(x):
            total_area += 1
    return total_area / n * (b - a)


# Функція, для якої ми обчислюємо інтеграл
def sample_function(x):
    return x ** 3


# Параметри для обчислення інтеграла
a = 0
b = 2
n = 1000000

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(sample_function, a, b, n)
print("Monte Carlo Integration Result:", monte_carlo_result)

# Обчислення інтеграла за допомогою quad
quad_result, _ = spi.quad(sample_function, a, b)
print("Quad Integration Result:", quad_result)
