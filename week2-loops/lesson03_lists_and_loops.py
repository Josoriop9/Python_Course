# Lesson 3 · Lists and for loops

# --- Lists: positions start at 0 ---
savings = [4600, 5200, 3900, 4800]
print(savings)
print(len(savings))  # 4
print(savings[0])    # 4600, the first one
print(savings[-1])   # 4800, the last one

savings.append(6100)  # adds to the end
savings[0] = 4700     # changes the first one
print(savings)

# --- for: goes through them one by one ---
for amount in savings:
    print(amount)

# --- Accumulator: add up values ---
total = 0
for amount in savings:
    total = total + amount
print(total)

# --- Counter: add 1 when something is true ---
high_months = 0
for amount in savings:
    if amount > 5000:
        high_months = high_months + 1
print(high_months)

# --- Champion: keep the best so far ---
best = savings[0]
for amount in savings:
    if amount > best:
        best = amount
print(best)

# --- range: the last number is not included ---
for month in range(2, 13, 2):
    print(f"Month {month}")   # 2, 4, 6, 8, 10, 12

# --- Break something on purpose (remove the # to see the error) ---
# print(savings[10])   # IndexError: that position doesn't exist
