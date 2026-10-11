# Clase 5 · Diccionarios

# --- Una ficha con cajones: llave -> valor ---
cliente = {"nombre": "Banco Andino", "pais": "CO", "empleados": 10000}
print(cliente["nombre"])       # Banco Andino

# --- Agregar y cambiar ---
cliente["sector"] = "banca"    # no existía: la crea
cliente["empleados"] = 12000   # ya existía: la reemplaza

# --- Cajones que no existen ---
# print(cliente["telefono"])   # KeyError
print(cliente.get("telefono", "no registrado"))

# --- ¿Existe el cajón? ---
print("pais" in cliente)       # True

# --- Recorrer: dos variables por vuelta ---
for llave, valor in cliente.items():
    print(f"{llave}: {valor}")

# --- Lista de diccionarios ---
casos = [
    {"reclamo": "Me cobraron dos veces", "esperado": "cobro_duplicado"},
    {"reclamo": "La app no abre", "esperado": "app_caida"},
]
for caso in casos:
    print(caso["reclamo"])

# --- Patrón: contar frecuencias ---
frutas = ["mango", "pera", "mango"]
conteo = {}
for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] = conteo[fruta] + 1   # ya existe: le sumo 1
    else:
        conteo[fruta] = 1                   # no existe: lo creo en 1
print(conteo)   # {'mango': 2, 'pera': 1}
