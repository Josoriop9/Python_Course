# Clase 4 · Textos

palabra = "python"
print(palabra[0])     # p
print(palabra[-1])    # n
print(len(palabra))   # 6

# --- Un texto se recorre como una lista de letras ---
for letra in "oso":
    print(letra)

# --- Rebanadas [inicio:fin:paso]: el fin no entra ---
print(palabra[0:3])   # pyt
print(palabra[2:])    # thon
print(palabra[::-1])  # nohtyp, invertido

# --- Métodos ---
frase = "  Hola Mundo  "
print(frase.lower())           # "  hola mundo  "
print(frase.strip())           # "Hola Mundo"
print(frase.replace(" ", ""))  # "HolaMundo"
print("banana".count("a"))     # 3

# --- in: ¿está adentro? ---
print("a" in "casa")  # True
print("x" in "casa")  # False

# --- split y join ---
palabras = "yo amo python".split()   # ['yo', 'amo', 'python']
print(palabras)
print(" ".join(palabras))            # yo amo python

# split devuelve textos: para sumar, int()
partes = "3,8,1".split(",")
print(int(partes[0]) + int(partes[1]))  # 11

# --- Construir un texto con un for ---
invertido = ""
for letra in "casa":
    invertido = letra + invertido
print(invertido)            # asac
print(invertido == "casa")  # False
