from models.personas import Personas


class Administrativo(Personas):
    """Persona que desempeña un cargo en una dependencia de la universidad.

    Hereda de Personas la identificación, el nombre, el correo y sus
    validaciones. Aquí solo se agregan los datos propios del administrativo.
    """

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.set_numero_empleado(numero_empleado)
        self.set_dependencia(dependencia)
        self.set_cargo(cargo)
        self.set_jornada(jornada)

    def get_numero_empleado(self):
        return self._numero_empleado

    def set_numero_empleado(self, numero_empleado):
        if numero_empleado != "":
            self._numero_empleado = numero_empleado
        else:
            raise ValueError("El número de empleado no puede estar vacío")

    def get_dependencia(self):
        return self._dependencia

    def set_dependencia(self, dependencia):
        if dependencia != "":
            self._dependencia = dependencia
        else:
            raise ValueError("La dependencia no puede estar vacía")

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        if cargo != "":
            self._cargo = cargo
        else:
            raise ValueError("El cargo no puede estar vacío")

    def get_jornada(self):
        return self._jornada

    def set_jornada(self, jornada):
        if jornada != "":
            self._jornada = jornada
        else:
            raise ValueError("La jornada no puede estar vacía")

    def mostrar_informacion(self):
        return ("Tipo: Administrativo\n"
                f"{super().mostrar_informacion()}\n"
                f"Número de empleado: {self.get_numero_empleado()}\n"
                f"Dependencia: {self.get_dependencia()}\n"
                f"Cargo: {self.get_cargo()}\n"
                f"Jornada: {self.get_jornada()}")

    def realizar_actividad_principal(self):
        return (f"{self.get_nombre()} se desempeña como {self.get_cargo()} "
                f"en la dependencia {self.get_dependencia()}.")
