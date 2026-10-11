# LeetCode · Valid Palindrome (simplified)

def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("house"))                        # False
print(is_palindrome(""))                             # True
