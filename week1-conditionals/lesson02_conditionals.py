# Clase 2 · Decisiones con if / elif / else

# --- Comparaciones: dan True o False ---
edad = 32
print(edad > 30)    # True
print(edad == 40)   # False (== compara, = guarda)
print(edad != 40)   # True (distinto)
print(edad >= 32)   # True

# --- if / else ---
if edad >= 40:
    print("Ya tienes 40 o más")
else:
    print(f"Te faltan {40 - edad} años para los 40")

# --- if / elif / else: entra solo en el primero que se cumple ---
tasa = 43
if tasa >= 40:
    print("Excelente")
elif tasa >= 30:
    print("Bien")
else:
    print("Alerta")

# --- and / not ---
ahorro = 94000
gastos = 6000
if ahorro > 50000 and gastos < 7000:
    print("Vas muy bien")

tiene_visa = False
if not tiene_visa:
    print("Falta la visa")
