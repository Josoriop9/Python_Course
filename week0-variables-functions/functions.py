# Clase 6 · Funciones


# --- 1. Definir y llamar ---
def saludar():
    print("Hola, Juan Carlos")

saludar()
saludar()


# --- 2. Parámetros: los datos que recibe ---
def saludar_a(nombre):
    print(f"Hola, {nombre}")

saludar_a("Ana")
saludar_a("Marcelo")


# --- 3. print contra return ---
def doble_print(numero):
    print(numero * 2)       # muestra, pero no entrega nada (devuelve None)

def doble_return(numero):
    return numero * 2       # entrega el valor para seguir usándolo

resultado = doble_return(5)
print(resultado + 1)        # 11

r = doble_print(3)          # imprime 6
print(r)                    # None: sin return, la función devuelve None


# --- 4. Un ejercicio convertido en función ---
def es_palindromo(texto):
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]

print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("casa"))                # False


# --- 5. Varios parámetros, y return termina la función ---
def clasificar(monto, limite_alto):
    if monto > limite_alto:
        return "revision"
    return "normal"

print(clasificar(15000, 10000))  # revision


# --- 6. Rompe algo a propósito (quita el # para ver el error) ---
def sumar(a, b):
    return a + b

# sumar(3)   # TypeError: falta un argumento


# --- 7. Lo que pasa dentro, se queda dentro ---
def calcular():
    total = 100

calcular()
# print(total)   # NameError: total solo existe dentro de la función
