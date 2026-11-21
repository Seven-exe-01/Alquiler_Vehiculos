class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, correo):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__telefono=telefono
        self.__correo=correo

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
            return self.__apellido
    @property
    def dni(self):
            return self.__dni
    @property
    def telefono(self):
            return self.__telefono
    @property
    def correo(self):
            return self.__correo

    @staticmethod
    def control_dni(buscoDni, clientes):
        if not clientes:
            resultado=False
        else:
            resultado=False
            for c in clientes:
                if c.dni == buscoDni:
                    resultado=True
        return resultado