from tareas import trabajoPractico
from mailAutomation import EmailSender


class usuario():
    def __init__(self,id,nombre,apellido,password,correo,edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.correo = correo
        self.edad = edad

class profesor(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,especialidad):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.especialidad = especialidad
        self.beneficios = []

    def asignarTarea(self,estudiante,tarea):
        estudiante.tareas.append(tarea)
        
        email = EmailSender(self.correo, self.password)
        email.enviar_mail(
            destinatario=estudiante.correo,
            asunto=f"Nueva tarea asignada: {tarea.descripcion}",
            mensaje=f"""Hola {estudiante.nombre}
Se te ha asignado una nueva tarea:
Descripción: {tarea.descripcion}


"""
        )
        print(f"Tarea asignada y notificación enviada a {estudiante.nombre}")


    def chequearEntrega(self,estudiante,tarea):
        for t in estudiante.tareas:
            if t == tarea:
                print(f"La tarea '{t.descripcion}' ha sido marcada como entregada: {t.entrega}")
    def aprobarTarea(self,estudiante,tarea):
        for t in estudiante.tareas:
            if t == tarea:
                estudiante.coins=tarea.valor
                t.aprobado=True

                email = EmailSender(self.correo, self.password)
                email.enviar_mail(
                    destinatario=estudiante.correo,
                    asunto=f"aprobaste la tarea {tarea.descripcion}",
                    mensaje=f"felicidades {estudiante.nombre}\n\n"
                           f"Tu tarea '{tarea.descripcion} fue aprobada.\n"
                           f"conseguiste {tarea.valor} coins.\n"
                           f"Total de monedas: {estudiante.coins}\n\n"
                           f"ATT:profesor {self.nombre} {self.apellido}"
                )
                print(f"El estudiante {estudiante.nombre} posee {estudiante.coins} coins")
                print(f"el estudiante recibio el mail{estudiante.nombre}")
            print(f"El estudiante {estudiante.nombre} posee {estudiante.coins} coins")
        
class estudiante(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,curso,legajo,coins=0):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.curso = curso
        self.legajo = legajo
        self.coins = coins
        self.tareas = []

    def entregarTarea(self,tarea):
        for t in self.tareas:
            if t == tarea:
                t.entrega = True

    def chequeartareas(self):
        for t in self.tareas:
            trabajoPractico.mostrarInfo(t)

    def canjearbeneficio(self, beneficio,profesor):
        costo = beneficio.costo
        

        if self.coins >=costo:
            self.coins = self.coins - costo
            profesor.beneficios.append((self.nombre, beneficio.nombre))
            print(f"{self.nombre} canjeó el beneficio '{beneficio.nombre}' por {costo} coins.")
            print(f"Monedas restantes: {self.coins}")







