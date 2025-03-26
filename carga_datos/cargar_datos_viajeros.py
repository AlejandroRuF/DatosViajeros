import os
import pandas as pd
from classes.DatosViajeros import DatosViajero


def cargar_datos_viajeros(ruta_archivo):
    columnas_importantes = [
        'Nombre', 'Primer apellido', 'Segundo apellido', 'Fecha de nacimiento',
        'Tipo de documento', 'Número del Documento', 'Soporte del Documento(solo DNI o NIF)',
        'Codigo de la Nacionalidad', 'Teléfono', 'Código País', 'Dirección', 'Provincia',
        'Código del Municipio(Solo España)', 'Municipio', 'Código postal', 'Código Parentesco'
    ]

    extension = os.path.splitext(ruta_archivo)[1].lower()

    if extension in ['.xls', '.xlsx', '.odf']:
        viajeros_data = pd.read_excel(ruta_archivo, usecols=columnas_importantes, dtype=str)
    else:
        viajeros_data = pd.read_csv(ruta_archivo, usecols=columnas_importantes, dtype=str)

    viajeros_data.fillna("", inplace=True)
    viajeros_data = viajeros_data[viajeros_data['Nombre'].notna() & (viajeros_data['Nombre'] != '')]

    viajeros = []
    for _, row in viajeros_data.iterrows():
        codigo_pais = row['Código País']
        codigo_municipio = row['Código del Municipio(Solo España)'] if codigo_pais == 'ESP' else None
        nombre_municipio = row['Municipio'] if codigo_pais != 'ESP' else None

        viajero = DatosViajero(
            nombre=row['Nombre'],
            primer_apellido=row['Primer apellido'],
            segundo_apellido=row['Segundo apellido'],
            fecha_nacimiento=row['Fecha de nacimiento'],
            tipo_documento=row['Tipo de documento'],
            numero_documento=row['Número del Documento'],
            soporte_documento=row['Soporte del Documento(solo DNI o NIF)'],
            telefono=row['Teléfono'],
            codigo_pais=codigo_pais,
            direccion=row['Dirección'],
            provincia=row['Provincia'],
            codigo_municipio=codigo_municipio,
            nombre_municipio=nombre_municipio,
            codigo_postal=row['Código postal'],
            codigo_parentesco=row['Código Parentesco'],
            codigo_nacionalidad=row['Codigo de la Nacionalidad'],
        )
        viajeros.append(viajero)

    # Imprimir viajeros para verificar
    for viajero in viajeros:
        print(viajero)

    return viajeros