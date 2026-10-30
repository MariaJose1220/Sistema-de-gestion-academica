from models.horario import Horario

class HorarioController:
    def __init__(self):
        self.horarios = []
        
    def añadir_horario(self, dia, hora_inicio, hora_fin, salon):
        horario=Horario(dia, hora_inicio, hora_fin, salon)    
        self.horarios.append(horario)
        
    def get_horario(self):
        return self.horarios.copy()
    