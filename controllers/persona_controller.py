
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

class PersonaController:
    
    def __init__(self):
        self.personas = [] #se crea la lista

    def añadir_estudiante(self, identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio_acumulado):
        estudiante=Estudiante(identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio_acumulado)
        self.personas.append(estudiante)
        
    def añadir_docente(self, identificacion, nombre, correo, NumEmpleado, Facultad, Contratacion, Hsemanales):
        docente=Docente(identificacion, nombre, correo, NumEmpleado, Facultad, Contratacion, Hsemanales)
        self.personas.append(docente)
        
    def añadir_administrativo(self, identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada):
        administrativo=Administrativo(identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada)
        self.personas.append(administrativo)
        
    def get_persona(self):
        return self.personas.copy()
        #devuelve una copia de la lista con todas las personas
        #inluyendo los tres tipos: estudiante, docente y administrativo 
