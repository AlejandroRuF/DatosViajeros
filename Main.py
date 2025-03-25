import pandas as pd
import os

from DatosContrato import DatosContrato
from DatosEstablecimiento import DatosEstablecimiento
from DatosViajeros import DatosViajero

formatos_compatibles = ['.xls', '.xlsx','.odf','.csv']

def listar_archivos_compatibles(directorio):
    archivos_compatibles = []

    for archivo in os.listdir(directorio):
        nombre,extension = os.path.splitext(archivo)

        if extension in formatos_compatibles:
            archivos_compatibles.append(archivo)

    return archivos_compatibles


def cargar_datos_viajeros(ruta_archivo):
    columnas_importantes = ['Nombre', 'Primer apellido', 'Segundo apellido', 'Fecha de nacimiento',
                            'Tipo de documento', 'Número de documento', 'Teléfono', 'Correo electrónico',
                            'País', 'Código País', 'Dirección', 'Provincia', 'Municipio',
                            'Código postal', 'Parentesco', 'Código Parentesco']
    extension = os.path.splitext(ruta_archivo)[1].lower()

    if extension in ['.xls', '.xlsx', '.odf']:
        viajeros_data = pd.read_excel(ruta_archivo, usecols=columnas_importantes)

    else:
        viajeros_data = pd.read_csv(ruta_archivo, usecols=columnas_importantes)

    viajeros_data = viajeros_data[viajeros_data['Nombre'].notna() & (viajeros_data['Nombre'] != '')]
    viajeros = []
    for _, row in viajeros_data.iterrows():
        viajero = DatosViajero(
            nombre=row['Nombre'],
            primer_apellido=row['Primer apellido'],
            segundo_apellido=row['Segundo apellido'],
            fecha_nacimiento=row['Fecha de nacimiento'],
            tipo_documento=row['Tipo de documento'],
            numero_documento=row['Número de documento'],
            telefono=row['Teléfono'],
            correo_electronico=row['Correo electrónico'],
            codigo_pais=row['Código País'],
            direccion=row['Dirección'],
            provincia=row['Provincia'],
            municipio=row['Municipio'],
            codigo_postal=row['Código postal'],
            codigo_parentesco=row['Código Parentesco']
        )
        viajeros.append(viajero)


    for viajero in viajeros:
        print(viajero)

    return viajeros


def cargar_datos_establecimiento(ruta_archivo):
    columnas_importantes = ['Nombre del establecimiento', 'Código del establecimiento', 'Tipo de establecimiento',
                            'Dirección', 'Provincia', 'Municipio', 'Código Postal', 'País', 'Teléfono',
                            'Correo electrónico']

    extension = os.path.splitext(ruta_archivo)[1].lower()

    # Leer el archivo según el formato
    if extension in ['.xls', '.xlsx', '.odf']:  # Archivos Excel y OpenDocument
        establecimiento_data = pd.read_excel(ruta_archivo, usecols=columnas_importantes)
    elif extension == '.csv':  # Archivos CSV
        establecimiento_data = pd.read_csv(ruta_archivo, usecols=columnas_importantes)
    else:
        raise ValueError(f"Formato de archivo no compatible: {extension}")

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


# Función para cargar los datos del contrato desde el archivo
def cargar_datos_contrato(ruta_archivo):
    columnas_importantes = ['Referencia de contrato', 'Fecha de Contrato', 'Fecha de entrada', 'Fecha de salida',
                            'Numero de personas',
                            'Tipo de Pago', 'Fecha de Pago', 'Medio de Pago', 'Titular del Pago',
                            'Fecha de caducidad de la Tarjeta']

    extension = os.path.splitext(ruta_archivo)[1].lower()

    # Leer el archivo según el formato
    if extension in ['.xls', '.xlsx', '.odf']:  # Archivos Excel y OpenDocument
        contrato_data = pd.read_excel(ruta_archivo, usecols=columnas_importantes)
    elif extension == '.csv':  # Archivos CSV
        contrato_data = pd.read_csv(ruta_archivo, usecols=columnas_importantes)
    else:
        raise ValueError(f"Formato de archivo no compatible: {extension}")

    # Crear la lista de objetos DatosContrato
    contratos = []
    for _, row in contrato_data.iterrows():
        contrato = DatosContrato(
            referencia_contrato=row['Referencia de contrato'],
            fecha_contrato=row['Fecha de Contrato'],
            fecha_entrada=row['Fecha de entrada'],
            fecha_salida=row['Fecha de salida'],
            numero_personas=row['Numero de personas'],
            tipo_pago=row['Tipo de Pago'],
            fecha_pago=row['Fecha de Pago'],
            medio_pago=row['Medio de Pago'],
            titular_pago=row['Titular del Pago'],
            fecha_caducidad_tarjeta=row['Fecha de caducidad de la Tarjeta']
        )
        contratos.append(contrato)

    for contrato in contratos:
        print(contrato)

    return contratos


correcto = False
directorio_proyecto = os.getcwd()

while not correcto:
    archivos_compatibles = listar_archivos_compatibles(directorio_proyecto)
    ruta_datos_contrato = ""
    ruta_datos_establecimiento = ""
    ruta_datos_viajeros = ""

    if archivos_compatibles:
        for index,archivo in enumerate(archivos_compatibles):
            print(f"{index+1}- {archivo}")

        try:
            num_establecimiento = int(input(f"Selecciona el número asociado a los datos de Establecimento -> "))-1
            ruta_datos_establecimiento = f"{directorio_proyecto}\\{archivos_compatibles[num_establecimiento]}"
            print(ruta_datos_establecimiento)
        except:
            print("Los datos introducidos no son válidos")
            break

        try:
            num_contrato = int(input(f"Selecciona el número asociado a datos de Contrato -> "))-1
            ruta_datos_contrato = f"{directorio_proyecto}\\{archivos_compatibles[num_contrato]}"
            print(ruta_datos_contrato)
        except:
            print("Los datos introducidos no son válidos")
            break

        try:
            num_viajeros = int(input(f"Selecciona el número asociado a los datos de Viajeros -> "))-1
            ruta_datos_viajeros = f"{directorio_proyecto}\\{archivos_compatibles[num_viajeros]}"
            print(ruta_datos_viajeros)
        except:
            print("Los datos introducidos no son válidos")
            break

        print("\nDatos de establecimiento")
        print('------------------------------------------------------------------------------------------')
        datos_establecimientos = cargar_datos_establecimiento(ruta_datos_establecimiento)
        print('\nDatos de contrato')
        print('------------------------------------------------------------------------------------------')
        datos_contratos = cargar_datos_contrato(ruta_datos_contrato)
        print('\nDatos de viajero')
        print('------------------------------------------------------------------------------------------')
        datos_viajeros = cargar_datos_viajeros(ruta_datos_viajeros)
        print('------------------------------------------------------------------------------------------\n')
    else:
        print("No existen archivos compatibles")

    pregunta = input(f"Los datos vistos anteriormente son Correctos? Pulsa S/N -> ").upper()
    correcto = pregunta in ['S', 'SI']

print("FUERA")