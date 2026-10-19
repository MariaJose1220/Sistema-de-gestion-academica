# Sistema de Gestión Académica con Programación Orientada a Objetos
Proyecto de la Actividad colaborativa N.º 1 — Universidad de Manizales.

Sistema en Python que modela personas, programas y asignaturas de una institución educativa, aplicando clases, encapsulamiento, herencia, sobrescritura y polimorfismo.
 
## Nombre de los integrantes
- María José Osorio Giraldo - @MariaJose1220
- Laura Fernanda Pérez Galvis - @Laferpg
- Juan Camilo Pérez Oviedo - @juankp86

## Estructura del proyecto
En nuestra carpeta encontramos un archivo principal main.py donde se ejecuta el programa, una carpeta llamada models donde se guardan los archivos correspondientes a cada clase del sistema y una carpeta llamada controllers que contiene archivos con clases que 
permiten guardar y traer datos.
```
~ controllers
   - asignatura_controller.py       -> Controlador de la clase asignatura 
   - persona_controller.py          -> Controlador de la clase personas y sus clases hijas     
   - programa_controller.py         -> Controlador de la clase programa académico     
~ models
    - Asignatura.py                 -> Clase asignatura
    - administrativo.py             -> Clase hija de personas
    - docente.py                    -> Clase hija de personas
    - estudiante.py                 -> Clase hija de personas
    - personas.py                   -> Clase base personas
    - Programa.py                   -> Clase programa académico
~ README.md
~ demostracion.py                   -> Clase con ejemplos y pruebas para demostrar correcto funcionamiento
~ main.py                           -> Archivo principal ejecutable
```
## Ejecución 
Código para ejecutar:
```bash
git clone <falta link>
cd sistema-de-gestion-academica
py main.py
```
Al ejecutar el archivo principal se muestra un menú con 11 opciones para que el usuario elija qué acción desea realizar, los datos se 
escriben por teclado y se guardan en memoria mientras el programa esté abierto: 

Se puede agregar un objeto a las diferentes clases como programa, asignatura, estudiante, docente y administrativo (opciones 1 a 5);
también puede ver los objetos que ha agregado a cada clase (opciones 6 a 8), en este caso las clases estudiante, docente y administrativo
se muestran en una misma acción ya que todas son personas, también se realizan los metodos de realizar_actividad_principal()
correspondientes para cada tipo de persona y, aunque todas están en una misma lista, el sistema reconoce qué tipo de persona es y realiza
el método correcto; para validar modificaciones se puede seleccionar cambiar un correo (opción 9) donde el usuario selecciona la persona y posteriormente cambia el correo, allí se verifica si es vacío y de ser así no lo guarda; por otro lado, si desea ver las 7 pruebas de 
funcionamiento sin necesidad de ingresar todos los objetos y realizar todo a mano, puede elegir ejecutar las pruebas de funcionamiento 
(opción 10) donde se verifica la creación de objetos en todas las clases como ejemplo, se realizan métodos como mostrar_informacion(), 
mostar_actividad_principal() y también getters y setters, se realizan verificaciones al modificar datos válidos, se verifica que no 
guarda modificaciones de datos inválidos y se realiza un recorrido polimórfico de personas; por último, puede seleccionar salir del menú (opción 11).

## Conceptos aplicados 
### Encapsulamiento y validaciones (fase 2) 
Los atributos son privados (se llaman con guion bajo, por ejemplo 'self._nombre') y solo se leen o modifican mediante métodos 
get() y set(). Los setters validan el dato y lanzan `ValueError` si no cumple (por ejemplo, que no esté vacío), los getters permiten 
llamar y leer el atributo. Los constructores también usan los setters, de modo que no se puede crear un objeto con datos inválidos.
 
#### Validaciones principales:
 
- El correo, el nombre y la identificación no pueden estar vacíos
- El número de semestres de un programa debe ser un entero mayor que cero
- Los créditos de una asignatura debe ser un entero mayor que cero
- El promedio acumulado de un estudiante debe estar entre 0.0 y 5.0
- Las horas semanales de un docente deben ser un entero mayor que cero
  
En el archivo de demostración se usa 'try/except' para atrapar errores, mostrar el mensaje y continuar sin detener el programa.

### Herencia (fase 3)
Como las clases 'Estudiante', 'Docente' y 'Administrativo' tienen atributos y métodos en común, heredan los atributos y comportamientos de la clase 'Persona' para evitar repetirlos en cada una de estas clases, así que los reutilizan y agregan los propios de su rol. 
Cada constructor en cada clase llama a super().__init__(identificacion, nombre, correo) para inicializar la parte heredada.

### Sobrescritura (fase 4)
Las tres clases hijas de personas sobreescriben el método mostrar_informacion() que existe en Persona ya que reutilizan la parte de la 
clase base con super() y agregan los datos correspondientes de cada rol.
 
Además, cada clase hija implementa realizar_actividad_principal() con el mismo nombre pero con un comportamiento propio, este método 
no existe en Persona, sino que se define de forma independiente en cada una de las tres clases.

### Polimorfismo (fase 5)
En persona_controller.py las personas registradas (estudiantes, docentes y administrativos) se guardan en una sola lista y la opción 
7 del menú la recorre sin condicionales que revisen el tipo. La opción 10 carga seis personas de ejemplo (dos de cada tipo) para 
probarlo rápidamente, ejecuta automáticamente el método que corresponde al tipo real de cada objeto y así el mismo código produce
resultados distintos según se trate de un estudiante, un docente o un administrativo.

## Pruebas sugeridas
1. Registrar un programa y una asignatura con datos válidos y consultarlos (opciones 1,2,6 y 8)
2. Intentar registrar con valores inválidos: semestres = 0, créditos = -2, correo vacío, promedio = 7.5 y saldrá el error
3. Modificar un correo válido y luego uno vacío (opción 9): el dato inválido se rechaza y se conserva el anterior
4. Registrar un estudiante, un docente y un administrativo (opciones 3 a 5)
5. Mostrar las personas (opción 7) y observar cómo cada tipo responde distinto al mismo método.

## Declaración de uso de inteligencia artificial
El equipo utilizó Claude como herramienta de apoyo en este proyecto para: comprender conceptos, revisar errores y proponer datos ejemplo
para creación de clases.

El equipo revisó, probó, comprende el código entregado y puede explicarlo.

