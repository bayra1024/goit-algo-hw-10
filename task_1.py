from pulp import LpProblem, LpMaximize, LpVariable, LpStatus


model = LpProblem(name="Production_Maximization", sense=LpMaximize)


lemonade_units = LpVariable(name="Lemonade_units", lowBound=0, cat="Integer")
fruit_juice_units = LpVariable(name="Fruit_juice_units", lowBound=0, cat="Integer")


model += lemonade_units + fruit_juice_units, "Total_Products"


model += 2 * lemonade_units + 0 * fruit_juice_units <= 100, "Water_constraint"
model += 1 * lemonade_units + 1 * fruit_juice_units <= 50, "Sugar_constraint"
model += 1 * lemonade_units + 0 * fruit_juice_units <= 30, "Lemon_juice_constraint"
model += 0 * lemonade_units + 2 * fruit_juice_units <= 40, "Fruit_puree_constraint"


model += 2 * lemonade_units + 1 * fruit_juice_units <= 100, "Water_usage"
model += 1 * lemonade_units + 0 * fruit_juice_units <= 50, "Sugar_usage"
model += 1 * lemonade_units + 0 * fruit_juice_units <= 30, "Lemon_juice_usage"
model += 0 * lemonade_units + 2 * fruit_juice_units <= 40, "Fruit_puree_usage"


model.solve()


print("Status:", LpStatus[model.status])

print(f"Optimal quantity of Lemonade: {lemonade_units.varValue}")
print(f"Optimal quantity of Fruit Juice: {fruit_juice_units.varValue}")

print(f"Maximum total quantity of products: {model.objective.value()}")
