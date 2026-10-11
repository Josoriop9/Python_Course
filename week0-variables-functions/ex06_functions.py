# Lesson 6 · Exercises: functions
# Replace each "pass" with your code. The tests at the bottom should print True.


# 1. Return how many vowels the text has, ignoring upper/lower case.
def count_vowels(text):
    pass


# 2. Return "review" if it's over 10000, "high" if it's over 1000, otherwise "normal".
def classify(amount):
    pass


# 3. Take a list and return a dictionary with how many times each item appears.
def count_frequencies(items):
    pass


# 4. Challenge: take the complaints list and return the fraud percentage
#    (complaints that contain "didn't make").
def fraud_percentage(complaints):
    pass


# --- Tests ---
print(count_vowels("Colombia") == 4)
print(classify(7000) == "high")
print(classify(10000) == "high")
print(classify(15000) == "review")
print(count_frequencies(["a", "b", "a"]) == {"a": 2, "b": 1})

complaints = [
    "They charged me twice",
    "The app won't open",
    "There's a purchase I didn't make",
    "they CHARGED me twice again",
    "I want to change my address",
]
print(fraud_percentage(complaints) == 20.0)
