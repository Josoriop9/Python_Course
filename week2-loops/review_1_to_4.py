# Review · Lessons 1 to 4

# 1. Variables and operations -> 15 months, 4000 left over
savings = 94000
monthly_expense = 6000
months_covered = savings // monthly_expense
left_over = savings % monthly_expense
print(f"It covers {months_covered} months with {left_over} left over")

# 2. Decisions ("over" means >, not >=)
amount = 12500
if amount > 10000:
    print("review")
elif amount > 1000:
    print("high")
else:
    print("normal")

transactions = [120, 4500, 80, 15000, 300, 9800]

# 3. Total, average and how many are over 1000 -> 29800, 4966.7, 3
total = 0
for transaction in transactions:
    total = total + transaction
average = total / len(transactions)
high_ones = 0
for transaction in transactions:
    if transaction > 1000:
        high_ones = high_ones + 1
print(total, round(average, 1), high_ones)

# 4. The smallest one without min() -> 80
smallest = transactions[0]
for transaction in transactions:
    if transaction < smallest:
        smallest = transaction
print(smallest)

# 5. Label each one: rules, not answers
for transaction in transactions:
    if transaction > 10000:
        category = "review"
    elif transaction > 1000:
        category = "high"
    else:
        category = "normal"
    print(f"{transaction} is {category}")

# 6. Strings and split -> 19700
data = "120,4500,80,15000"
parts = data.split(",")
total_parts = 0
for part in parts:
    total_parts = total_parts + int(part)
print(total_parts)

# 7. Vowels in "Anthropic" -> 3
vowels = 0
for letter in "Anthropic":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
print(vowels)

# 8. Palindrome -> True
phrase = "A man a plan a canal Panama"
clean = phrase.lower().replace(" ", "")
print(clean == clean[::-1])
