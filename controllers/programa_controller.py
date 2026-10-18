from models.Programa import Programa

class ProgramaController:
    def __init__(self):
        self.programas=[]
        
    def añadir_programa(self, codigo, nombre, Facultad, NumeroSemestres):
        programa=Programa(codigo, nombre, Facultad, NumeroSemestres)
        self.programas.append(programa)
          
    def get_programa(self):
        return self.programas.copy()