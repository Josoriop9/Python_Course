# Lesson 4 · Strings

word = "python"
print(word[0])     # p
print(word[-1])    # n
print(len(word))   # 6

# --- A string can be looped like a list of letters ---
for letter in "wow":
    print(letter)

# --- Slices [start:end:step]: end is not included ---
print(word[0:3])   # pyt
print(word[2:])    # thon
print(word[::-1])  # nohtyp, reversed

# --- Methods ---
phrase = "  Hello World  "
print(phrase.lower())           # "  hello world  "
print(phrase.strip())           # "Hello World"
print(phrase.replace(" ", ""))  # "HelloWorld"
print("banana".count("a"))      # 3

# --- in: is it inside? ---
print("a" in "cat")  # True
print("x" in "cat")  # False

# --- split and join ---
words = "i love python".split()   # ['i', 'love', 'python']
print(words)
print(" ".join(words))            # i love python

# split returns text: use int() to add
parts = "3,8,1".split(",")
print(int(parts[0]) + int(parts[1]))  # 11

# --- Build a string with a for loop ---
reversed_text = ""
for letter in "house":
    reversed_text = letter + reversed_text
print(reversed_text)              # esuoh

# --- Break something on purpose (remove the # to see the error) ---
# word[0] = "P"   # TypeError: strings can't be changed in place
