import pulp

# Створення моделі оптимізації
model = pulp.LpProblem("Production Optimization", pulp.LpMaximize)

# Оголошення змінних рішення
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit Juice", lowBound=0, cat='Integer')

# Об'єктивна функція для максимізації виробництва
model += lemonade + fruit_juice, "Total Production"

# Обмеження на ресурси
model += 2 * (lemonade + fruit_juice) <= 100, "Water Constraint"
model += lemonade <= 50, "Sugar Constraint"
model += lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Вирішення моделі
model.solve()

# Вивід результатів
print("Optimal Production Plan:")
print("Lemonade:", pulp.value(lemonade))
print("Fruit Juice:", pulp.value(fruit_juice))
print("Total Production:", pulp.value(model.objective))
