class DatosViajero:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, tipo_documento, numero_documento,
                 telefono, correo_electronico, pais, codigo_pais, direccion, provincia, municipio, codigo_postal,
                 parentesco, codigo_parentesco):
        self.nombre = nombre  # String (Nombre del viajero)
        self.primer_apellido = primer_apellido  # String (Primer apellido)
        self.segundo_apellido = segundo_apellido  # String (Segundo apellido)
        self.fecha_nacimiento = fecha_nacimiento  # Fecha (Formato AAAA-MM-DD)
        self.tipo_documento = tipo_documento  # String (Tipo de documento, ej. DNI, Pasaporte)
        self.numero_documento = numero_documento  # String (Número de documento, ej. 12345678A)
        self.telefono = telefono  # String (Número de teléfono, ej. +34912345678)
        self.correo_electronico = correo_electronico  # String (Correo electrónico, ej. correo@dominio.com)
        self.pais = pais  # String (Nombre del país)
        self.codigo_pais = codigo_pais  # String (Código ISO 3166-1 del país, ej. ESP, USA)
        self.direccion = direccion  # String (Dirección completa, ej. Calle Ficticia, 123)
        self.provincia = provincia  # String (Provincia, ej. Madrid)
        self.municipio = municipio  # String (Municipio, ej. Alcázar de San Juan)
        self.codigo_postal = codigo_postal  # String (Código postal, ej. 28001)
        self.parentesco = parentesco  # String (Parentesco, ej. Hijo/a, Padre/Madre)
        self.codigo_parentesco = codigo_parentesco  # String (Código de parentesco, ej. HJ, PM)
