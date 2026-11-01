from models.docente import Docente
from models.estudiante import Estudiante
from models.grupo_academico import GrupoAcademico


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

def mostrar_programas(programa_controller):
    programas = programa_controller.get_programa()
    print()
    if not programas:
        print("No existen programas registrados")
        return
    for programa in programas:
        print(programa.mostrar_informacion())
        print()
        
def mostrar_asignaturas(asignatura_controller):
    asignaturas = asignatura_controller.get_asignatura()
    print()
    if not asignaturas:
        print("No existen asignaturas registradas")
        return
    for asignatura in asignaturas:
        print(asignatura.mostrar_informacion())
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
        print(f"{i}. {persona.get_nombre()}")
    while True:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]

def elegir_grupo (lista):
    print("Grupos guardados: ")
    for i, g in enumerate(lista, start=1):
        print(f"{i}. Código:{GrupoAcademico.get_codigo(g)} - Asignatura: {GrupoAcademico.get_asignatura(g).get_nombreA()}")
    while True:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]

def elegir_estudiante (lista):
    # Se filtra primero, para que el número mostrado coincida con el objeto elegido
    lista = [e for e in lista if isinstance(e, Estudiante)]
    print("Estudiantes guardados: ")
    for i, e in enumerate(lista, start=1):
            print(f"  {i}. Nombre: {Estudiante.get_nombre(e)} - Código estudiantil: {Estudiante.get_codigo_estudiantil(e)}")
    while True:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]
        
def elegir_docente (lista):
    # Se filtra primero, para que el número mostrado coincida con el objeto elegido
    lista = [d for d in lista if isinstance(d, Docente)]
    print("Docente responsable: ")
    for i, docente in enumerate(lista, start=1):
            print(f"  {i}. Nombre: {Docente.get_nombre(docente)} - Número de empleado: {Docente.get_NumEmpleado(docente)}")
    while True:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]

def elegir_asignatura(lista):
    print("Asignatura ofrecida: ")
    for i, asignatura in enumerate(lista, start=1):
        print(f"{i}. Nombre: {asignatura.get_nombreA()} - Código: {asignatura.get_codigoA()}")
    while True:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]
        
def mostrar_grupos(grupo_controller):
    grupos = grupo_controller.get_grupos()
    if not grupos:
        print("No se han registrado grupos académicos")
        return
    for grupo in grupos:
        print(grupo.mostrar_informacion_grupo())
        print("-" * 20)

def agregar_grupo(grupo_controller, asignatura_controller, persona_controller):
    if not any(type(objeto)== Docente for objeto in persona_controller.get_persona()):
        print("Primero debe registrar al menos un docente.")
        return
    if not asignatura_controller.get_asignatura():
        print("Primero debe registrar al menos una asignatura.")
        return
    
    codigo=input("Ingrese el códgio del grupo académico: ")
    asignatura = elegir_asignatura(asignatura_controller.get_asignatura())
    docente=elegir_docente(persona_controller.get_persona())
    capacidad_maxima=int(input("Ingrese la cantidad máxima de estudiantes: "))
    # El horario se pide aquí porque se crea como parte del grupo (composición)
    print("Horario del grupo: ")
    dia=input("Ingrese el día: ")
    hora_inicio=input("Ingrese la hora de inicio: ")
    hora_fin=input("Ingrese la hora de fin: ")
    salon=input("Ingrese el salón: ")
    
    grupo_controller.añadir_grupo(codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon)
    print("Grupo académico agregado con éxito")
