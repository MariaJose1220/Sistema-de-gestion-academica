from menus.metodos import agregar_grupo, elegir_estudiante, elegir_grupo, mostrar_grupos
from models.excepciones import CapacidadMaximaError, EstudianteNoMatriculadoError, EstudianteYaMatriculadoError


def menu_grupo_academico(grupo_controller, asignatura_controller, persona_controller):
    
    while True:
        print("\n Nuevo grupo académico")
        print("1. Agregar un grupo académico (con su horario)")
        print("2. Matricular un estudiante")
        print("3. Retirar un estudiante")
        print("4. Mostrar estudiantes matriculados")
        print("5. Mostrar grupos académicos y sus horarios")
        print("6. Salir")
            
        option = input("Selecciona una opción: ")
        match option: 
            case "1":
                agregar_grupo(grupo_controller, asignatura_controller, persona_controller)
                
            case "2":
                if not grupo_controller.get_grupos():
                    print("Primero debe registrar al menos un grupo académico.")
                    continue
                grupo=elegir_grupo(grupo_controller.get_grupos())
                estudiante=elegir_estudiante(persona_controller.get_persona())
                try:
                    grupo.matricular_estudiante(estudiante)
                    print("Estudiante matriculado con éxito")
                except EstudianteYaMatriculadoError as e:
                    print(e)
                except CapacidadMaximaError as e:
                    print(e)
            
            case "3":
                  if not grupo_controller.get_grupos():
                      print("Primero debe registrar al menos un grupo académico.")
                      continue
                  grupo = elegir_grupo(grupo_controller.get_grupos())
                  estudiante = elegir_estudiante(
                      persona_controller.get_persona()
                      )
                  try:
                      mensaje = grupo.retirar_estudiante(estudiante.get_codigo_estudiantil())
                      print(mensaje)
                  except EstudianteNoMatriculadoError as e:
                      print(e)
                
            case "4":
                if not grupo_controller.get_grupos():
                    print("Primero debe registrar al menos un grupo académico.")
                    continue
                grupo=elegir_grupo(grupo_controller.get_grupos())
                grupo.mostrar_estudiantes()
            
            case "5":
                mostrar_grupos(grupo_controller)
            
            case "6":
                return
