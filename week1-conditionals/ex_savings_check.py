# Lesson 2 · Exercise: savings check
import math

monthly_income = 10600
monthly_expenses = 6000
current_savings = 94000
goal = 150000

monthly_savings = monthly_income - monthly_expenses
savings_rate = monthly_savings / monthly_income * 100
months_to_goal = math.ceil((goal - current_savings) / monthly_savings)

print(f"Monthly savings: {monthly_savings}")
print(f"You save {round(savings_rate, 1)}% of your income")

# 1. Based on the savings rate
if savings_rate >= 40:
    print("Excellent")
elif savings_rate >= 30:
    print("Good")
else:
    print("You're saving too little")

# 2. Runway: how many months your savings cover
runway = math.floor(current_savings / monthly_expenses)
print(f"Runway: {runway} months")
if runway >= 12:
    print("You have more than a year of cushion")
else:
    print("Build a cushion")

# 3. Did you reach the goal?
if current_savings >= goal:
    print("You reached your goal!")
else:
    print(f"Not there yet, {months_to_goal} months to go")
