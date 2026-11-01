"""Pruebas mínimas de funcionamiento de la Actividad Colaborativa 2.

Se ejecutan desde la opción 6 del menú principal. Crean objetos con datos
ficticios y demuestran, en orden, las 11 pruebas que pide el documento.
Cada excepción personalizada se lanza desde el método donde ocurre la
situación y se captura aquí, mostrando un mensaje y continuando.
"""

from controllers.persona_controller import PersonaController
from controllers.programa_controller import ProgramaController
from controllers.asignatura_controller import AsignaturaController
from controllers.grupo_controller import GrupoAcademicoController
from models.personas import Personas
from models.docente import Docente
from models.estudiante import Estudiante
from models.excepciones import SistemaAcademicoError


def obtener_docentes(persona_controller):
    return [p for p in persona_controller.get_persona() if isinstance(p, Docente)]

def obtener_estudiantes(persona_controller):
    return [p for p in persona_controller.get_persona() if isinstance(p, Estudiante)]

def titulo(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)

def ejecutar_pruebas_ac2():
    """Ejecuta en orden las 11 pruebas mínimas de la Actividad Colaborativa 2.

    Cada excepción personalizada se lanza desde el método donde ocurre la
    situación y se captura aquí, en el programa principal.
    Los datos son ficticios.
    """
    persona_controller = PersonaController()
    programa_controller = ProgramaController()
    asignatura_controller = AsignaturaController()
    grupo_controller = GrupoAcademicoController()
    excepciones_controladas = 0

    titulo("PRUEBA 1. No se puede crear directamente una persona")
    try:
        Personas("9999", "Persona genérica", "generica@correo.com")
        print("Error: se creó una Persona directamente")
    except TypeError as error:
        print(f"[Controlado] No se puede crear un objeto Personas: {error}")

    titulo("PRUEBA 2. Creación de asignaturas, docentes, estudiantes y horarios")
    programa_controller.añadir_programa("P1", "Ingeniería en Analítica de Datos", "Ciencias e Ingenierías", 10)
    analitica = programa_controller.buscar_programa("P1")
    asignatura_controller.añadir_asignatura("A1", "Programación Orientada a Objetos", 3, analitica)
    asignatura_controller.añadir_asignatura("A2", "Estadística Descriptiva", 4, analitica)
    persona_controller.añadir_docente("2001", "Marta Salazar", "marta@correo.com", "EMP-501", "Ciencias e Ingenierías", "Tiempo completo", 40)
    persona_controller.añadir_docente("2002", "Jorge Castaño", "jorge@correo.com", "EMP-502", "Ciencias e Ingenierías", "Cátedra", 12)
    persona_controller.añadir_estudiante("1001", "Ana Gómez", "ana@correo.com", "E001", analitica, 3, 4.2)
    persona_controller.añadir_estudiante("1002", "Luis Ríos", "luis@correo.com", "E002", analitica, 3, 3.8)
    persona_controller.añadir_estudiante("1003", "Sofía Henao", "sofia@correo.com", "E003", analitica, 2, 4.5)
    persona_controller.añadir_administrativo("3001", "Paula Mejía", "paula@correo.com", "EMP-801", "Registro Académico", "Coordinadora", "Diurna")
    print(f"Se crearon {len(asignatura_controller.get_asignatura())} asignaturas y {len(persona_controller.get_persona())} personas.")
    print("Los horarios se crean como parte de cada grupo académico (composición): ver prueba 3.")
    print("\nPolimorfismo de la AC1 (un solo ciclo para todas las personas):")
    for persona in persona_controller.get_persona():
        print(f"  - {persona.realizar_actividad_principal()}")

    titulo("PRUEBA 3. Creación de dos grupos académicos")
    poo = asignatura_controller.buscar_asignatura("A1")
    estadistica = asignatura_controller.buscar_asignatura("A2")
    marta, jorge = obtener_docentes(persona_controller)
    grupo_controller.añadir_grupo("G1", poo, marta, 2, "Lunes", "08:00", "10:00", "B-201")
    grupo_controller.añadir_grupo("G2", estadistica, jorge, 3, "Miércoles", "14:00", "16:00", "C-105")
    g1, g2 = grupo_controller.get_grupos()
    for grupo in grupo_controller.get_grupos():
        print(grupo.mostrar_informacion_grupo())
        print()

    titulo("PRUEBA 4. Matrícula correcta de estudiantes")
    ana, luis, sofia = obtener_estudiantes(persona_controller)
    g1.matricular_estudiante(ana)
    g1.matricular_estudiante(luis)
    g2.matricular_estudiante(ana)
    g1.mostrar_estudiantes()
    g2.mostrar_estudiantes()

    titulo("PRUEBA 5. Intento de matricular un estudiante duplicado")
    try:
        g1.matricular_estudiante(ana)
    except SistemaAcademicoError as error:
        excepciones_controladas += 1
        print(f"[{type(error).__name__}] {error}")
    print("El programa continúa: el grupo G1 sigue con", len(g1.estudiantes), "estudiantes.")

    titulo("PRUEBA 6. Intento de superar la capacidad de un grupo")
    try:
        g1.matricular_estudiante(sofia)
    except SistemaAcademicoError as error:
        excepciones_controladas += 1
        print(f"[{type(error).__name__}] {error}")
    print("El programa continúa: Sofía no quedó matriculada en G1.")

    titulo("PRUEBA 7. Retiro correcto de un estudiante")
    print(g1.retirar_estudiante("E002"))
    g1.mostrar_estudiantes()

    titulo("PRUEBA 8. Intento de retirar un estudiante que no está matriculado")
    try:
        g1.retirar_estudiante("E999")
    except SistemaAcademicoError as error:
        excepciones_controladas += 1
        print(f"[{type(error).__name__}] {error}")
    print("El programa continúa.")

    titulo("PRUEBA 9. Búsqueda de una asignatura inexistente")
    try:
        asignatura_controller.buscar_asignatura("A99")
    except SistemaAcademicoError as error:
        excepciones_controladas += 1
        print(f"[{type(error).__name__}] {error}")
    print("El programa continúa.")

    titulo("PRUEBA 10. Búsqueda de un programa inexistente")
    try:
        programa_controller.buscar_programa("P99")
    except SistemaAcademicoError as error:
        excepciones_controladas += 1
        print(f"[{type(error).__name__}] {error}")
    print("El programa continúa.")

    titulo("PRUEBA 11. Continuidad del programa después de cada excepción")
    print(f"Se controlaron {excepciones_controladas} excepciones personalizadas y el programa siguió ejecutándose.")
    print("Estado final de los grupos:")
    for grupo in grupo_controller.get_grupos():
        grupo.mostrar_estudiantes()
