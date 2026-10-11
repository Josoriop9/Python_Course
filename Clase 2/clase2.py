edad = 32
print(edad > 30)    # True
print(edad == 40)   # False (== compara, = asigna)
print(edad != 40)   # True (distinto)
print(edad >= 32)   # True

edad = 32
if edad >= 40:
    print("Ya tienes 40 o más")
else:
    print(f"Te faltan {40 - edad} años para los 40")

tasa = 43
if tasa >= 40:
    print("Excelente")
elif tasa >= 30:
    print("Bien")
else:
    print("Alerta")


ahorro = 94000
gastos = 6000
if ahorro > 50000 and gastos < 7000:
    print("Vas muy bien")

tiene_visa = False
if not tiene_visa:
    print("Falta la visa")