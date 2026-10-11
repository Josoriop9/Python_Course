# Clase 5 · Ejercicios de diccionarios

# Nivel 1 · Mi ficha
perfil = {"nombre": "Juan Carlos", "ciudad": "NY", "experiencia": 12}
print(f"Hola, soy {perfil['nombre']}, vivo en {perfil['ciudad']} "
      f"y tengo {perfil['experiencia']} años de experiencia")

casos = [
    {"reclamo": "Me cobraron dos veces", "esperado": "cobro_duplicado"},
    {"reclamo": "La app no abre", "esperado": "app_caida"},
    {"reclamo": "Hay una compra que no hice", "esperado": "fraude"},
    {"reclamo": "Fui cobrado em dobro", "esperado": "cobro_duplicado"},
]

# Nivel 2 · Imprimir solo los reclamos
for caso in casos:
    print(caso["reclamo"])

# Nivel 3 · Contar cobros duplicados -> 2
cobros = 0
for caso in casos:
    if caso["esperado"] == "cobro_duplicado":
        cobros = cobros + 1
print(cobros)

# Nivel 4 · Frecuencia de cada categoría
conteo = {}
for caso in casos:
    categoria = caso["esperado"]
    if categoria in conteo:
        conteo[categoria] = conteo[categoria] + 1
    else:
        conteo[categoria] = 1
print(conteo)   # {'cobro_duplicado': 2, 'app_caida': 1, 'fraude': 1}
