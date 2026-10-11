# Capstone · Bank complaints (lessons 1 to 4)

complaints = [
    "They charged me twice",
    "The app won't open",
    "There's a purchase I didn't make",
    "they CHARGED me twice again",
    "I want to change my address",
]

# Complaints with more than 4 words -> 3
long_complaints = 0
for complaint in complaints:
    if len(complaint.split()) > 4:
        long_complaints = long_complaints + 1
print(long_complaints)

# Part 3 · How many mention "charged", ignoring case -> 2
charged = 0
for complaint in complaints:
    if "charged" in complaint.lower():
        charged = charged + 1
print(charged)

# Part 4 · The longest complaint (champion)
longest = complaints[0]
for complaint in complaints:
    if len(complaint) > len(longest):
        longest = complaint
print(longest)

# Part 5 · Category for each complaint
for complaint in complaints:
    text = complaint.lower()
    if "charged" in text:
        category = "duplicate_charge"
    elif "didn't make" in text:
        category = "fraud"
    elif "app" in text:
        category = "app_down"
    else:
        category = "other"
    print(f"{complaint} -> {category}")

# Part 6 · Fraud percentage and alert -> 20%
frauds = 0
for complaint in complaints:
    if "didn't make" in complaint.lower():
        frauds = frauds + 1
total_complaints = len(complaints)
fraud_percentage = frauds / total_complaints * 100
if fraud_percentage > 15:
    print(f"Fraud alert: {round(fraud_percentage)}%")
else:
    print(f"All good: {round(fraud_percentage)}%")
