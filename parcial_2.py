#UNIVERSIDAD LIBRE
#SECCIONAL CALI
#ELECTIVA PROFESIONAL 1
#CAMILO ANDRES NORIEGA
#164023

from urllib.request import urlopen
import json
import io
ruta = "https://random-data-api.com/api/commerce/random_commerce?size=100"

 


response = urlopen(ruta)  

 

data = json.loads(response.read())

 

archivos = "archivo1.txt"
resultados = list()
archivo=io.open(archivos,"w")
for i in range(101):
  response = urlopen(ruta)  
  d_json = json.loads(response.read())
  
  resultados.append(d_json)

 



for x in range(len(resultados)-1):
  for y in resultados[x]:
    if x == 0:
      archivo.write("{},".format(y))
    else:
      archivo.write(",{}".format(y))

 


archivo.close()
