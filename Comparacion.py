import json
import pandas as pd
from pandas import json_normalize

# El input se deja como string y además, se pasa todo a minúscula
cerveza = str(input('¿Qué marca de cerveza estás buscando? ')).lower()
print('La cerveza buscada es: {}\n'.format(cerveza))


#--------------------------------------------
# TOTTUS
#--------------------------------------------
with open('cervezas-tottus.json') as f:
    d = json.load(f)

dataTottus = json_normalize(d['cervezas'])
colsTottus = ['Brand','Description','Price']
rowsTottus = []
for i in range(len(dataTottus)):
    rowsTottus.append([dataTottus['name'][i], dataTottus['description'][i], dataTottus['regularPrice'][i]])

df_Tottus = pd.DataFrame(rowsTottus, columns=colsTottus)
df_Tottus['Brand'] = df_Tottus['Brand'].str.lower() # Se transforma todo el texto de la columna en minúscula, para poder realizar comparación

print('Precios para la cerveza marca "{}" en Supermercado Tottus\n'.format(cerveza))
print(df_Tottus[df_Tottus['Brand'].str.contains(cerveza)])
#--------------------------------------------
# LIDER
#--------------------------------------------
with open('cervezas-lider.json') as f:
    d = json.load(f)

dataLider = json_normalize(d['cervezas'])
colsLider = ['Brand','Description','Price']
rowsLider = []
for i in range(len(dataLider)):
    rowsLider.append([dataLider['name'][i], dataLider['description'][i], dataLider['regularPrice'][i]])

df_Lider = pd.DataFrame(rowsLider, columns=colsLider)
df_Lider['Brand'] = df_Lider['Brand'].str.lower()

print('\nPrecios para la cerveza marca "{}" en Supermercado Lider\n'.format(cerveza))
print(df_Lider[df_Lider['Brand'].str.contains(cerveza)])