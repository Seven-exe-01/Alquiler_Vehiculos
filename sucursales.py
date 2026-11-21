class Sucursal:
    def __init__(self, codigo, ciudad, direccion):
        self.codigo = codigo
        self.ciudad = ciudad
        self.direccion = direccion
        self.__vehiculos = []

    @property
    def vehiculos(self):
        return list(self.__vehiculos)

    def agregar_vehiculo(self, vehiculo):
        if vehiculo not in self.__vehiculos:
            self.__vehiculos.append(vehiculo)

    def remover_vehiculo(self, vehiculo):
        if vehiculo in self.__vehiculos:
            self.__vehiculos.remove(vehiculo)
        else:
            print("El vehiculo no pertenece a esta sucursal")

    @staticmethod
    def control_suc(buscoCodSuc, sucursales):
        if not sucursales:
            return False
        for c in sucursales:
            if int(c.codigo) == int(buscoCodSuc):
                return True
        return False