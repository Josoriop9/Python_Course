# Clase 2 · Ejercicio: chequeo de ahorro
import math

ingreso_mensual = 10600
gastos_mensuales = 6000
ahorro_actual = 94000
meta = 150000

ahorro_mensual = ingreso_mensual - gastos_mensuales
porcentaje_ahorro = ahorro_mensual / ingreso_mensual * 100
meses_meta = math.ceil((meta - ahorro_actual) / ahorro_mensual)

print(f"Ahorro mensual: {ahorro_mensual}")
print(f"Ahorras el {round(porcentaje_ahorro, 1)}% de tu ingreso")

# 1. Según el porcentaje de ahorro
if porcentaje_ahorro >= 40:
    print("Excelente")
elif porcentaje_ahorro >= 30:
    print("Bien")
else:
    print("Estás ahorrando poco")

# 2. Runway: cuántos meses te cubre el ahorro
runway = math.floor(ahorro_actual / gastos_mensuales)
print(f"Runway: {runway} meses")
if runway >= 12:
    print("Tienes más de un año de colchón")
else:
    print("Construye un colchón")

# 3. ¿Ya llegaste a la meta?
if ahorro_actual >= meta:
    print("¡Ya llegaste a la meta!")
else:
    print(f"Aún no llegas, faltan {meses_meta} meses")
