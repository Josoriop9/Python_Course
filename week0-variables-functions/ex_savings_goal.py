# Lesson 1 · Exercise: savings goal

monthly_income = 10600
monthly_expenses = 6000
current_savings = 94000
goal = 150000

monthly_savings = monthly_income - monthly_expenses
months_needed = (goal - current_savings) / monthly_savings
percent_saved = (current_savings / goal) * 100

print(f"Monthly savings: {monthly_savings}")
print(f"Months needed to reach the goal: {round(months_needed)}")
print(f"Percent saved: {round(percent_saved, 2)}%")
