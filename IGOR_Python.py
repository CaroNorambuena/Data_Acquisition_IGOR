
# FUNCIONES CONVERSOR IGOR A PHYTON

def conversor(archivo_txt, nombre_csv):

    from charset_normalizer import detect
    import csv

    with open(archivo_txt, 'rb') as f:
        encoding = detect(f.read())['encoding']

    with open(archivo_txt, encoding=encoding) as archivo:
        lineas = archivo.readlines()
        archivo.close()

    nombre_archivo_csv = nombre_csv
    with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['-', 'tiempo', 'voltaje'])
        for linea in lineas:
            # Dividir cada línea en base al delimitador (en este caso, una coma)
            datos = linea.strip().split(',')
            escritor_csv.writerow(datos)
    
    return nombre_archivo_csv

def edit_dataframe(nombre_csv):

    import pandas as pd

    spikes = pd.read_csv(nombre_csv) # esta función de pandas lee csv y convierte a dataframe
    work_spikes = spikes.copy()
    df = work_spikes.iloc[1: , [1, 2]] # se selecciona las filas de la 1 en adelante y las columna tiempo y voltaje.

    return df

def plot_dataframe(df):

    import matplotlib.pyplot as plt

    # Crear el gráfico
    plt.plot(df["tiempo"], df["voltaje"], color='b', label= 'voltaje vs tiempo')

    # Añadir etiquetas y título
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Voltaje (uV)')
    plt.title('Actividad neuronal')

    # Mostrar leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()

    return plt.show()