Caso práctico final:
Proyecto final de mano de Bejob e IbmSkillBuild del curso de Python Full Stack.

Enunciado:

Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
una lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes
operaciones:
• Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
la lista de tareas pendientes.
• Marcar una tarea como completada: El programa deberá permitir al usuario marcar una
tarea como completada, dada su posición en la lista.
• Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
pendientes, numeradas y mostrando su estado (completada o pendiente).
• Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
dada su posición.

El programa deberá incluir las siguientes características:
• Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
usuario ingrese una opción no válida o una posición que no exista en la lista.
• Comentarios explicativos: El código deberá estar comentado para explicar su
funcionamiento en cada parte relevante.


-Pasos:
1. Definimos una clase Task que representará una tarea individual. Esta clase deberá tener al menos dos atributos: description (para almacenar la descripción de la tarea) y completed (para indicar si la tarea ha sido completada o no).
2. Definimos una clase TaskManager que manejará la lista de tareas. Esta clase deberá tener al menos un atributo: tasks (una lista para almacenar las tareas).
3. En la clase TaskManager, definimos un método add_task que toma una descripción de tarea como argumento, creamos una nueva instancia de Task con esa descripción, y la añadimos a la lista de tareas.
4. Definimos un método mark_completed que toma el índice de la tarea como argumento, y marca esa tarea como completada. Manejamos la excepción que se producirá si el índice no es válido.
5. Definimos un método show_tasks que imprime todas las tareas en la lista, junto con su estado. Cada tarea debe estar numerada.
6. Define un método eliminate_task que toma un índice de tarea como argumento, y elimina esa tarea de la lista. Manejamos la excepción que se producirá si el índice no es válido.
8. Añadimos comentarios explicativos.