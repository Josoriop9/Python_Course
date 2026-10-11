# Repaso · Clases 1 a 4

# 1. Variables y operaciones -> 15 meses, sobran 4000
ahorro = 94000
gasto_mensual = 6000
meses_cubiertos = ahorro // gasto_mensual
sobrante = ahorro % gasto_mensual
print(f"Te cubre {meses_cubiertos} meses y sobran {sobrante}")

# 2. Decisiones ("pasa de" es >, no >=)
monto = 12500
if monto > 10000:
    print("revision")
elif monto > 1000:
    print("alto")
else:
    print("normal")

transacciones = [120, 4500, 80, 15000, 300, 9800]

# 3. Total, promedio y cuántas pasan de 1000 -> 29800, 4966.7, 3
total = 0
for transaccion in transacciones:
    total = total + transaccion
promedio = total / len(transacciones)
altas = 0
for transaccion in transacciones:
    if transaccion > 1000:
        altas = altas + 1
print(total, round(promedio, 1), altas)

# 4. La más pequeña sin min() -> 80
menor = transacciones[0]
for transaccion in transacciones:
    if transaccion < menor:
        menor = transaccion
print(menor)

# 5. Etiqueta para cada una: reglas, no respuestas
for transaccion in transacciones:
    if transaccion > 10000:
        categoria = "revision"
    elif transaccion > 1000:
        categoria = "alto"
    else:
        categoria = "normal"
    print(f"{transaccion} es {categoria}")

# 6. Textos y split -> 19700
datos = "120,4500,80,15000"
partes = datos.split(",")
suma = 0
for parte in partes:
    suma = suma + int(parte)
print(suma)

# 7. Vocales de "Anthropic" -> 3
vocales = 0
for letra in "Anthropic":
    if letra.lower() in "aeiou":
        vocales = vocales + 1
print(vocales)

# 8. Palíndromo -> True
palabra = "Anita lava la tina"
limpio = palabra.lower().replace(" ", "")
print(limpio == limpio[::-1])
