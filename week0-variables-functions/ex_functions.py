# Clase 6 · Ejercicios de funciones
# Reemplaza cada "pass" por tu código. Las pruebas de abajo deben imprimir True.


# 1. Devuelve cuántas vocales tiene el texto, sin importar mayúsculas.
def contar_vocales(texto):
    pass


# 2. Devuelve "revision" si pasa de 10000, "alto" si pasa de 1000, si no "normal".
def clasificar(monto):
    pass


# 3. Recibe una lista y devuelve el diccionario de conteo.
def contar_frecuencias(lista):
    pass


# 4. Reto: recibe la lista de reclamos y devuelve el porcentaje de fraude ("no hice").
def porcentaje_fraude(reclamos):
    pass


# --- Pruebas ---
print(contar_vocales("Colombia") == 4)
print(clasificar(7000) == "alto")
print(clasificar(10000) == "alto")
print(clasificar(15000) == "revision")
print(contar_frecuencias(["a", "b", "a"]) == {"a": 2, "b": 1})

reclamos = [
    "Me cobraron dos veces",
    "La app no abre",
    "Hay una compra que no hice",
    "me COBRARON dos veces otra vez",
    "Quiero cambiar mi dirección",
]
print(porcentaje_fraude(reclamos) == 20.0)
