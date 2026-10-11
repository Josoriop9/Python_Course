# Lesson 1 · Variables, types and operations

# --- Variables: = means "store this here" ---
name = "Juan Carlos"
age = 32
city = "New York"
print(name, age, city)

# --- Types ---
text = "hello"      # str: text
whole = 10          # int: whole number
decimal = 4.5       # float: number with decimals
active = True       # bool: True or False
print(type(decimal))  # <class 'float'>

# --- Operations ---
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333... (always a float)
print(10 // 3)  # 3 (integer division)
print(10 % 3)   # 1 (remainder)
print(2 ** 3)   # 8 (power)

# --- Strings and f-strings ---
greeting = "hello"
print(greeting.upper())        # HELLO
print(len(greeting))           # 5
print(f"{name} is {age} years old")
print("Age: " + str(age))      # convert to text before joining
print(f"Age: {age}")           # f-strings are the best option

# --- Convert text to a number ---
number_text = "100"
number = int(number_text)
print(number + 50)  # 150

# --- Break something on purpose (remove the # to see the error) ---
# print("Age: " + 32)   # TypeError: can't join text and a number
