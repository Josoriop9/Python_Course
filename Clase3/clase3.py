"""
ahorros = [4600, 5200, 3900, 4800]
print(ahorros)
print(len(ahorros))  # 4

print(ahorros[0])   # 4600, el primero
print(ahorros[1])   # 5200, el segundo
print(ahorros[-1])  # 4800, el último


ahorros.append(6100)  # agrega al final
ahorros[0] = 4700     # cambia el primero
print(ahorros) 

for ahorro in ahorros:
    print(ahorro)

total = 0
for ahorro in ahorros:
    total = total + ahorro
print(total)

meses_altos = 0
for ahorro in ahorros:
    if ahorro > 5000:
        meses_altos = meses_altos + 1
print(meses_altos)



for mes in range(2,13, 2):
    print(f"Mes {mes}")  



for mes in range(1,13):
    if mes % 2 == 0: 
        print(mes)
    """


ahorros = [4600, 5200, 3900, 4800, 6100, 4400]

totall = 0
for ahorro in ahorros:
    totall = totall + ahorro
print(totall)

totall = 0
for ahorro in ahorros:
    totall = totall + ahorro
print(totall)

promedio = totall / len(ahorros)
print(promedio)

meses_bajos = 0
for ahorro in ahorros: 
    if ahorro < 4500:
        meses_bajos = meses_bajos + 1 
print(meses_bajos)

mejor = ahorros[0]
for ahorro in ahorros:
    if ahorro > mejor:
        mejor = ahorro
print(mejor)