# Sistema de Gestión Académica con Programación Orientada a Objetos
Proyecto de la Actividad colaborativa N.º 1 y N.º 2 — Universidad de Manizales.

Sistema en Python que modela personas, programas académicos, asignaturas y grupos académicos de una institución educativa. En la **Actividad 1** se aplicaron clases, encapsulamiento, herencia, sobrescritura y polimorfismo. En la **Actividad 2** el mismo proyecto evolucionó con **clases abstractas**, **composición** y **excepciones personalizadas**, para gestionar la oferta de grupos y la matrícula de estudiantes.
 
## Nombre de los integrantes
- María José Osorio Giraldo - @MariaJose1220
- Laura Fernanda Pérez Galvis - @Laferpg
- Juan Camilo Pérez Oviedo - @juankp86

## Versiones entregadas
- `v1.0-actividad1`: versión entregada en la Actividad Colaborativa 1.
- `Entrega_AC2`: versión entregada en la Actividad Colaborativa 2.

## Estructura del proyecto
`main.py` solo crea los controladores e inicia el menú. Los menús y las funciones auxiliares están organizados en la carpeta `menus`, las clases del sistema en `models` y las clases que guardan y buscan los objetos en `controllers`.
```
~ main.py                           -> Archivo principal: inicia el sistema
~ demostracion.py                   -> Demostración de las 7 pruebas de la Actividad 1
~ demostracion_ac2.py               -> Demostración de las 11 pruebas de la Actividad 2
~ Documento de Decisiones de Diseño.docx -> Documento de decisiones de diseño (Actividad 2)
~ README.md
~ menus
   - menu_principal.py              -> Menú principal y submenús de agregar, mostrar y buscar
   - menu_secundario.py             -> Submenú de grupos académicos (agregar, matricular, retirar)
   - metodos.py                     -> Funciones auxiliares para elegir y mostrar objetos
~ controllers
   - persona_controller.py          -> Guarda estudiantes, docentes y administrativos en una sola lista
   - programa_controller.py         -> Guarda y busca programas académicos
   - asignatura_controller.py       -> Guarda y busca asignaturas
   - grupo_controller.py            -> Guarda los grupos académicos
~ models
   - personas.py                    -> Clase abstracta Personas
   - estudiante.py                  -> Clase hija de Personas
   - docente.py                     -> Clase hija de Personas
   - administrativo.py              -> Clase hija de Personas
   - programa.py                    -> Clase Programa académico
   - asignatura.py                  -> Clase Asignatura (asociada a un programa)
   - horario.py                     -> Clase Horario (forma parte de un grupo)
   - grupo_academico.py             -> Clase GrupoAcademico
   - excepciones.py                 -> Excepciones personalizadas del sistema
```
## Ejecución 
Requiere Python 3.10 o superior (el menú usa `match`). No se necesitan librerías externas.
```bash
git clone https://github.com/MariaJose1220/Sistema-de-gestion-academica.git
cd Sistema-de-gestion-academica
python main.py
```
(en Windows también funciona `py main.py`)

Al ejecutarlo se muestra el menú principal. Los datos se escriben por teclado y se guardan en memoria mientras el programa esté abierto:
 
1. **Agregar:** programa académico, asignatura, estudiante, docente, administrativo, o entrar al **submenú de grupos académicos** (agregar un grupo con su horario, matricular un estudiante, retirar un estudiante, mostrar los estudiantes matriculados y mostrar los grupos).
2. **Mostrar:** programas, personas y asignaturas. Al mostrar las personas, cada una presenta sus datos y realiza su actividad principal.
3. **Buscar:** asignatura o programa académico por código.
4. **Cambiar el correo** de cualquier persona.
5. **Ejecutar la demostración de la Actividad 1** (7 pruebas).
6. **Ejecutar las pruebas de la Actividad 2** (11 pruebas, con todas las excepciones).
7. **Salir.**
Primero se debe registrar un programa académico, porque las asignaturas y los estudiantes pertenecen a uno. Para crear un grupo se necesitan al menos una asignatura y un docente.

## Conceptos aplicados — Actividad 1
 
### Encapsulamiento y validaciones
Los atributos se escriben con un guion bajo (por ejemplo `self._nombre`), lo que indica por convención que no deben usarse directamente desde fuera de la clase. Se leen y modifican mediante métodos get y set. Los setters validan el dato y lanzan `ValueError` si no cumple. Los constructores también usan los setters, de modo que no se puede crear un objeto con datos inválidos.
 
Validaciones principales: el correo, el nombre y la identificación no pueden estar vacíos; el número de semestres, los créditos, las horas semanales de un docente y la capacidad de un grupo deben ser mayores que cero; el promedio acumulado debe estar entre 0.0 y 5.0.
 
### Herencia
`Estudiante`, `Docente` y `Administrativo` heredan de `Personas` los atributos y comportamientos comunes (identificación, nombre, correo y sus validaciones) y agregan los propios de su rol. Cada constructor llama a `super().__init__(identificacion, nombre, correo)`.
 
### Sobrescritura
Las tres clases hijas sobrescriben `mostrar_informacion()`: reutilizan la versión de `Personas` con `super()` y agregan sus datos. Además, cada una implementa `realizar_actividad_principal()` con un comportamiento propio.
 
### Polimorfismo
Las personas se guardan en una sola lista en `PersonaController`. La función `mostrar_personas()` (`menus/metodos.py`) la recorre con un único ciclo, sin condicionales que revisen el tipo, y Python ejecuta automáticamente el método que corresponde a la clase real de cada objeto.
 
## Conceptos aplicados — Actividad 2
 
### Clase abstracta
No tiene sentido registrar una persona sin saber si es estudiante, docente o administrativo. Por eso `Personas` hereda de `ABC` y define `realizar_actividad_principal()` como método abstracto (`@abstractmethod`). Así, Python impide crear objetos directamente de `Personas` (lanza `TypeError`), y cada clase hija está obligada a implementar su actividad principal.
 
### Grupo académico
`GrupoAcademico` recibe objetos ya creados de `Asignatura` y `Docente` (no sus nombres como texto), guarda la capacidad máxima y la lista de estudiantes matriculados, y ofrece los métodos `mostrar_informacion_grupo()`, `matricular_estudiante(estudiante)`, `retirar_estudiante(codigo_estudiantil)` y `mostrar_estudiantes()`.
 
### Composición: por qué el grupo contiene un horario
El horario describe cuándo y dónde se desarrolla un grupo, y no tiene sentido por sí solo. Por eso el constructor de `GrupoAcademico` recibe el día, la hora de inicio, la hora de finalización y el salón, y **crea el objeto `Horario` dentro del grupo**. El horario nace con el grupo y le pertenece solo a él: es una relación de **composición** («el grupo tiene un horario»). El horario es un objeto con sus propios atributos y métodos, no una cadena de texto.
 
**Por qué no es herencia:** la herencia expresa una relación «es un» (un estudiante *es una* persona). Un grupo académico *no es* un horario, ni un horario es un tipo de grupo; el grupo *tiene* un horario. Si `GrupoAcademico` heredara de `Horario`, el grupo sería un tipo de horario, lo cual no describe la realidad.
 
En cambio, la asignatura y el docente existen antes y después del grupo: el grupo solo los referencia (agregación).
 
### Excepciones personalizadas
Se definen en `models/excepciones.py`. Todas heredan de `SistemaAcademicoError` (que hereda de `Exception`):
 
| Excepción | Situación | Dónde se lanza |
|---|---|---|
| `EstudianteYaMatriculadoError` | El estudiante ya está matriculado en el grupo | `GrupoAcademico.matricular_estudiante()` |
| `CapacidadMaximaError` | El grupo alcanzó su capacidad máxima | `GrupoAcademico.matricular_estudiante()` |
| `EstudianteNoMatriculadoError` | El estudiante a retirar no está matriculado | `GrupoAcademico.retirar_estudiante()` |
| `AsignaturaNoEncontradaError` | La asignatura buscada no existe | `AsignaturaController.buscar_asignatura()` |
| `ProgramaNoEncontradoError` | El programa académico buscado no existe | `ProgramaController.buscar_programa()` |
 
Cada una se lanza con `raise` desde el método donde ocurre la situación, se captura con `try/except` en los menús y en `demostracion_ac2.py`, muestra un mensaje comprensible y el programa continúa.
 
## Pruebas
La opción **6** del menú principal ejecuta las 11 pruebas mínimas de la Actividad 2:
 
1. No se puede crear directamente una persona.
2. Creación de asignaturas, docentes, estudiantes y horarios.
3. Creación de dos grupos académicos.
4. Matrícula correcta de estudiantes.
5. Intento de matricular un estudiante duplicado.
6. Intento de superar la capacidad de un grupo.
7. Retiro correcto de un estudiante.
8. Intento de retirar un estudiante que no está matriculado.
9. Búsqueda de una asignatura inexistente.
10. Búsqueda de un programa inexistente.
11. Continuidad del programa después de cada excepción.
La opción **5** ejecuta las 7 pruebas de la Actividad 1.
 
## Declaración de uso de inteligencia artificial
El equipo utilizó Claude como herramienta de apoyo en este proyecto para: comprender conceptos, revisar errores y proponer datos ejemplo 
y fragmentos de código. 

El equipo revisó, probó y comprende el código entregado, y puede explicarlo.
