from models.Asignatura import Asignatura
from models.docente import Docente
from models.horario import Horario

class GrupoAcademico:
    def __init__(self, codigo, asignatura, docente, capacidad_maxima, horario):
        self.set_codigo(codigo)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad_maxima(capacidad_maxima)
        self.estudiantes = [] #se crea una lista (inicialmente vacía) para gregar a todos los estudiantes del grupo
        self.set_horario(horario)
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo):
        if codigo != "":
            self._codigo = codigo
        else: 
            raise ValueError("El código del grupo no puede ser vacío")
    
    def get_asignatura(self):
        return self._asignatura
    
    def set_asignatura(self, asignatura):
            if isinstance(asignatura,Asignatura):
                self._asignatura = asignatura
            else: 
                raise ValueError("La asignatura ofrecida debe ser un objeto existente")
    
    def get_docente(self):
        return self._docente
    
    def set_docente(self, docente):
        if isinstance(docente, Docente):
            self._docente = docente
        else: 
            raise ValueError("El docente responsable debe ser un objeto existente")
        
    def get_capacidad_maxima(self):
        return self._capacidad_maxima
    
    def set_capacidad_maxima(self, capacidad_maxima):
        if capacidad_maxima >0:
            self._capacidad_maxima = capacidad_maxima
        else: 
            raise ValueError("La capacidad máxima debe ser un número positivo")
        
    def get_horario(self):
        return self._horario
    
    def set_horario(self, horario):
        if isinstance(horario, Horario):
            self._horario = horario
        else: 
            raise ValueError("El horario debe ser un objeto existente")