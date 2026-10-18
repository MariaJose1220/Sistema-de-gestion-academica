from models.Programa import Programa

class Asignatura:

     def __init__(self, codigoA, nombreA, NumCreditos, ProgramaAcademico):
          self.set_codigo(codigoA)
          self.set_nombreA(nombreA)
          self.set_NumCreditos(NumCreditos)
          self.set_ProgramaAcademico(ProgramaAcademico)

     def get_codigoA(self):
          return self._codigoA

     def set_codigo(self, codigoA):
        if(codigoA != ""):
               self._codigoA = codigoA
        else:
               raise ValueError("El codigo no puede estar vacio")

     def get_nombreA(self):
              return self._nombreA
    
     def set_nombreA(self, nombreA):
            if(nombreA != ""):
                   self._nombreA = nombreA
            else:
                   raise ValueError("La nombre de la asignatura no puede estar vacio")

     def get_NumCreditos(self):
              return self._NumCreditos
    
     def set_NumCreditos(self, NumCreditos):
            if(NumCreditos > 0):
                   self._NumCreditos = NumCreditos
            else:
                   raise ValueError("El Numero de Creditos debe ser mayor a cero")

     def get_ProgramaAcademico(self):
                  return self._ProgramaAcademico
        
     def set_ProgramaAcademico(self, ProgramaAcademico):
                if isinstance (ProgramaAcademico, Programa): #toma el objeto de la calse programa
                       self._ProgramaAcademico = ProgramaAcademico
                else:
                       raise ValueError("La asignatura debe pertenecer a un programa académico existente")

     def mostrar_informacion(self):
            return ("Agisnatura\n"
                   f"Código de la Asignatura: {self.get_codigoA()}\n"
                   f"Nombre de la Asignatura: {self.get_nombreA()}\n"
                   f"Numero de Creditos: {self.get_NumCreditos()}\n"
                   f"Programa academico: {self.get_ProgramaAcademico().get_nombre()}\n")