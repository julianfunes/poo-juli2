class Tarea():
    def __init__(self,valor,descripcion,consigna,fechaEntrega,criterioEvaluacion):
        self.valor = valor
        self.descripcion = descripcion
        self.consigna=consigna
        self.fechaEntrega=fechaEntrega
        self.criterioEvaluacion=criterioEvaluacion
        #Clase día 27/10
        self.entrega=False
        self.aprobado=False

class trabajoPractico(Tarea):
    def __init__(self,consigna,fechaEntrega,criterioEvaluacion):
        descripcion = "Trabajo Practico"
        valor = 200
        super().__init__(valor,descripcion,consigna,fechaEntrega,criterioEvaluacion)
        
class proyectoExtra(Tarea):
        def __init__(self,consigna,fechaEntrega,criterioEvaluacion):
            descripcion = "Proyecto Extra"
            valor = 1000
            super().__init__(valor,descripcion,consigna,fechaEntrega,criterioEvaluacion)