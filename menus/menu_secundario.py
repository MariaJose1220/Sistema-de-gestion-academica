from menus.metodos import agregar_grupo, agregar_horario, elegir_estudiante, elegir_grupo, mostrar_horarios
from models.excepciones import CapacidadMaximaError, EstudianteNoMatriculadoError, EstudianteYaMatriculadoError


def menu_grupo_academico(horario_controller, grupo_controller, asignatura_controller, persona_controller):
    
    while True:
        print("\n Nuevo grupo académico")
        print("1. Agregar un horario")
        print("2. Agregar un grupo académico")
        print("3. Matricular un estudiante")
        print("4. Retirar un estudiante")
        print("5. Mostrar estudiantes matriculados")
        print("6. Mostrar horarios")
        print("7. Salir")
            
        option = input("Slecciona una opción: ")
        match option: 
            case "1":
                agregar_horario(horario_controller)

            case "2":
                agregar_grupo(grupo_controller, horario_controller, asignatura_controller, persona_controller)
                
            case "3":
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
            
            case "4":
                  if not grupo_controller.get_grupos():
                      print("Primero debe registrar al menos un grupo académico.")
                      continue
                  grupo = elegir_grupo(grupo_controller.get_grupos())
                  estudiante = elegir_estudiante(
                      persona_controller.get_persona()
                      )
                  try:
                      mensaje = grupo.retirar_estudiante(estudiante)
                      print(mensaje)
                  except EstudianteNoMatriculadoError as e:
                      print(e)
                
            case "5":
                if not grupo_controller.get_grupos():
                    print("Primero debe registrar al menos un grupo académico.")
                    continue
                grupo=elegir_grupo(grupo_controller.get_grupos())
                grupo.mostrar_estudiantes()
            
            case "6":
                mostrar_horarios(horario_controller)
            
            case "7":
                return