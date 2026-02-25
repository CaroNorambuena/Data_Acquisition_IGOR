
#SCRIPT PARA CREAR MATRIZ DE DATOS (DATASET) DE ACTIVIDAD NEURONAL DESDE IGOR A PYTHON
#REGISTRO CON 32 CANALES

"1. Importar libreria"

import IGOR_Python

"2. Conversión a DataFrame"

#Guardar nombres de archivos en una lista. En este caso son 32 archivos, nombrados del 1 al 32.
archivos_txt = []
for i in range(1, 33):
    archivos_txt.append(f"E{i}.txt")

print(archivos_txt)

#Generar una lista para los archivos csv
archivos_csv = []
for i in range(1, 33):
    archivos_csv.append(f"E{i}.csv")

print(archivos_csv)

#Aplicar la función conversor que convierte archivos txt a csv
for archivo_txt, archivo_csv in zip (archivos_txt, archivos_csv):
    IGOR_Python.conversor(archivo_txt, archivo_csv)

#Editar y guardar en un dataframe
numeros = []  # también puede se el total de canales que se usaron para registrar
for i in range(1, 33):
    numeros.append(i)
print(numeros)

#Se crea un diccionario de DataFrames para mapear nombres personalizados a cada DataFrame.
dataframes = {}
for archivo_csv, numeros in zip (archivos_csv, numeros):
    df = IGOR_Python.edit_dataframe(archivo_csv)
    dataframes[f"df{numeros}"] = df
print(dataframes)

"3. Unir en un solo DataFrame"

from functools import reduce
import pandas as pd

# Realizar el merge de todos los DataFrames en el diccionario
resultado = reduce(lambda left, right: pd.merge(left, right, on='tiempo'), dataframes.values())
resultado.head()

# Lista con los nuevos encabezados
encabezados = ['tiempo']
for i in range(1, 33):
    encabezados.append(f"E{i}")
print(encabezados)

# Renombrar las columnas
resultado.columns = [encabezados]
resultado.head()

#Guardar en un archivo csv
resultado.to_csv('Test1_32 sites_140825_210355.csv', sep=',')