from enums import TipoVehiculo, EstadoVehiculo


class Vehiculo:
    def __init__(self, patente, marca, modelo, tarifa, estado, tipo, sucursal):
        if tarifa <= 0:
            raise ValueError("La tarifa base por dia debe ser mayor que cero.")
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__tarifa = tarifa
        self.__estado = estado
        self.__tipo = tipo
        self.__sucursal = sucursal

    @property
    def patente(self):
        return self.__patente

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def tarifa(self):
        return self.__tarifa

    @property
    def estado(self):
        return self.__estado

    @property
    def tipo(self):
        return self.__tipo

    @property
    def sucursal(self):
        return self.__sucursal

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    @sucursal.setter
    def sucursal(self, nueva_sucursal):
        self.__sucursal = nueva_sucursal

    @tarifa.setter
    def tarifa(self, nueva_tarifa):
        if nueva_tarifa <= 0:
            raise ValueError("La tarifa base por dia debe ser mayor que cero.")
        self.__tarifa = nueva_tarifa

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("La cantidad de dias debe ser mayor que cero.")
        total = self.__tarifa * dias
        if total < 0:
            raise ValueError("El costo total no puede ser negativo.")
        return total

    @staticmethod
    def control_pat(buscoPatente, vehiculos):
        if not vehiculos:
            return False
        for c in vehiculos:
            if c.patente == buscoPatente:
                return True
        return False

    @staticmethod
    def buscar_pat(buscoPatente, vehiculos):
        if not vehiculos:
            return None
        for patenteing in vehiculos:
            if patenteing.patente == buscoPatente:
                return patenteing
        return None


class Auto(Vehiculo):
    def __init__(self, patente, marca, modelo, tarifa, estado, sucursal):
        super().__init__(patente, marca, modelo, tarifa, estado, TipoVehiculo.AUTO, sucursal)

    def calcular_costo(self, dias):
        return super().calcular_costo(dias)


class Camioneta(Vehiculo):
    def __init__(self, patente, marca, modelo, tarifa, estado, sucursal):
        super().__init__(patente, marca, modelo, tarifa, estado, TipoVehiculo.CAMIONETA, sucursal)

    def calcular_costo(self, dias):
        base = super().calcular_costo(dias)
        total = base * 1.20
        if total < 0:
            raise ValueError("El costo total no puede ser negativo.")
        return total


class Moto(Vehiculo):
    def __init__(self, patente, marca, modelo, tarifa, estado, sucursal):
        super().__init__(patente, marca, modelo, tarifa, estado, TipoVehiculo.MOTO, sucursal)

    def calcular_costo(self, dias):
        base = super().calcular_costo(dias)
        total = base * 0.85
        if total < 0:
            raise ValueError("El costo total no puede ser negativo.")
        return total