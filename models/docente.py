class Docente:

     def __init__(self, NumEmpleado, Facultad, Contratacion, Hsemanales):
          self.set_NumEmpleado(NumEmpleado)
          self.set_Facultad(Facultad)
          self.set_Contratacion(Contratacion)
          self.set_Hsemanales(Hsemanales)

     def get_NumEmpleado(self):
          return self._NumEmpleado

     def set_NumEmpleado(self, NumEmpleado):
        if(NumEmpleado != ""):
               self._NumEmpleado = NumEmpleado
        else:
               raise ValueError("El numero de empleado no puede estar vacio")


     def get_Facultad(self):
              return self._Facultad
    
     def set_Facultad(self, Facultad):
            if(Facultad != ""):
                   self._Facultad = Facultad
            else:
                   raise ValueError("La Facultad a la que pertenece el docente no puede estar vacia")


     def get_Contratacion(self):
              return self._Contratacion
    
     def set_Contratacion(self, Contratacion):
            if(Contratacion != ""):
                   self._Contratacion = Contratacion
            else:
                   raise ValueError("El tipo de Contratacion no puede estar vacia ")

     def get_Hsemanales(self):
                  return self._Hsemanales
        
     def set_Hsemanales(self, Hsemanales):
                if(Hsemanales > 0):
                       self._Hsemanales = Hsemanales
                else:
                       raise ValueError("El nuemro de horas semanales no puede ser menor o igual a cero")