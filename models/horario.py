
class Horario:
    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.set_dia(dia)
        self.set_hora_inicio(hora_inicio)
        self.set_hora_fin(hora_fin)
        self.set_salon(salon)

    def get_dia(self):
        return self._dia

    def set_dia(self, dia):
        if dia != "":
            self._dia = dia
        else:
            raise ValueError("El día no puede ser vacío")
            
    def get_hora_inicio(self):
        return self._hora_inicio
    
    def set_hora_inicio(self, hora_inicio):
        if hora_inicio != "":
            self._hora_inicio = hora_inicio
        else:
            raise ValueError("La hora de inicio no puede ser vacía")
            
    def get_hora_fin(self):
        return self._hora_fin
    
    def set_hora_fin(self, hora_fin):
        if hora_fin != "":
            self._hora_fin = hora_fin
        else:
            raise ValueError("La hora de finalización no puede ser vacía")
    
    def get_salon(self):
        return self._salon 
    
    def set_salon(self, salon):
        if salon != "":
            self._salon = salon
        else: 
            raise ValueError ("El salón no puede ser vacío")
        
    def mostrar_información(self):
        return (f"Horario\n"
                f"Día: {self.get_dia()}\n"
                f"Hora de inicio: {self.get_hora_inicio()}\n"
                f"Hora de finalización: {self.get_hora_fin()}\n"
                f"Salón: {self.get_salon()}")