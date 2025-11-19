from beneficios import faltaTutorias, puntosExtra, cambiarFecha , beneficios
from usuario import profesor, estudiante
from tareas import trabajoPractico

estudiante1 = estudiante(nombre="julian",
                          apellido="Funes",
                            edad=22, 
                            legajo=1234, 
                            curso="4to año", 
                            correo="jfunescarcano@escuelasproa.edu.ar", 
                            password="", 
                            id=1)

profesor1 = profesor(nombre="nacho", 
                     apellido="sanchez", 
                     edad=40, 
                     especialidad="Matematica", 
                     correo="pepo008400@gmail.com", 
                     password="ygaz tqdj sbed vmsi", 
                     id=1)

tarea1= trabajoPractico(consigna="esto es una consigna de Tarea1", 
                        fechaEntrega="12/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico")

beneficio1= cambiarFecha()

profesor1.asignarTarea(estudiante1, tarea1)

estudiante1.entregarTarea(tarea1)

profesor1.aprobarTarea(estudiante1, tarea1)

estudiante1.canjearbeneficio(beneficio1, profesor1)

print (profesor1.beneficios)

