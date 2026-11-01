from models.grupo_academico import GrupoAcademico

class GrupoAcademicoController:
    def __init__(self):
        self.grupos = []
        
    def añadir_grupo(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        grupo=GrupoAcademico(codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon)
        self.grupos.append(grupo)
        
    def get_grupos(self):
        return self.grupos.copy()
