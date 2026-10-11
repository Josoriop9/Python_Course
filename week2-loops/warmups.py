# Calentamiento · contador y acumulador con condición

numeros = [3, 8, 1, 9, 4]

# Contador: cuántos pasan de 5 -> 2
mayores = 0
for numero in numeros:
    if numero > 5:
        mayores = mayores + 1
print(mayores)

# Acumulador: suma total -> 25
suma = 0
for numero in numeros:
    suma = suma + numero
print(suma)

# Acumulador con condición: suma de los que pasan de 5 -> 17
suma_mayores = 0
for numero in numeros:
    if numero > 5:
        suma_mayores = suma_mayores + numero
print(suma_mayores)

palabras = ["sol", "casa", "mar", "ventana"]

# Cuántas palabras tienen más de 3 letras -> 2
largas = 0
for palabra in palabras:
    if len(palabra) > 3:
        largas = largas + 1
print(largas)

# Total de letras -> 17
letras = 0
for palabra in palabras:
    letras = letras + len(palabra)
print(letras)

frases = ["hola mundo", "yo amo python mucho", "buenos dias"]

# Cuántas frases tienen más de 2 palabras -> 1
frases_largas = 0
for frase in frases:
    if len(frase.split()) > 2:
        frases_largas = frases_largas + 1
print(frases_largas)

# Total de palabras -> 8
total_palabras = 0
for frase in frases:
    total_palabras = total_palabras + len(frase.split())
print(total_palabras)
