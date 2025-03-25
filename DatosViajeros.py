class DatosViajero:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, tipo_documento, numero_documento,
                 telefono, correo_electronico, codigo_pais, direccion, provincia, municipio, codigo_postal,
                 codigo_parentesco):

        self.nombre = nombre  # String (Nombre del viajero)
        self.primer_apellido = primer_apellido  # String (Primer apellido)
        self.segundo_apellido = segundo_apellido  # String (Segundo apellido)
        self.fecha_nacimiento = fecha_nacimiento  # Fecha (Formato AAAA-MM-DD)
        self.tipo_documento = tipo_documento  # String (Tipo de documento, ej. DNI, Pasaporte)
        self.numero_documento = numero_documento  # String (Número de documento, ej. 12345678A)
        self.telefono = telefono  # String (Número de teléfono, ej. +34912345678)
        self.correo_electronico = correo_electronico  # String (Correo electrónico, ej. correo@dominio.com)
        self.codigo_pais = codigo_pais  # String (Código ISO 3166-1 del país, ej. ESP, USA)
        self.direccion = direccion  # String (Dirección completa, ej. Calle Ficticia, 123)
        self.provincia = provincia  # String (Provincia, ej. Madrid)
        self.municipio = municipio  # String (Municipio, ej. Alcázar de San Juan)
        self.codigo_postal = codigo_postal  # String (Código postal, ej. 28001)
        self.codigo_parentesco = codigo_parentesco  # String (Código de parentesco, ej. HJ, PM)

    def __str__(self):
        return f"Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}, " \
               f"Fecha de nacimiento: {self.fecha_nacimiento}, Tipo de documento: {self.tipo_documento}, " \
               f"Número de documento: {self.numero_documento}, Teléfono: {self.telefono}, " \
               f"Correo electrónico: {self.correo_electronico}, País: {self.codigo_pais}, " \
               f"Dirección: {self.direccion}, Provincia: {self.provincia}, Municipio: {self.municipio}, " \
               f"Código postal: {self.codigo_postal}, Parentesco: {self.codigo_parentesco}"

