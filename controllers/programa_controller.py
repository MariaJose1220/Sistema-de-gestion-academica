from models.Programa import Programa


class ProgramaController:
    
    def __init__(self):
        self.personas = [] #se crea la lista con los programas academicos

    def añadir_programa(self, codigo, nombre, Facultad, NumeroSemestres):
        programa=programa(codigo, nombre, Facultad, NumeroSemestres)
        self.personas.append(programa)
        
    def get_programa(self):
        return self.programa.copy()
        #devuelve una copia de la lista con todas los programas ingresados