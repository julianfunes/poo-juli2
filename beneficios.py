from mailAutomation import EmailSender
from usuario import profesor, estudiante

class beneficios():
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
    

class cambiarFecha(beneficios):
    def __init__(self, costo=10):
        super().__init__("Cambio de fecha de entrega", costo)

class puntosExtra(beneficios):
    def __init__(self, puntos=1, costo=15):
        super().__init__(f"Puntos extra ({puntos})", costo)
        self.puntos = puntos

class faltaTutorias(beneficios):
    def __init__(self,  costo=20):
        super().__init__(f"Tutoría ({costo} de la falta)", costo)

    