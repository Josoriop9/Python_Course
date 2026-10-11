# LeetCode · Valid Palindrome (versión simplificada)

def es_palindromo(texto):
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]

print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("casa"))                # False
print(es_palindromo(""))                    # True
