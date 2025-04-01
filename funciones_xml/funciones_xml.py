import xml.etree.ElementTree as ET
import xml.dom.minidom
from lxml import etree
from typing import List
from classes.DatosContrato import DatosContrato
from classes.DatosEstablecimiento import DatosEstablecimiento
from classes.DatosViajeros import DatosViajero

def generar_xml(datos_establecimiento: DatosEstablecimiento, datos_contrato: DatosContrato, datos_viajeros: List[DatosViajero]):
    nsmap = {"ns2": "http://www.neg.hospedajes.mir.es/altaParteHospedaje"}
    NS = nsmap["ns2"]

    # Crear raíz con prefijo ns2
    peticion = etree.Element("{%s}peticion" % NS, nsmap=nsmap)

    # Bloque solicitud
    solicitud = etree.SubElement(peticion, "{%s}solicitud" % NS)
    etree.SubElement(solicitud, "{%s}codigoEstablecimiento" % NS).text = datos_establecimiento.codigo_establecimiento
    comunicacion = etree.SubElement(solicitud, "{%s}comunicacion" % NS)

    # Bloque contrato
    contrato_xml = etree.SubElement(comunicacion, "{%s}contrato" % NS)
    etree.SubElement(contrato_xml, "{%s}referencia" % NS).text = datos_contrato.referencia_contrato
    etree.SubElement(contrato_xml, "{%s}fechaContrato" % NS).text = datos_contrato.fecha_contrato.split(" ")[0]
    etree.SubElement(contrato_xml, "{%s}fechaEntrada" % NS).text = f"{datos_contrato.fecha_entrada.split(' ')[0]}T00:00:00"
    etree.SubElement(contrato_xml, "{%s}fechaSalida" % NS).text = f"{datos_contrato.fecha_salida.split(' ')[0]}T00:00:00"
    etree.SubElement(contrato_xml, "{%s}numPersonas" % NS).text = str(datos_contrato.numero_personas)

    # Bloque pago
    pago = etree.SubElement(contrato_xml, "{%s}pago" % NS)
    etree.SubElement(pago, "{%s}tipoPago" % NS).text = datos_contrato.tipo_pago
    etree.SubElement(pago, "{%s}fechaPago" % NS).text = str(datos_contrato.fecha_pago).split(" ")[0]
    etree.SubElement(pago, "{%s}medioPago" % NS).text = datos_contrato.medio_pago
    etree.SubElement(pago, "{%s}titular" % NS).text = datos_contrato.titular_pago
    if datos_contrato.tipo_pago == 'TARJT':
        etree.SubElement(pago, "{%s}caducidadTarjeta" % NS).text = str(datos_contrato.fecha_caducidad_tarjeta).split(" ")[0]

    # Añadir viajeros
    for viajero in datos_viajeros:
        anyadir_viajero(comunicacion, viajero, NS)  # Siempre como VI
        if hasattr(viajero, 'rol') and viajero.rol == 'TI':
            anyadir_viajero(comunicacion, viajero, NS, rol='TI')  # También como TI si aplica

    # Guardar XML
    tree = etree.ElementTree(peticion)
    tree.write("comunicacion.xml", encoding="utf-8", xml_declaration=True, pretty_print=True)
    print("✅ XML generado correctamente como comunicacion.xml")


def anyadir_viajero(comunicacion, viajero, NS, rol='VI'):
    persona = etree.SubElement(comunicacion, f"{{{NS}}}persona")
    etree.SubElement(persona, f"{{{NS}}}rol").text = rol
    etree.SubElement(persona, f"{{{NS}}}nombre").text = viajero.nombre
    etree.SubElement(persona, f"{{{NS}}}apellido1").text = viajero.primer_apellido
    etree.SubElement(persona, f"{{{NS}}}apellido2").text = viajero.segundo_apellido
    etree.SubElement(persona, f"{{{NS}}}tipoDocumento").text = viajero.tipo_documento
    etree.SubElement(persona, f"{{{NS}}}numeroDocumento").text = viajero.numero_documento
    etree.SubElement(persona, f"{{{NS}}}soporteDocumento").text = viajero.soporte_documento
    etree.SubElement(persona, f"{{{NS}}}fechaNacimiento").text = viajero.fecha_nacimiento.split(" ")[0]
    etree.SubElement(persona, f"{{{NS}}}nacionalidad").text = viajero.codigo_nacionalidad

    direccion = etree.SubElement(persona, f"{{{NS}}}direccion")
    etree.SubElement(direccion, f"{{{NS}}}direccion").text = viajero.direccion
    if viajero.codigo_pais == 'ESP':
        etree.SubElement(direccion, f"{{{NS}}}codigoMunicipio").text = viajero.codigo_municipio
    else:
        etree.SubElement(direccion, f"{{{NS}}}nombreMunicipio").text = viajero.nombre_municipio

    etree.SubElement(direccion, f"{{{NS}}}codigoPostal").text = viajero.codigo_postal
    etree.SubElement(direccion, f"{{{NS}}}pais").text = viajero.codigo_pais

    etree.SubElement(persona, f"{{{NS}}}telefono").text = viajero.telefono
    if getattr(viajero, "codigo_parentesco", None):
        etree.SubElement(persona, f"{{{NS}}}parentesco").text = viajero.codigo_parentesco
