# Lesson 3 · Exercise: savings analysis

savings = [4600, 5200, 3900, 4800, 6100, 4400]

# 1. Total (accumulator)
total = 0
for amount in savings:
    total = total + amount
print(f"Total: {total}")

# 2. Average
average = total / len(savings)
print(f"Average: {round(average, 1)}")

# 3. Low months (counter)
low_months = 0
for amount in savings:
    if amount < 4500:
        low_months = low_months + 1
print(f"Low months: {low_months}")

# 4. Best month without max() (champion)
best = savings[0]
for amount in savings:
    if amount > best:
        best = amount
print(f"Best month: {best}")
