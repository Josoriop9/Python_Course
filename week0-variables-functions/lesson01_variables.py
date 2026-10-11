# Clase 1 · Variables, tipos y operaciones

# --- Variables: el = significa "guarda aquí" ---
nombre = "Juan Carlos"
edad = 32
ciudad = "New York"
print(nombre, edad, ciudad)
print(type(nombre))

# --- Tipos ---
texto = "hola"      # str: texto
entero = 10         # int: número entero
decimal = 4.5       # float: número con decimales
activo = True       # bool: True o False
print(type(decimal))  # <class 'float'>

# --- Operaciones ---
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333... (siempre da float)
print(10 // 3)  # 3 (división entera)
print(10 % 3)   # 1 (el residuo)
print(2 ** 3)   # 8 (potencia)

# --- Textos y f-strings ---
saludo = "hola"
print(saludo.upper())          # HOLA
print(len(saludo))             # 4
print(f"{nombre} tiene {edad} años")
print("Edad: " + str(edad))    # convertir a texto para pegarlo
print(f"Edad: {edad}")         # la f-string es la mejor opción

# --- Convertir texto a número ---
numero_texto = "100"
numero = int(numero_texto)
print(numero + 50)  # 150
