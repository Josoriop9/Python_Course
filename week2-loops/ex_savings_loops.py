# Clase 3 · Ejercicio: análisis de ahorros

ahorros = [4600, 5200, 3900, 4800, 6100, 4400]

# 1. Total (acumulador)
total = 0
for ahorro in ahorros:
    total = total + ahorro
print(f"Total: {total}")

# 2. Promedio
promedio = total / len(ahorros)
print(f"Promedio: {round(promedio, 1)}")

# 3. Meses bajos (contador)
meses_bajos = 0
for ahorro in ahorros:
    if ahorro < 4500:
        meses_bajos = meses_bajos + 1
print(f"Meses bajos: {meses_bajos}")

# 4. Mejor mes sin max() (campeón)
mejor = ahorros[0]
for ahorro in ahorros:
    if ahorro > mejor:
        mejor = ahorro
print(f"Mejor mes: {mejor}")
