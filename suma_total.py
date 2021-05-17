#UNIVERSIDAD LIBRE
#SECCIONAL CALI
#ELECTIVA PROFESIONAL 1
#CAMILO ANDRES NORIEGA
#164023
#SUMA

import json
import os

    
def get_datos(ruta):
    with open(ruta) as contenido:
        objeto = json.load(contenido)
        
    return objeto;


def ventas_depto(datos):
    # suma los campos
    suma = {}
    for componente in datos:
        suma[componente['department']] = suma.get(componente['department'], 0) + componente['price']

    # guarda el archivo
    with open('ventas_depto.json', 'w') as json_file:
        json.dump(suma, json_file)


def ventas_materiales(datos):
    # suma los campos
    suma = {}
    for componente in datos:
        suma[componente['material']] = suma.get(componente['material'], 0) + componente['price']

    # guarda el archivo
    with open('ventas_materiales.json', 'w') as json_file:
        json.dump(suma, json_file)


def ventas_colores(datos):
    # suma los campos
    suma = {}
    for componente in datos:
        suma[componente['color']] = suma.get(componente['color'], 0) + componente['price']

    # guarda el archivo
    with open('ventas_colores.json', 'w') as json_file:
        json.dump(suma, json_file)



def ventas_categorias(datos):
    # suma los campos
    suma = {}
    for componente in datos:
        suma[str(componente['product_name']).split()[-1]] = suma.get(str(componente['product_name']).split()[-1], 0) + componente['price']

    # guarda el archivo 
    with open('ventas_categorias.json', 'w') as json_file:
        json.dump(suma, json_file)



if __name__ == '__main__':
    base = '/home/spark/segundo_corte'
    file = 'archivo5.json' 
    ruta = os.path.join(base, file)
    datos = get_datos(ruta)
    
    ventas_depto(datos)
    #ventas_categorias(datos)
    #ventas_materiales(datos)
    #ventas_colores(datos)
