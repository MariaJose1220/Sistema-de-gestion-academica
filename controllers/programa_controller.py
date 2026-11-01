from models.programa import Programa
from models.excepciones import ProgramaNoEncontradoError

class ProgramaController:
    def __init__(self):
        self.programas=[]
        
    def añadir_programa(self, codigo, nombre, Facultad, NumeroSemestres):
        programa= Programa(codigo, nombre, Facultad, NumeroSemestres)
        self.programas.append(programa)
          
    def get_programa(self):
        return self.programas.copy()

    def buscar_programa(self, codigo):
        for programa in self.programas:
            if programa.get_codigo() == codigo:
                return programa

        raise ProgramaNoEncontradoError(
            "El programa académico buscado no encontrado."
        )

