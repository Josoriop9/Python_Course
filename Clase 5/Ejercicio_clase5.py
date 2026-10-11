#1 
#Diccionario = {'nombre': 'juan', 'ciudad': 'NY', 'experiencia': '12 anos'}
#print(f'Hola, soy {Diccionario["nombre"]} vivo en {Diccionario["ciudad"]} y tengo {Diccionario["experiencia"]} de experiencia')

"""
#2
casos = [
    {"reclamo": "Me cobraron dos veces", "esperado": "cobro_duplicado"},
    {"reclamo": "La app no abre", "esperado": "app_caida"},
    {"reclamo": "Hay una compra que no hice", "esperado": "fraude"},
    {"reclamo": "Fui cobrado em dobro", "esperado": "cobro_duplicado"},
]

for caso in casos: 
    print(caso["reclamo"])


#3
casos = [
    {"reclamo": "Me cobraron dos veces", "esperado": "cobro_duplicado"},
    {"reclamo": "La app no abre", "esperado": "app_caida"},
    {"reclamo": "Hay una compra que no hice", "esperado": "fraude"},
    {"reclamo": "Fui cobrado em dobro", "esperado": "cobro_duplicado"},
]
contador = 0
for caso in casos: 
    if caso["esperado"] == "cobro_duplicado":
        contador = contador + 1
print(contador)
"""

#
casos = [
    {"reclamo": "Me cobraron dos veces", "esperado": "cobro_duplicado"},
    {"reclamo": "La app no abre", "esperado": "app_caida"},
    {"reclamo": "Hay una compra que no hice", "esperado": "fraude"},
    {"reclamo": "Fui cobrado em dobro", "esperado": "cobro_duplicado"},
]
contador = {}
for caso in casos: 
    categoria = caso["esperado"]
    if categoria in contador:
        contador[categoria] = contador[categoria] + 1
    else:
        contador[categoria] = 1
print(contador)
