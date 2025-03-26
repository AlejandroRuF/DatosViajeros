import os
import pandas as pd

from classes.DatosEstablecimiento import DatosEstablecimiento


def cargar_datos_establecimiento(ruta_archivo):
    columnas_importantes = ['Nombre del establecimiento', 'Código del establecimiento', 'Tipo de establecimiento',
                            'Dirección', 'Provincia', 'Municipio', 'Código Postal', 'País', 'Teléfono',
                            'Correo electrónico']

    extension = os.path.splitext(ruta_archivo)[1].lower()

    # Leer el archivo según el formato
    if extension in ['.xls', '.xlsx', '.odf']:  # Archivos Excel y OpenDocument
        establecimiento_data = pd.read_excel(ruta_archivo, usecols=columnas_importantes, dtype=str)
    elif extension == '.csv':  # Archivos CSV
        establecimiento_data = pd.read_csv(ruta_archivo, usecols=columnas_importantes, dtype=str)
    else:
        raise ValueError(f"Formato de archivo no compatible: {extension}")
    establecimiento_data.fillna("", inplace=True)
    # Crear la lista de objetos DatosEstablecimiento
    establecimientos = []
    for _, row in establecimiento_data.iterrows():
        establecimiento = DatosEstablecimiento(
            nombre_establecimiento=row['Nombre del establecimiento'],
            codigo_establecimiento=row['Código del establecimiento'],
            tipo_establecimiento=row['Tipo de establecimiento'],
            direccion=row['Dirección'],
            provincia=row['Provincia'],
            municipio=row['Municipio'],
            codigo_postal=row['Código Postal'],
            pais=row['País'],
            telefono=row['Teléfono'],
            correo_electronico=row['Correo electrónico']
        )
        establecimientos.append(establecimiento)

    for establecimiento in establecimientos:
        print(establecimiento)

    return establecimientos