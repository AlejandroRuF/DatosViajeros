import xml.etree.ElementTree as ET
import xml.dom.minidom
from typing import List

from classes.DatosContrato import DatosContrato
from classes.DatosEstablecimiento import DatosEstablecimiento
from classes.DatosViajeros import DatosViajero


def pretty_print_xml(root, xml_file):
    """Formatea un XML usando minidom sin perder namespaces y lo guarda correctamente."""

    # Convertir el árbol de elementos a una cadena de bytes con namespaces
    xml_str = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    # Reemplazar manualmente el namespace "ns0" con el namespace correcto
    xml_pretty = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")
    xml_pretty = xml_pretty.replace("ns0:", "").replace(":ns0", "")

    # Guardar el XML formateado correctamente
    with open(xml_file, "w", encoding="utf-8") as f:
        f.write(xml_pretty)

    print(f"✅ XML generado y formateado correctamente en: {xml_file}")


def generar_xml(datos_establecimiento: DatosEstablecimiento, datos_contrato: DatosContrato, datos_viajeros: List[DatosViajero]):
    namespace = "http://www.neg.hospedajes.mir.es/altaParteHospedaje"
    ET.register_namespace("", namespace)  # Registrar correctamente el namespace

    peticion = ET.Element("{%s}peticion" % namespace)  # Usar namespace en la raíz
    solicitud = ET.SubElement(peticion, "{%s}solicitud" % namespace)
    ET.SubElement(solicitud, 'codigoEstablecimiento').text = datos_establecimiento.codigo_establecimiento
    comunicacion = ET.SubElement(solicitud, "{%s}comunicacion" % namespace)

    contrato_xml = ET.SubElement(comunicacion, "{%s}contrato" % namespace)
    ET.SubElement(contrato_xml, "{%s}referencia" % namespace).text = datos_contrato.referencia_contrato
    ET.SubElement(contrato_xml, "{%s}fechaContrato" % namespace).text = datos_contrato.fecha_contrato.split(" ")[0]
    ET.SubElement(contrato_xml,
                  "{%s}fechaEntrada" % namespace).text = f"{datos_contrato.fecha_entrada.split(' ')[0]}T00:00:00"
    ET.SubElement(contrato_xml,
                  "{%s}fechaSalida" % namespace).text = f"{datos_contrato.fecha_salida.split(' ')[0]}T00:00:00"
    ET.SubElement(contrato_xml, "{%s}numPersonas" % namespace).text = str(datos_contrato.numero_personas)

    pago = ET.SubElement(contrato_xml, "{%s}pago" % namespace)
    ET.SubElement(pago, "{%s}tipoPago" % namespace).text = datos_contrato.tipo_pago
    ET.SubElement(pago, "{%s}fechaPago" % namespace).text = str(datos_contrato.fecha_pago).split(" ")[0]
    ET.SubElement(pago, "{%s}medioPago" % namespace).text = datos_contrato.medio_pago
    ET.SubElement(pago, "{%s}titular" % namespace).text = datos_contrato.titular_pago
    if datos_contrato.tipo_pago == 'TARJT':
        ET.SubElement(pago, "{%s}caducidadTarjeta" % namespace).text = str(datos_contrato.fecha_caducidad_tarjeta).split(" ")[0]

    for viajero in datos_viajeros:
        anyadir_viajero(comunicacion, viajero, namespace)

        if viajero.rol == 'TI':
            anyadir_viajero(comunicacion, viajero, namespace, 'TI')

    xml_file = "comunicacion.xml"

    # ✅ Pasar el XML correctamente formateado
    pretty_print_xml(peticion, xml_file)



def anyadir_viajero(comunicacion, viajero, namespace, rol='VI'):
    persona_viajero = ET.SubElement(comunicacion, "{%s}persona" % namespace)
    ET.SubElement(persona_viajero, "{%s}rol" % namespace).text = rol
    ET.SubElement(persona_viajero, "{%s}nombre" % namespace).text = viajero.nombre
    ET.SubElement(persona_viajero, "{%s}apellido1" % namespace).text = viajero.primer_apellido
    ET.SubElement(persona_viajero, "{%s}apellido2" % namespace).text = viajero.segundo_apellido
    ET.SubElement(persona_viajero, "{%s}tipoDocumento" % namespace).text = viajero.tipo_documento
    ET.SubElement(persona_viajero, "{%s}numeroDocumento" % namespace).text = viajero.numero_documento
    ET.SubElement(persona_viajero, "{%s}soporteDocumento" % namespace).text = viajero.soporte_documento
    ET.SubElement(persona_viajero, "{%s}fechaNacimiento" % namespace).text = viajero.fecha_nacimiento.split(" ")[0]
    ET.SubElement(persona_viajero, "{%s}nacionalidad" % namespace).text = viajero.codigo_nacionalidad

    direccion_xml = ET.SubElement(persona_viajero, "{%s}direccion" % namespace)
    ET.SubElement(direccion_xml, "{%s}direccion" % namespace).text = viajero.direccion

    if viajero.codigo_pais == 'ESP':
        ET.SubElement(direccion_xml, "{%s}codigoMunicipio" % namespace).text = viajero.codigo_municipio
    else:
        ET.SubElement(direccion_xml, "{%s}nombreMunicipio" % namespace).text = viajero.nombre_municipio

    ET.SubElement(direccion_xml, "{%s}codigoPostal" % namespace).text = viajero.codigo_postal
    ET.SubElement(direccion_xml, "{%s}pais" % namespace).text = viajero.codigo_pais

    ET.SubElement(persona_viajero, "{%s}telefono" % namespace).text = viajero.telefono
    if viajero.codigo_parentesco != '':
        ET.SubElement(persona_viajero, "{%s}parentesco" % namespace).text = viajero.codigo_parentesco
