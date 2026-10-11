# Integrador · Reclamos bancarios (clases 1 a 4)

reclamos = [
    "Me cobraron dos veces",
    "La app no abre",
    "Hay una compra que no hice",
    "me COBRARON dos veces otra vez",
    "Quiero cambiar mi dirección",
]

# Reclamos con más de 4 palabras -> 2
largos = 0
for reclamo in reclamos:
    if len(reclamo.split()) > 4:
        largos = largos + 1
print(largos)

# Parte 3 · Cuántos mencionan "cobraron", sin importar mayúsculas -> 2
cobros = 0
for reclamo in reclamos:
    if "cobraron" in reclamo.lower():
        cobros = cobros + 1
print(cobros)

# Parte 4 · El reclamo más largo (campeón)
mas_largo = reclamos[0]
for reclamo in reclamos:
    if len(reclamo) > len(mas_largo):
        mas_largo = reclamo
print(mas_largo)

# Parte 5 · Categoría de cada reclamo
for reclamo in reclamos:
    texto = reclamo.lower()
    if "cobraron" in texto:
        categoria = "cobro_duplicado"
    elif "no hice" in texto:
        categoria = "fraude"
    elif "app" in texto:
        categoria = "app_caida"
    else:
        categoria = "otro"
    print(f"{reclamo} -> {categoria}")

# Parte 6 · Porcentaje de fraude y alerta -> 20%
fraudes = 0
for reclamo in reclamos:
    if "no hice" in reclamo.lower():
        fraudes = fraudes + 1
total_reclamos = len(reclamos)
porcentaje_fraude = fraudes / total_reclamos * 100
if porcentaje_fraude > 15:
    print(f"Alerta de fraude: {round(porcentaje_fraude)}%")
else:
    print(f"Todo bien: {round(porcentaje_fraude)}%")
