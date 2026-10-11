#una lista 
#contar reclamos con mas de 4 palabras 
#cuento cada linea la que tenga mas de 4 le sumo uno al contador 
#contador con condicion

"""
reclamos = [
    "Me cobraron dos veces",
    "La app no abre",
    "Hay una compra que no hice",
    "me COBRARON dos veces otra vez",
    "Quiero cambiar mi dirección",
]

contador = 0
for reclamo in reclamos:
    palabras = len(reclamo.split())
    if palabras > 4:
        contador = contador + 1
print(contador)  # 2


numeros = [3, 8, 1, 9, 4]

#1
contador = 0
for numero in numeros: 
    if numero > 5:
        contador = contador + 1
print(contador)

contador = 0
for numero in range(1,5): 
    if numero % 2:
        contador = contador + 1
print(contador)

#2
acumulador = 0 
for numero in numeros: 
    acumulador = acumulador + numero 
print(acumulador)

acumulador = 0 
for numero in numeros: 
    if numero > 5:
        acumulador = acumulador + numero 
print(acumulador)


#3 
palabras = ["sol", "casa", "mar", "ventana"]

contador_palabras = 0 
for palabra in palabras:
    word = len(palabra)
    if word > 3:
        contador_palabras = contador_palabras + 1
print(contador_palabras)

contador_palabras = 0 
for palabra in palabras:
    word = len(palabra)
    contador_palabras = contador_palabras + word
print(contador_palabras)


#4
frases = ["hola mundo", "yo amo python mucho", "buenos dias"]


contador = 0 
for frase in frases: 
    ph = len(frase.split())
    if ph > 2:
        contador = contador + 1
print(contador)


contador = 0 
for frase in frases: 
    ph = len(frase.split())
    contador = contador + ph
print(contador)



#¿Qué tengo? una lista 
#¿Qué quiero? saber cuantos cobraron aparecen en los reclamos 
#¿Cómo lo haría a mano? recorrer cada lista e ir sacando la palabra si corresponde o hace match 
#¿Qué patrón es? contador

reclamos = [
    "Me cobraron dos veces",
    "La app no abre",
    "Hay una compra que no hice",
    "me COBRARON dos veces otra vez",
    "Quiero cambiar mi dirección",
]

contador = 0
for reclamo in reclamos:
    texto = reclamo.lower()
    if "no hice" in texto:
        contador = contador + 1
total_reclamos = len(reclamos)
porcentaje_fraude = contador / total_reclamos * 100
if porcentaje_fraude > 15: 
    print(f'precaucion Alerta de fraude inminente, porcentaje {round(porcentaje_fraude)}%')
else:
    print(f'todo al pelo, porcentaje {round(porcentaje_fraude)}%')



#print(round(total),"%")
#print(len(reclamos))
#print(contador)
    








for reclamo in reclamos:
    if "cobraron" in reclamo.lower():
        print(f"la categoria de tu reclamo: {reclamo} es: cobro_duplicado")
    elif "no hice" in reclamo:
        print(f"la categoria de tu reclamo: {reclamo} es: fraude")
    elif "app" in reclamo:
        print(f"la categoria de tu reclamo: {reclamo} es: app_caida")
    else:
        print(f"la categoria de tu reclamo: {reclamo} es: otro")




campeon = reclamos[0] 
for reclamo in reclamos: 
    if len(reclamo) > len(campeon):
        campeon = reclamo
print(campeon)


contador = 0
for reclamo in reclamos:
    if "cobraron" in reclamo.lower():
        contador = contador + 1

print(contador)


"""




#1. Variables y operaciones 
"""
ahorro = 94000
gasto_mensual = 6000

meses_cubiertos = ahorro // gasto_mensual
print(meses_cubiertos)

cantidad_sobrante = ahorro % gasto_mensual
print(cantidad_sobrante)


#2. Desiciones 

monto = 12500

if monto >= 10000: 
    print("revision")
elif monto >= 1000:
    print("alto")
else:
    print("normal")



#3. Acum+cont etc 

transacciones = [120, 4500, 80, 15000, 300, 9800]

contador = 0 
for transaccion in transacciones:
    contador = contador + transaccion
print(contador)

acumulador = 0 
for transaccion in transacciones:
    acumulador = acumulador + 1
    total = contador / acumulador
print(round(total, 1))

contador1 = 0
for transaccion in transacciones:
    if transaccion >= 1000:
        contador1 = contador1 + 1
print(contador1)

#4. Campeon al reves
campeon = transacciones[0] 
for transaccion in transacciones:
    if campeon > transaccion:
        campeon = transaccion
print(campeon)



#5 Todo junto 
transacciones = [120, 4500, 80, 15000, 300, 9800]

transacciones = [120, 4500, 80, 15000, 300, 9800]

for transaccion in transacciones:
    if transaccion > 10000:
        categoria = "revision"
    elif transaccion > 1000:
        categoria = "alto"
    else:
        categoria = "normal"
    print(f"{transaccion} es {categoria}")


#6. Textos y split 

datos = "120,4500,80,15000"

partes = datos.split(",")
total = 0
for parte in partes:
    total = total + int(parte)
print(total)


#7 contar letras
contador = 0
for letra in "Anthropic":
    minimo = letra.lower()
    if minimo in "aeiou":
        contador = contador + 1
print(contador)


#8 Palindromo 

palabra = "Anita lava la tina"
minusculas = palabra.lower()
texto_sin_espacios = minusculas.replace(" ", "")
#print(texto_sin_espacios)
girado = texto_sin_espacios[::-1]
#print(girado)
print(texto_sin_espacios == girado)
"""
