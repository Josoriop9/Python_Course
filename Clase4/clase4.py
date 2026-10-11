"""


palabra = "python"
print(palabra[0])    # p
print(palabra[-1])   # n
print(len(palabra))  # 6

for letra in "oso":
    print(letra)   # o, s, o

print(palabra[0:3])   # pyt
print(palabra[2:])    # thon, desde la posición 2 hasta el final
print(palabra[::-1])  # nohtyp, invertido

frase = "  Hola Mundo  "
print(frase.lower())           # "  hola mundo  "
print(frase.strip())           # "Hola Mundo"
print(frase.replace(" ", ""))  # "HolaMundo"
print("banana".count("a"))     # 3

print("a" in "casa")  # True
print("x" in "casa")  # False

palabras = "yo amo python".split()  
print(palabras)
unido = " ".join(palabras)        
print(unido)



resultado = ""
for letra in "abc":
    resultado = resultado + letra
print(resultado)  # abc

"""

texto = "casa"

invertido = ""
for letra in texto:
    invertido = letra + invertido 

print(invertido)           
print(invertido == texto)  