# Clase 1 · Ejercicio: meta de ahorro

ingreso_mensual = 10600
gastos_mensuales = 6000
ahorro_actual = 94000
meta = 150000

ahorro_mensual = ingreso_mensual - gastos_mensuales
meses_necesarios = (meta - ahorro_actual) / ahorro_mensual
porcentaje_ahorrado = (ahorro_actual / meta) * 100

print(f"Tu ahorro mensual es: {ahorro_mensual}")
print(f"Meses necesarios para alcanzar la meta: {round(meses_necesarios)}")
print(f"Porcentaje ahorrado: {round(porcentaje_ahorrado, 2)}%")
