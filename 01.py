import pulp

model = pulp.LpProblem("Production optimization", pulp.LpMaximize)

x_lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
x_fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Integer')

model += x_lemonade + x_fruit_juice, "Total Products"

model += 2 * x_lemonade + 1 * x_fruit_juice <= 100, "Water Constraint"  
model += 1 * x_lemonade <= 50, "Sugar Constraint" 
model += 1 * x_lemonade <= 30, "Lemon Juice Constraint" 
model += 2 * x_fruit_juice <= 40, "Fruit Puree Constraint"  

model.solve()

print(f"Optimal Lemonade value: {x_lemonade.varValue}")
print(f"Optimal Fruit Juice value: {x_fruit_juice.varValue}")
print(f"Total Products: {pulp.value(model.objective)}")
