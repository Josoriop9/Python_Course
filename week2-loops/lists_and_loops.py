# Clase 3 · Listas y ciclos for

# --- Listas: las posiciones empiezan en 0 ---
ahorros = [4600, 5200, 3900, 4800]
print(ahorros)
print(len(ahorros))  # 4
print(ahorros[0])    # 4600, el primero
print(ahorros[-1])   # 4800, el último

ahorros.append(6100)  # agrega al final
ahorros[0] = 4700     # cambia el primero
print(ahorros)

# --- for: recorre uno por uno ---
for ahorro in ahorros:
    print(ahorro)

# --- Acumulador: sumo valores ---
total = 0
for ahorro in ahorros:
    total = total + ahorro
print(total)

# --- Contador: sumo 1 cuando se cumple algo ---
meses_altos = 0
for ahorro in ahorros:
    if ahorro > 5000:
        meses_altos = meses_altos + 1
print(meses_altos)

# --- range: el último no entra ---
for mes in range(2, 13, 2):
    print(f"Mes {mes}")   # 2, 4, 6, 8, 10, 12

for mes in range(1, 13):
    if mes % 2 == 0:
        print(mes)        # los pares
