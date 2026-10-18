"""Demostración automática de las siete pruebas mínimas de la actividad.

Se ejecuta desde la opción del menú de main.py. Crea objetos con datos
FICTICIOS y muestra, en orden, cada una de las pruebas que pide el documento,
sin que el usuario tenga que escribir los datos a mano.
"""

from models.programa import Programa
from models.Asignatura import Asignatura
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo


def titulo(texto):
    """Imprime un encabezado para separar cada prueba en la salida."""
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


def ejecutar_demostracion():
    # ------------------------------------------------------------------
    titulo("PRUEBA 1. Creación de programas académicos y asignaturas")
    # ------------------------------------------------------------------
    analitica = Programa("PA-001", "Ingeniería en Analítica de Datos",
                         "Ciencias e Ingenierías", 10)
    sistemas = Programa("PA-002", "Ingeniería de Sistemas",
                        "Ciencias e Ingenierías", 10)
    poo = Asignatura("AS-101", "Programación Orientada a Objetos", 3, analitica)
    estadistica = Asignatura("AS-102", "Estadística Descriptiva", 4, analitica)
    redes = Asignatura("AS-201", "Redes de Computadores", 3, sistemas)

    programas = [analitica, sistemas]
    asignaturas = [poo, estadistica, redes]
    print(f"Se crearon {len(programas)} programas y {len(asignaturas)} asignaturas.")

    # ------------------------------------------------------------------
    titulo("PRUEBA 2. Creación de seis personas (2 de cada tipo)")
    # ------------------------------------------------------------------
    est_laura = Estudiante("1001", "Laura Gómez (ficticia)",
                           "laura.gomez@correo.ejemplo.edu.co",
                           "EST-2024-01", analitica, 3, 4.25)
    est_andres = Estudiante("1002", "Andrés Ríos (ficticio)",
                            "andres.rios@correo.ejemplo.edu.co",
                            "EST-2023-07", sistemas, 5, 3.80)
    doc_marta = Docente("2001", "Marta Salazar (ficticia)",
                        "marta.salazar@correo.ejemplo.edu.co",
                        "EMP-501", "Ciencias e Ingenierías", "Tiempo completo", 40)
    doc_jorge = Docente("2002", "Jorge Castaño (ficticio)",
                        "jorge.castano@correo.ejemplo.edu.co",
                        "EMP-502", "Ciencias Contables, Económicas y Administrativas",
                        "Cátedra", 12)
    adm_paula = Administrativo("3001", "Paula Henao (ficticia)",
                               "paula.henao@correo.ejemplo.edu.co",
                               "EMP-801", "Registro Académico", "Coordinadora", "Diurna")
    adm_carlos = Administrativo("3002", "Carlos Mejía (ficticio)",
                                "carlos.mejia@correo.ejemplo.edu.co",
                                "EMP-802", "Bienestar Universitario",
                                "Auxiliar administrativo", "Mixta")

    # Colección ÚNICA, con los tipos mezclados a propósito.
    personas = [est_laura, doc_marta, adm_paula, est_andres, doc_jorge, adm_carlos]
    print(f"Se crearon {len(personas)} personas en una única colección.")

    # ------------------------------------------------------------------
    titulo("PRUEBA 3. Consulta de la información de los objetos")
    # ------------------------------------------------------------------
    for programa in programas:
        print(programa.mostrar_informacion() + "\n")
    for asignatura in asignaturas:
        print(asignatura.mostrar_informacion() + "\n")
    print("Consulta con métodos get_:")
    print(f"  Créditos de {poo.get_nombreA()}: {poo.get_NumCreditos()}")
    print(f"  Correo de {est_laura.get_nombre()}: {est_laura.get_correo()}")
    print(f"  Semestre de {est_andres.get_nombre()}: {est_andres.get_semestre()}")

    # ------------------------------------------------------------------
    titulo("PRUEBA 4. Modificación válida de datos encapsulados")
    # ------------------------------------------------------------------
    print(f"Correo antes:      {est_laura.get_correo()}")
    est_laura.set_correo("laura.gomez.nuevo@correo.ejemplo.edu.co")
    print(f"Correo después:    {est_laura.get_correo()}")

    print(f"Semestres antes:   {sistemas.get_NumeroSemestres()}")
    sistemas.set_NumeroSemestres(9)
    print(f"Semestres después: {sistemas.get_NumeroSemestres()}")

    print(f"Créditos antes:    {estadistica.get_NumCreditos()}")
    estadistica.set_NumCreditos(3)
    print(f"Créditos después:  {estadistica.get_NumCreditos()}")

    # ------------------------------------------------------------------
    titulo("PRUEBA 5. Intento de asignar valores inválidos")
    # ------------------------------------------------------------------
    # Cada intento informa el error y se verifica que el dato NO cambió.
    correo_original = doc_marta.get_correo()
    try:
        doc_marta.set_correo("")
    except ValueError as error:
        print(f"[Rechazado] Correo vacío -> {error}")
    print(f"  Correo conservado: {doc_marta.get_correo()} "
          f"(sin cambios: {doc_marta.get_correo() == correo_original})")

    semestres_original = analitica.get_NumeroSemestres()
    try:
        analitica.set_NumeroSemestres(0)
    except ValueError as error:
        print(f"[Rechazado] Semestres = 0 -> {error}")
    print(f"  Semestres conservados: {analitica.get_NumeroSemestres()} "
          f"(sin cambios: {analitica.get_NumeroSemestres() == semestres_original})")

    creditos_original = poo.get_NumCreditos()
    try:
        poo.set_NumCreditos(-2)
    except ValueError as error:
        print(f"[Rechazado] Créditos = -2 -> {error}")
    print(f"  Créditos conservados: {poo.get_NumCreditos()} "
          f"(sin cambios: {poo.get_NumCreditos() == creditos_original})")

    promedio_original = est_andres.get_promedio_acumulado()
    try:
        est_andres.set_promedio_acumulado(7.5)
    except ValueError as error:
        print(f"[Rechazado] Promedio = 7.5 -> {error}")
    print(f"  Promedio conservado: {est_andres.get_promedio_acumulado()} "
          f"(sin cambios: {est_andres.get_promedio_acumulado() == promedio_original})")

    # ------------------------------------------------------------------
    titulo("PRUEBA 6. Presentación particular de cada tipo de persona")
    # ------------------------------------------------------------------
    # Un ejemplo de cada tipo para comparar sus presentaciones.
    # (El recorrido polimórfico de toda la colección es la prueba 7.)
    print(est_laura.mostrar_informacion() + "\n")
    print(doc_marta.mostrar_informacion() + "\n")
    print(adm_paula.mostrar_informacion())

    # ------------------------------------------------------------------
    titulo("PRUEBA 7. Recorrido polimórfico de la colección de personas")
    # ------------------------------------------------------------------
    # Un único ciclo, sin preguntar el tipo de cada objeto: Python ejecuta
    # automáticamente la versión del método que corresponde a su clase real.
    for persona in personas:
        print(persona.mostrar_informacion())
        print(f"Actividad principal: {persona.realizar_actividad_principal()}")
        print("-" * 70)
