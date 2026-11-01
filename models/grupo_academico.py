from models.asignatura import Asignatura
from models.docente import Docente
from models.horario import Horario
from models.estudiante import Estudiante
from models.excepciones import EstudianteYaMatriculadoError,CapacidadMaximaError,EstudianteNoMatriculadoError

class GrupoAcademico:
    def __init__(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        self.set_codigo(codigo)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad_maxima(capacidad_maxima)
        self.estudiantes = [] #se crea una lista (inicialmente vacía) para gregar a todos los estudiantes del grupo
        # COMPOSICIÓN: el horario se crea aquí, como parte del grupo. No existe
        # por fuera de él: nace cuando se crea el grupo y le pertenece solo a él.
        self._horario = Horario(dia, hora_inicio, hora_fin, salon)
    
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
    
        
    def mostrar_informacion_grupo(self):
        return (f"Grupo académico\n"
                f"Código del grupo: {self.get_codigo()}\n"
                f"Asignatura ofrecida: {self.get_asignatura().get_nombreA()}\n"
                f"Docente responsable: {self.get_docente().get_nombre()}\n"
                f"Capacidad máxima: {self.get_capacidad_maxima()}\n"
                f"Número de estudiantes: {len(self.estudiantes)}\n"
                f"{self.get_horario().mostrar_información()}")
        
    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Solo se pueden matricular estudiantes en un grupo")
        for est in self.estudiantes:
            if est.get_identificacion()== estudiante.get_identificacion():

                raise EstudianteYaMatriculadoError(
                    f"El estudiante con identificación "
                    f"{estudiante.get_identificacion()} ya está matriculado."
                )
            
        if len(self.estudiantes) >= self.get_capacidad_maxima():
            raise CapacidadMaximaError(
            "El grupo alcanzó su capacidad máxima."
        )
        self.estudiantes.append(estudiante)
     

    def retirar_estudiante(self, codigo_estudiantil):
        for a in self.estudiantes:
            if a.get_codigo_estudiantil() == codigo_estudiantil:
                self.estudiantes.remove(a)
                return (
                    f"El estudiante {a.get_nombre()} (código {codigo_estudiantil}) "
                    f"fue retirado correctamente del grupo."
                    )
        raise EstudianteNoMatriculadoError(
        f"El estudiante con código {codigo_estudiantil} no está matriculado en el grupo."
          )

        
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes matriculados en el grupo.")
            return
        print("Estudiantes en el grupo: \n")
        for i, estudiante in enumerate(self.estudiantes, start=1):
            print(f"{i}. {estudiante.mostrar_informacion()}\n")
