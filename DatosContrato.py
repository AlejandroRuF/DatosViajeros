class DatosContrato:
    def __init__(self, referencia_contrato, fecha_contrato, fecha_entrada, fecha_salida, numero_personas,
                 tipo_pago, fecha_pago, medio_pago, titular_pago, fecha_caducidad_tarjeta):
        self.referencia_contrato = referencia_contrato  # String (Referencia del contrato)
        self.fecha_contrato = fecha_contrato  # Fecha (Formato AAAA-MM-DD)
        self.fecha_entrada = fecha_entrada  # Fecha (Formato AAAA-MM-DD)
        self.fecha_salida = fecha_salida  # Fecha (Formato AAAA-MM-DD)
        self.numero_personas = numero_personas  # Integer (Número de personas)
        self.tipo_pago = tipo_pago  # String (Tipo de pago, por ejemplo "EFECTIVO", "TARJETA", etc.)
        self.fecha_pago = fecha_pago  # Fecha (Formato AAAA-MM-DD)
        self.medio_pago = medio_pago  # String (Método de pago como "tarjeta", "efectivo", etc.)
        self.titular_pago = titular_pago  # String (Nombre del titular del pago)
        self.fecha_caducidad_tarjeta = fecha_caducidad_tarjeta  # String (MM/AAAA, por ejemplo "12/2025")

    def __str__(self):
        return f"Referencia del Contrato: {self.referencia_contrato}\n" \
               f"Fecha de Contrato: {self.fecha_contrato}\n" \
               f"Fecha de Entrada: {self.fecha_entrada}\n" \
               f"Fecha de Salida: {self.fecha_salida}\n" \
               f"Número de Personas: {self.numero_personas}\n" \
               f"Tipo de Pago: {self.tipo_pago}\n" \
               f"Fecha de Pago: {self.fecha_pago}\n" \
               f"Medio de Pago: {self.medio_pago}\n" \
               f"Titular del Pago: {self.titular_pago}\n" \
               f"Fecha de Caducidad de la Tarjeta: {self.fecha_caducidad_tarjeta}"
