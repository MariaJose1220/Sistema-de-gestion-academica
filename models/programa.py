class Programa:

     def __init__(self, codigo, nombre, Facultad, NumeroSemestres):
          self.set_codigo(codigo)
          self.set_nombre(nombre)
          self.set_Facultad(Facultad)
          self.set_NumeroSemestres(NumeroSemestres)

     def get_codigo(self):
          return self._codigo

     def set_codigo(self, codigo):
        if(codigo != ""):
               self._codigo = codigo
        else:
               raise ValueError("El codigo no puede estar vacío")
        
     def get_Facultad(self):
                     return self._Facultad
       
     def set_Facultad(self, Facultad):
              if(Facultad != ""):
                     self._Facultad = Facultad
              else:
                     raise ValueError("La Facultad a la que pertenece el programa no puede estar vacía")

     def get_nombre(self):
              return self._nombre
    
     def set_nombre(self, nombre):
            if(nombre != ""):
                   self._nombre = nombre
            else:
                   raise ValueError("El nombre del programa no puede estar vacío")

     def get_NumeroSemestres(self):
                  return self._NumeroSemestres
        
     def set_NumeroSemestres(self, NumeroSemestres):
                if(NumeroSemestres > 0):
                       self._NumeroSemestres = NumeroSemestres
                else:
                       raise ValueError("El número de semestres debe ser mayor a cero")

     def mostrar_informacion(self):
            return ("Programa Académico\n"
                   f"Código del programa: {self.get_codigo()}\n"
                   f"Nombre del programa: {self.get_nombre()}\n"
                   f"Facultad: {self.get_Facultad()}\n"
                   f"Numero de semestres: {self.get_NumeroSemestres()}\n")

