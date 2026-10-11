# Lesson 2 · Decisions with if / elif / else

# --- Comparisons: they give True or False ---
age = 32
print(age > 30)    # True
print(age == 40)   # False (== compares, = stores)
print(age != 40)   # True (not equal)
print(age >= 32)   # True

# --- if / else ---
if age >= 40:
    print("You're 40 or older")
else:
    print(f"{40 - age} years to go until 40")

# --- if / elif / else: only the first match runs ---
rate = 43
if rate >= 40:
    print("Excellent")
elif rate >= 30:
    print("Good")
else:
    print("Warning")

# --- and / not ---
savings = 94000
expenses = 6000
if savings > 50000 and expenses < 7000:
    print("You're doing great")

has_visa = False
if not has_visa:
    print("Visa missing")

# --- Even or odd with % ---
number = 7
if number % 2 == 0:
    print("even")
else:
    print("odd")
