import os

from typing import List
from carga_datos.cargar_datos_contrato import cargar_datos_contrato
from carga_datos.cargar_datos_establecimiento import cargar_datos_establecimiento
from carga_datos.cargar_datos_viajeros import cargar_datos_viajeros
from classes.DatosContrato import DatosContrato
from classes.DatosEstablecimiento import DatosEstablecimiento
from classes.DatosViajeros import DatosViajero
from funciones_xml.funciones_xml import generar_xml

formatos_compatibles = ['.xls', '.xlsx','.odf','.csv']

def listar_archivos_compatibles(directorio):
    archivos_compatibles = []

    for archivo in os.listdir(directorio):
        nombre,extension = os.path.splitext(archivo)

        if extension in formatos_compatibles:
            archivos_compatibles.append(archivo)

    return archivos_compatibles


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
        datos_establecimientos:List[DatosEstablecimiento] = cargar_datos_establecimiento(ruta_datos_establecimiento)
        print('\nDatos de contrato')
        print('------------------------------------------------------------------------------------------')
        datos_contratos:List[DatosContrato] = cargar_datos_contrato(ruta_datos_contrato)
        print('\nDatos de viajero')
        print('------------------------------------------------------------------------------------------')
        datos_viajeros:List[DatosViajero] = cargar_datos_viajeros(ruta_datos_viajeros)
        print('------------------------------------------------------------------------------------------\n')
    else:
        print("No existen archivos compatibles")

    pregunta = input(f"Los datos vistos anteriormente son Correctos? Pulsa S/N -> ").upper()
    correcto = pregunta in ['S', 'SI']

print("\nSelecciona el titular del contrato entre los viajeros:")
for index, viajero in enumerate(datos_viajeros):
    print(f"{index+1} - {viajero.nombre} {viajero.primer_apellido} {viajero.segundo_apellido}")

# Solicitar selección al usuario
while True:
    try:
        num_titular = int(input("Introduce el número correspondiente al titular: ")) - 1
        if 0 <= num_titular < len(datos_viajeros):
            break
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
    except ValueError:
        print("Introduce un número válido.")

# Asignar rol TI al titular seleccionado, y VI a los demás
datos_viajeros[num_titular].rol = 'TI'


generar_xml(datos_establecimiento=datos_establecimientos[0], datos_contrato=datos_contratos[0], datos_viajeros=datos_viajeros)
