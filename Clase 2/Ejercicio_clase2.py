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

# 1. Según porcentaje_ahorro: Excelente / Bien / Alerta
if porcentaje_ahorro >= 40:
    print("excelente")
elif porcentaje_ahorro >=30:
    print("bien")
else:   
    print("estas ahorrando poco")

# 2. Runway: ahorro_actual / gastos_mensuales, y el mensaje según sea 12 o más
runway = math.floor(ahorro_actual/gastos_mensuales)
print(f"Runway: {runway} meses")

if runway >=12: 
    print("Tienes mas de una ano de colchon")
else:
    print("construye un colchon")
# 3. ¿Ya llegaste a la meta? Si no, cuántos meses faltan
if ahorro_actual >= meta:
    print("ya llegaste a la meta!")
else:
    print(f"aun no llegas faltan {meses_meta}")