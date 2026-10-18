from controllers.persona_controller import PersonaController
from controllers.programa_controller import ProgramaController
from models.personas import Personas

def mostrar_personas(persona_controller):
    personas = persona_controller.get_persona()
    print()
    if not personas:
        print("No existen personas registradas")
        return #se sale de la función
    
    for persona in personas:
        print(persona.mostrar_informacion())  
        print(persona.realizar_actividad_principal())
        print()

def elegir_programa (lista):
    print("Programa al que pertenece: ")
    for i, programa in enumerate(lista, start=1):
        print(f"{i}. {programa.get_nombre()}")
    while True:
        opcion = int(input("Elija una opción (el número): "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]

def elegir_persona (lista):
    print("Personas agregadas: ")
    for i, persona in enumerate(lista, start=1):
        print(f"{i}.{Personas.get_nombre(persona)}")
    while True:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]

def main():
    
    persona_controller = PersonaController()
    programa_controller = ProgramaController
    #asignatura_controller = AsignaturaController()
    
    while True:
            print("\n Opciones")
            print("1. Agregar programa académico")
            print("2. Agregar asignatura")
            print("3. Agregar estudiante")
            print("4. Agregar docente")
            print("5. Agregar administrativo")
            print("6. Mostrar programas académicos")
            print("7. Mostrar personas")
            print("8. Mostrar asignaturas")
            print("9. Cambiar correo de cualquier persona")
            print("10. Salir")
            
            option = input("Selecciona una opción: ")
            
            match option:
                 case "1":
                     codigo=input("Ingresa el código del programa: ")
                     nombre = input("Ingrese el nombre del programa: ")
                     facultad = input("Ingrese el nombre de la facultad: ")
                     semestres = int(input("Ingrese el número de semestres: "))
                    
                     programa_controller.añadir_programa(codigo, nombre, Facultad, NumeroSemestres)
                     print("Programa agregado con éxito")     
    
                 case "2":
                     if not programa_controller.get_programa():
                         print("Primero debe registrar al menos un programa académico.")
                         return
    
                 case "3":
                     if not programa_controller.get_programa():
                         print("Primero debe registrar al menos un programa académico.")
                         return
                     identificacion = input("Ingresa la identificación del estudiante: ")
                     nombre = input("Ingresa el nombre del estudiante: ")
                     correo = input("Ingrese el correo del estudiante: ")
                     codigo_estudiantil = input("Ingrese el código estudiantil del estudiante: ")
                     programa = elegir_programa(programa_controller.get_programa())
                     semestre = int(input("Ingrese el semestre en el que se encuentra: "))
                     promedio_acumulado = float(input("Ingrese el promedio acumulado: "))
                    
                     persona_controller.añadir_estudiante(identificacion, nombre, correo, codigo_estudiantil, """programa""", semestre, promedio_acumulado)
                     print("Estudiante agregado con éxito")
                    
                 case "4":
                    identificacion = input("Ingresa la identificación del docente: ")
                    nombre = input("Ingresa el nombre del docente: ")
                    correo = input("Ingrese el correo del docente: ")
                    NumEmpleado = input("Ingrese el número de empleado: ")
                    Facultad = input("Ingrese el nombre de la facultad: ")
                    Contratacion = input("Ingrese el tipo de contratación: ")
                    Hsemanales = int(input("Ingrese las horas semanales: "))
                    
                    persona_controller.añadir_docente(identificacion, nombre, correo, NumEmpleado, Facultad, Contratacion, Hsemanales)
                    print("Docente agregado con éxito")
                
                 case "5":
                    identificacion = input("Ingresa la identificación del administrativo: ")
                    nombre = input("Ingresa el nombre del administrativo: ")
                    correo = input("Ingrese el correo del administrativo: ")
                    numero_empleado = input("Ingrese el número de empleado: ")
                    dependencia = input("Ingrese la dependencia: ")
                    cargo = input("Ingrese el cargo: ")
                    jornada = input("Ingrese la jornada: ")
                    
                    persona_controller.añadir_administrativo(identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada)
                    print("Administrativo agregado con éxito")
    
                # case "6":
    
                 case "7":
                    mostrar_personas(persona_controller)
    
                #case "8":
                
                 case "9":
                    
                    if not persona_controller.get_persona():
                        print("No hay personas registradas")
                    else:
                        persona = elegir_persona(persona_controller.get_persona())
                        persona.set_correo(input("Ingrese el nuevo correo: "))
                        print()
                        print(f"Correo actual: {persona.get_correo()}")
                    
                 case "10":
                    print(f"Vuelve pronto \n")
                    break
                
                 case _:
                    print("Opción inválida")


if __name__ == "__main__":
    main()

