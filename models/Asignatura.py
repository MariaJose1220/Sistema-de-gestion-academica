class Asignatura:

     def __init__(self, codigo, nombre, NumCreditos, ProgramaAcademico):
          self.set_codigo(codigo)
          self.set_nombre(nombre)
          self.set_NumCreditos(NumCreditos)
          self.set_ProgramaAcademico(ProgramaAcademico)

     def get_codigo(self):
          return self._codigo

     def set_codigo(self, codigo):
        if(codigo != ""):
               self._codigo = codigo
        else:
               raise ValueError("El codigo no puede estar vacio")


     def get_nombre(self):
              return self._nombre
    
     def set_nombre(self, nombre):
            if(nombre != ""):
                   self._nombre = nombre
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
                if(ProgramaAcademico != ""):
                       self._ProgramaAcademico = ProgramaAcademico
                else:
                       raise ValueError("El programa academico no puede estar vacio")