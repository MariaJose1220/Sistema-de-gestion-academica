from models.personas import Personas
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

class PersonaController:
    
    def __init__(self):
        self.personas = [] #se crea la lista
    
    def añadir_persona(self, identificacion, nombre, correo):
        persona=Personas(identificacion, nombre, correo)
        self.personas.append(persona)
        
    def añadir_estudiante(self, identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio):
        estudiante=Estudiante(identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio)
        self.personas.append(estudiante)
        
    def añadir_docente(self, identificacion, nombre, correo, num_empleado, facultad, tipo_contratacion, horas_semanales):
        docente=Docente(identificacion, nombre, correo, num_empleado, facultad, tipo_contratacion, horas_semanales)
        self.personas.append(docente)
        
    def añadir_administrativo(self, identificacion, nombre, correo, num_empleado, dependencia, cargo, jornada):
        administrativo=Administrativo(identificacion, nombre, correo, num_empleado, dependencia, cargo, jornada)
        self.personas.append(administrativo)
        
    def get_persona(self):
        return self.personas.copy()
        #devuelve una copia de la lista con todas las personas
        #inluyendo los tres tipos: estudiante, docente y administrativo 
