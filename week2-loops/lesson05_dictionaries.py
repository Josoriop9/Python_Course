# Lesson 5 · Dictionaries

# --- A card with labeled drawers: key -> value ---
client = {"name": "Andes Bank", "country": "CO", "employees": 10000}
print(client["name"])        # Andes Bank

# --- Add and change ---
client["sector"] = "banking"   # didn't exist: creates it
client["employees"] = 12000    # already existed: replaces it

# --- Keys that don't exist ---
# print(client["phone"])   # KeyError
print(client.get("phone", "not registered"))

# --- Does the key exist? ---
print("country" in client)   # True

# --- Loop: two variables per turn ---
for key, value in client.items():
    print(f"{key}: {value}")

# --- List of dictionaries ---
cases = [
    {"complaint": "They charged me twice", "expected": "duplicate_charge"},
    {"complaint": "The app won't open", "expected": "app_down"},
]
for case in cases:
    print(case["complaint"])

# --- Pattern: frequency count ---
fruits = ["mango", "pear", "mango"]
counts = {}
for fruit in fruits:
    if fruit in counts:
        counts[fruit] = counts[fruit] + 1   # exists: add 1
    else:
        counts[fruit] = 1                   # doesn't exist: create it at 1
print(counts)   # {'mango': 2, 'pear': 1}
