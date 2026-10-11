ingreso_mensual = 10600
gastos_mensuales = 6000
ahorro_actual = 94000
meta = 150000

ahorro_mensual = ingreso_mensual - gastos_mensuales
print("Ahorro mensual: ", ahorro_mensual)

meses_necesarios = (meta - ahorro_actual) / ahorro_mensual
print("Meses necesarios para alcanzar la meta: ", round(meses_necesarios))

porcentaje_ahorrado = (ahorro_actual / meta) * 100
print("Porcentaje ahorrado: ", round(porcentaje_ahorrado, 2), "%")

print(f"Tu ahorro mensual es: {ahorro_mensual}" f"\nMeses necesarios para alcanzar la meta: {round(meses_necesarios)}" f"\nPorcentaje ahorrado: {round(porcentaje_ahorrado, 2)}%")

