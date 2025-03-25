class DatosEstablecimiento:
    def __init__(self, nombre_establecimiento, codigo_establecimiento, tipo_establecimiento, direccion, provincia,
                 municipio, codigo_postal, pais, telefono, correo_electronico):
        self.nombre_establecimiento = nombre_establecimiento  # String (Nombre del establecimiento)
        self.codigo_establecimiento = codigo_establecimiento  # String (Código del establecimiento)
        self.tipo_establecimiento = tipo_establecimiento  # String (Tipo de establecimiento, como "hotel", "casa rural", etc.)
        self.direccion = direccion  # String (Dirección completa)
        self.provincia = provincia  # String (Provincia)
        self.municipio = municipio  # String (Municipio)
        self.codigo_postal = codigo_postal  # String (Código postal)
        self.pais = pais  # String (Código ISO 3166-1 del país, por ejemplo, "ESP" para España)
        self.telefono = telefono  # String (Número de teléfono)
        self.correo_electronico = correo_electronico  # String (Correo electrónico)

    def __str__(self):
        return f"Establecimiento: {self.nombre_establecimiento}\n" \
               f"Código: {self.codigo_establecimiento}\n" \
               f"Tipo: {self.tipo_establecimiento}\n" \
               f"Dirección: {self.direccion}\n" \
               f"Provincia: {self.provincia}\n" \
               f"Municipio: {self.municipio}\n" \
               f"Código Postal: {self.codigo_postal}\n" \
               f"País: {self.pais}\n" \
               f"Teléfono: {self.telefono}\n" \
               f"Correo Electrónico: {self.correo_electronico}"
