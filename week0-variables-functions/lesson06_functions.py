# Lesson 6 · Functions


# --- 1. Define and call ---
def greet():
    print("Hello, Juan Carlos")

greet()
greet()


# --- 2. Parameters: the data it receives ---
def greet_person(name):
    print(f"Hello, {name}")

greet_person("Ana")
greet_person("Marcelo")


# --- 3. print vs return ---
def double_print(number):
    print(number * 2)       # shows it, but hands nothing back (returns None)

def double_return(number):
    return number * 2       # hands the value back so you can keep using it

result = double_return(5)
print(result + 1)           # 11

r = double_print(3)         # prints 6
print(r)                    # None: without return, a function returns None


# --- 4. An exercise turned into a function ---
def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("house"))                        # False


# --- 5. Several parameters, and return ends the function ---
def classify(amount, high_limit):
    if amount > high_limit:
        return "review"
    return "normal"

print(classify(15000, 10000))  # review


# --- 6. Break something on purpose (remove the # to see the error) ---
def add(a, b):
    return a + b

# add(3)   # TypeError: missing 1 required positional argument


# --- 7. What happens inside, stays inside ---
def calculate():
    total = 100

calculate()
# print(total)   # NameError: total only exists inside the function
