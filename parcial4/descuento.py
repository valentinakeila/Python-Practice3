class Descuento():

    __descuento_comunidad = 0.30

    @staticmethod
    def pago_con_comunidad(monto_final: float):
        return monto_final - (monto_final * Descuento.__descuento_comunidad)