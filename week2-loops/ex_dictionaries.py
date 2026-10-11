# Lesson 5 · Exercises: dictionaries

# Level 1 · My profile
profile = {"name": "Juan Carlos", "city": "NY", "experience": 12}
print(f"Hi, I'm {profile['name']}, I live in {profile['city']} "
      f"and I have {profile['experience']} years of experience")

cases = [
    {"complaint": "They charged me twice", "expected": "duplicate_charge"},
    {"complaint": "The app won't open", "expected": "app_down"},
    {"complaint": "There's a purchase I didn't make", "expected": "fraud"},
    {"complaint": "I was charged double", "expected": "duplicate_charge"},
]

# Level 2 · Print only the complaints
for case in cases:
    print(case["complaint"])

# Level 3 · Count duplicate charges -> 2
duplicates = 0
for case in cases:
    if case["expected"] == "duplicate_charge":
        duplicates = duplicates + 1
print(duplicates)

# Level 4 · Frequency of each category
counts = {}
for case in cases:
    category = case["expected"]
    if category in counts:
        counts[category] = counts[category] + 1
    else:
        counts[category] = 1
print(counts)   # {'duplicate_charge': 2, 'app_down': 1, 'fraud': 1}
