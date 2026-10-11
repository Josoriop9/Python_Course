# Warm-ups · counter and accumulator with a condition

numbers = [3, 8, 1, 9, 4]

# Counter: how many are over 5 -> 2
over_five = 0
for number in numbers:
    if number > 5:
        over_five = over_five + 1
print(over_five)

# Accumulator: total sum -> 25
total = 0
for number in numbers:
    total = total + number
print(total)

# Accumulator with a condition: sum of those over 5 -> 17
total_over_five = 0
for number in numbers:
    if number > 5:
        total_over_five = total_over_five + number
print(total_over_five)

words = ["sun", "house", "sea", "window"]

# How many words have more than 3 letters -> 2
long_words = 0
for word in words:
    if len(word) > 3:
        long_words = long_words + 1
print(long_words)

# Total letters -> 17
letters = 0
for word in words:
    letters = letters + len(word)
print(letters)

phrases = ["hello world", "i really love python", "good morning"]

# How many phrases have more than 2 words -> 1
long_phrases = 0
for phrase in phrases:
    if len(phrase.split()) > 2:
        long_phrases = long_phrases + 1
print(long_phrases)

# Total words -> 8
total_words = 0
for phrase in phrases:
    total_words = total_words + len(phrase.split())
print(total_words)
