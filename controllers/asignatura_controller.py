from models.asignatura import Asignatura
from models.excepciones import AsignaturaNoEncontradaError

class AsignaturaController:
    def __init__(self):
        self.asignaturas=[]
        
    def añadir_asignatura(self, codigoA, nombreA, NumCreditos, ProgramaAcademico):
        asignatura = Asignatura(codigoA, nombreA, NumCreditos, ProgramaAcademico)
        self.asignaturas.append(asignatura)
        
    def get_asignatura(self):
        return self.asignaturas.copy()

    def buscar_asignatura(self, codigo):
        for asignatura in self.asignaturas:
            if asignatura.get_codigoA() == codigo:
                return asignatura
            raise AsignaturaNoEncontradaError(
            f"No existe una asignatura con código {codigo}"
        )
