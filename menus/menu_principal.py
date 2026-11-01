from menus.menu_secundario import menu_grupo_academico
from menus.metodos import elegir_persona, mostrar_asignaturas, mostrar_personas, mostrar_programas, elegir_programa 
from demostracion import ejecutar_demostracion
from demostracion_ac2 import ejecutar_pruebas_ac2
from models.excepciones import (AsignaturaNoEncontradaError,ProgramaNoEncontradoError,SistemaAcademicoError
)

def agregar(
            persona_controller,
            programa_controller,
            asignatura_controller,
            grupo_controller
):
    while True:
        print("\nQue elemento desea agregar")
        print("1. Agregar programa académico")
        print("2. Agregar asignatura")
        print("3. Agregar estudiante")
        print("4. Agregar docente")
        print("5. Agregar administrativo")
        print("6. Agregar grupo académico")
        print("7. Volver al menu anterior")

        option = input("Selecciona una opción: ")
        
        match option:
           
           case "1":
              codigo=input("Ingresa el código del programa: ")
              nombre = input("Ingrese el nombre del programa: ")
              Facultad = input("Ingrese el nombre de la facultad: ")
              NumeroSemestres = int(input("Ingrese el número de semestres: "))
                            
              programa_controller.añadir_programa(codigo, nombre, Facultad, NumeroSemestres)
              print("Programa agregado con éxito")     
            
           case "2":
              if not programa_controller.get_programa():
                 print("Primero debe registrar al menos un programa académico.")
                 continue
              codigoA=input("Ingrese el código de la asignatura: ")
              nombreA=input("Ingrese el nombre de la asignatura: ")
              NumCreditos=int(input("Ingrese el número de créditos de la asignatura: "))
              ProgramaAcademico=elegir_programa(programa_controller.get_programa())
              asignatura_controller.añadir_asignatura(codigoA, nombreA, NumCreditos, ProgramaAcademico)
              print("Asignatura agregada con éxito")
              
           case "3":
               if not programa_controller.get_programa():
                    print("Primero debe registrar al menos un programa académico.")
                    continue
               identificacion = input("Ingresa la identificación del estudiante: ")
               nombre = input("Ingresa el nombre del estudiante: ")
               correo = input("Ingrese el correo del estudiante: ")
               codigo_estudiantil = input("Ingrese el código estudiantil del estudiante: ")
               programa = elegir_programa(programa_controller.get_programa())
               semestre = int(input("Ingrese el semestre en el que se encuentra: "))
               promedio_acumulado = float(input("Ingrese el promedio acumulado: "))
               persona_controller.añadir_estudiante(identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio_acumulado)
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
            
           case "6":
              menu_grupo_academico(grupo_controller, asignatura_controller, persona_controller)

           case "7":
              return

def mostrar (
   persona_controller,
   programa_controller,
   asignatura_controller,
):
   while True:
      
      print("\n Que elemento desea ver")
      print("1. Mostrar programas académicos")
      print("2. Mostrar personas")
      print("3. Mostrar asignaturas")
      print("4. Regresar al menú anterior")
      
      option = input("Selecciona una opción: ")
      
      match option:
             
             case "1":
                mostrar_programas(programa_controller)
                
             case "2":
                mostrar_personas(persona_controller)
       
             case "3":
               mostrar_asignaturas(asignatura_controller)
             case "4":
                return
             
def buscar (
   programa_controller,
   asignatura_controller,
):
   while True:
      print("\n Que elemento quiere buscar")
      print("1. Buscar asignatura " )
      print("2. Buscar programas académicos")
      print("3. Volver al menú anterior")
      
      option = input("Selecciona una opción: ")
      
      match option:
         
         case "1":
            codigo = input(
               "Ingrese el código de la asignatura a buscar: "
               )
            try:
               asignatura = asignatura_controller.buscar_asignatura(codigo)
               print(asignatura.mostrar_informacion())
            except AsignaturaNoEncontradaError as e:
               print(e)
               
         case "2":
            codigo = input(
               "Ingrese el código del programa académico a buscar: "
               )
            try:
               programa = programa_controller.buscar_programa(codigo)
               print(programa.mostrar_informacion())
            except ProgramaNoEncontradoError as e:
               print(e)
         case "3":
            return

def menu_principal(
    persona_controller,
    programa_controller,
    asignatura_controller,
    grupo_controller
):
    while True:
       print("\n Bienvenido a su sistema de gestión académica")
       print("\n Seleccione la función desea realizar")
       print("1. Agregar " )
       print("2. Mostrar")
       print("3. Buscar")
       print("4. Cambiar correo de cualquier persona")
       print("5. Ejecutar demostración AC1")
       print("6. Ejecutar pruebas AC2")
       print("7. Salir")
       
       option = input("Selecciona una opción: ")
            
            # Si un dato es inválido (correo vacío, semestres <= 0, letras donde va
            # un número...) se lanza ValueError: se avisa y el programa sigue.
       try:
          match option:
                     case "1":
                        agregar(
                           persona_controller,
                           programa_controller,
                           asignatura_controller,
                           grupo_controller
                           )
                     
                     case "2":
                        mostrar(
                           persona_controller,
                           programa_controller,
                           asignatura_controller
                           )
                        
                     case "3":
                        buscar(
                           programa_controller,
                           asignatura_controller
                           )
               
                     case "4":
                        if not persona_controller.get_persona():
                            print("No hay personas registradas")
                        else:
                            persona = elegir_persona(persona_controller.get_persona())
                            persona.set_correo(input("Ingrese el nuevo correo: "))
                            print()
                            print(f"Correo actual: {persona.get_correo()}")
                    
                     case "5":
                        ejecutar_demostracion()
                        
                     case "6":
                        ejecutar_pruebas_ac2()

                     case "7":
                        print(f"Vuelve pronto \n")
                        break
                
                     case _:
                        print("Opción inválida")
       except SistemaAcademicoError as error:
                print(f"[{type(error).__name__}] {error}")
       except ValueError as error:
                print(f"Dato inválido: {error}. No se guardaron los cambios.")
