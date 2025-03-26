class DatosViajero:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, tipo_documento, numero_documento,
                 soporte_documento, telefono, codigo_pais, direccion, provincia,
                 codigo_municipio, nombre_municipio, codigo_postal, codigo_parentesco,codigo_nacionalidad, rol="VI" ):

        self.rol = rol
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.soporte_documento = soporte_documento  # Obligatorio para DNI/NIF/NIE
        self.codigo_nacionalidad = codigo_nacionalidad
        self.telefono = telefono
        self.codigo_pais = codigo_pais
        self.direccion = direccion
        self.provincia = provincia
        self.codigo_municipio = codigo_municipio  # Obligatorio si España
        self.nombre_municipio = nombre_municipio  # Obligatorio si NO España
        self.codigo_postal = codigo_postal
        self.codigo_parentesco = codigo_parentesco

    def __str__(self):
        municipio = self.codigo_municipio if self.codigo_pais == "ESP" else self.nombre_municipio
        return (f"Rol: {self.rol}, Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}, "
                f"Fecha Nacimiento: {self.fecha_nacimiento}, Tipo Documento: {self.tipo_documento}, "
                f"Nº Documento: {self.numero_documento}, Soporte Documento: {self.soporte_documento}, "
                f"Codigo de la nacionalidad: {self.codigo_nacionalidad}, "
                f"Teléfono: {self.telefono}, País: {self.codigo_pais}, "
                f"Dirección: {self.direccion}, Provincia: {self.provincia}, Municipio: {municipio}, "
                f"Código Postal: {self.codigo_postal}, Parentesco: {self.codigo_parentesco}")


