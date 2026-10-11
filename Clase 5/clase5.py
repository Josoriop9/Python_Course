cliente = {"nombre": "Banco Andino", "pais": "CO", "empleados": 10000}
#print(cliente["pais"])     # Banco Andino

cliente["sector"] = "banca"    # no existía: la crea
cliente["empleados"] = 12000   # ya existía: la reemplaza
#print(cliente["empleados"])    
#print("pais" in cliente) 

for llave, valor in cliente.items():
    #print(f"{llave}: {valor}")

    casos = [
    {"reclamo": "Me cobraron dos veces", "esperado": "cobro_duplicado"},
    {"reclamo": "La app no abre", "esperado": "app_caida"},
]
#for caso in casos:
    #print(caso["reclamo"])


frutas = ["mango", "pera", "mango"]
conteo = {}
for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] = conteo[fruta] + 1
    else:
        conteo[fruta] = 1
print(conteo)   # {'mango': 2, 'pera': 1}