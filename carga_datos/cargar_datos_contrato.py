import os
from classes.DatosContrato import DatosContrato
import pandas as pd

def cargar_datos_contrato(ruta_archivo):
    columnas_importantes = ['Referencia de contrato', 'Fecha de Contrato', 'Fecha de entrada', 'Fecha de salida',
                            'Numero de personas',
                            'Tipo de Pago', 'Fecha de Pago', 'Medio de Pago', 'Titular del Pago',
                            'Fecha de caducidad de la Tarjeta']

    extension = os.path.splitext(ruta_archivo)[1].lower()

    # Leer el archivo según el formato
    if extension in ['.xls', '.xlsx', '.odf']:  # Archivos Excel y OpenDocument
        contrato_data = pd.read_excel(ruta_archivo, usecols=columnas_importantes, dtype=str)
    elif extension == '.csv':  # Archivos CSV
        contrato_data = pd.read_csv(ruta_archivo, usecols=columnas_importantes, dtype=str)
    else:
        raise ValueError(f"Formato de archivo no compatible: {extension}")

    contrato_data.fillna("", inplace=True)
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