from models.Asignatura import Asignatura

class AsignaturaController:
    def __init__(self):
        self.asignaturas=[]
        
    def añadir_asignatura(self, codigoA, nombreA, NumCreditos, ProgramaAcademico):
        asignatura = Asignatura(codigoA, nombreA, NumCreditos, ProgramaAcademico)
        self.asignaturas.append(asignatura)
        
    def get_asignatura(self):
        return self.asignaturas.copy()