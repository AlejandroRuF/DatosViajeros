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

