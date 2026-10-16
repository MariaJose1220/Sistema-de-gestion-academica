from models.personas import Personas


class Estudiante(Personas):
    """Persona que cursa un programa académico.

    Hereda de Personas la identificación, el nombre, el correo y sus
    validaciones. Aquí solo se agregan los datos propios del estudiante.
    """

    def __init__(self, identificacion, nombre, correo,
                 codigo_estudiantil, programa, semestre, promedio_acumulado):
        # super() ejecuta el constructor de Personas: los datos comunes
        # se inicializan y validan allí, sin repetir ese código.
        super().__init__(identificacion, nombre, correo)
        self.set_codigo_estudiantil(codigo_estudiantil)
        self.set_programa(programa)
        self.set_semestre(semestre)
        self.set_promedio_acumulado(promedio_acumulado)

    def get_codigo_estudiantil(self):
        return self._codigo_estudiantil

    def set_codigo_estudiantil(self, codigo_estudiantil):
        if codigo_estudiantil != "":
            self._codigo_estudiantil = codigo_estudiantil
        else:
            raise ValueError("El código estudiantil no puede estar vacío")

    def get_programa(self):
        return self._programa

    def set_programa(self, programa):
        # Se guarda el OBJETO ProgramaAcademico (no solo su nombre),
        # para poder consultar cualquiera de sus datos.
        if programa is not None:
            self._programa = programa
        else:
            raise ValueError("El estudiante debe pertenecer a un programa académico")

    def get_semestre(self):
        return self._semestre

    def set_semestre(self, semestre):
        if semestre > 0:
            self._semestre = semestre
        else:
            raise ValueError("El semestre debe ser mayor que cero")

    def get_promedio_acumulado(self):
        return self._promedio_acumulado

    def set_promedio_acumulado(self, promedio_acumulado):
        if 0 <= promedio_acumulado <= 5:
            self._promedio_acumulado = promedio_acumulado
        else:
            raise ValueError("El promedio acumulado debe estar entre 0.0 y 5.0")

    def mostrar_informacion(self):
        # Sobrescritura: reutiliza los datos generales de Personas
        # y les agrega los datos propios del estudiante.
        return ("Tipo: Estudiante\n"
                f"{super().mostrar_informacion()}\n"
                f"Código estudiantil: {self.get_codigo_estudiantil()}\n"
                f"Programa: {self.get_programa().get_nombre()}\n"
                f"Semestre: {self.get_semestre()}\n"
                f"Promedio acumulado: {self.get_promedio_acumulado():.2f}")

    def realizar_actividad_principal(self):
        return (f"{self.get_nombre()} cursa el programa "
                f"{self.get_programa().get_nombre()} y se encuentra en el "
                f"semestre {self.get_semestre()}.")
