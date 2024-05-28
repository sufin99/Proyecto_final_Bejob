# Definimos la clase Task. Representa una tarea individual. Cada tarea
# tiene una descripción y un estado que indica si esta completado o no.
class Task:
	def __init__(self, description, completed = False):
		self.description = description
		self.completed = completed

# Definimos un gestor de tareas "TaskManager". Gestiona una lista de tareas
# con los métodos add_task, mark_completed, show_tasks y eliminated_task.
class TaskManager:
	def __init__(self):
		self.tasks = []

	# Creamos un método para añadir una tarea. Introduciendo los datos de la tarea.
	def add_task(self, description):
		new_task = Task(description)
		self.tasks.append(new_task)
	
	# Creamos un método para marcar una tarea como completada introduciendo el índice.
	def mark_completed(self, i):
		try:
			self.tasks[i].completed = True
		except IndexError: # Este error sucede si el usuario introduce un índice que no esté en la lista o si la lista de tareas esta vacía.
			print("\nError: El índice no es válido")
	
	# Creamos un método que muestre todas las tareas de la lista.
	def show_tasks(self):
		if not self.tasks: # Si la lista esta vacía se muestra un mensaje que felicita al usuario y le pide añadir una tarea.
			print("\n¡Enhorabuena! No hay tareas pendientes. Añade alguna tarea que quieras realizar")
			return
	
		for i, tks in enumerate(self.tasks): # Por defecto, las tareas añadidas como pendientes. Y la cambia a completada si así lo pide el usuario.
			if i == 0: # Añado un salto de línea en el primer índice.
				status = "Completada" if tks.completed else "Pendiente"
				print(f"\n{i}: {tks.description} - {status}")
			else:
				status = "Completada" if tks.completed else "Pendiente"
				print(f"{i}: {tks.description} - {status}")

	# Creamos un método para eliminar una tarea introduciendo el índice.		
	def eliminate_task(self, i):
		try:
			del self.tasks[i]
		except IndexError: # Este error sucede si el usuario introduce un índice que no esté en la lista o si la lista de tareas esta vacía.
			print("\nError: El índice no es válido") 

# Se crea una instancia de Taskmanager. Se utilizará para gestionar las tareas
# del usuario.
gestor = TaskManager()

# Entramos en un bucle para que el usuario elija la opción que quiera hasta que
# elija salir del bucle. Dentro del bucle enseña el menú de opciones.
while True:
	print("\n1. Agregar una tarea")
	print("2. Completar una tarea")
	print("3. Mostrar todas las tareas")
	print("4. Eliminar una tarea")
	print("5. Salir")

	option = input("\nElige una opción: ")

# Dependiendo de la opción que elija el usuario se llama a un método o a otro correspondiente
# al gestor de TaskManager.
	try:
		if option == "1": # Si el usuario elige la opción 1, el usuario podrá añadir una tarea.
			description = input("\nIntroduce la descripción de la tarea: ")
			gestor.add_task(description) # Llama al método add_task.
		elif option == "2": # Si el usuario elige la opción 2, el usuario podrá completar una tarea.
			try:
				i = int(input("\nIntroduce el índice de la tarea que quieres completar: "))
				gestor.mark_completed(i) # Llama al método mark_completed usando un índice.
			except ValueError:
				print("\nError: Debes introducir un número.") # Imprime este error si el usuario introduce un string.
				continue
		elif option == "3": # Si el usuario elige la opción 3, el usuario podrá ver las tareas.
			gestor.show_tasks() # Llama al método show_tasks.
		elif option == "4": # Si el usuario elige la opción 4, el usuario podrá eliminar una tarea.
			try:
				i = int(input("\nIntroduce el índice de la tarea que qieres eliminar: "))
				gestor.eliminate_task(i) # Llama al método eliminate_task usando un índice.
			except ValueError:
				print("\nError: Debes introducir un número.") # Imprime este error si el usuario introduce un string.
				continue
		elif option == "5": # Si el usuario elige la opción 5, el usuario podrá salir del programa.
			break # Salir del bucle y parar el programa.
		else:
			print("\nOpción no válida. Introduce la opción del 1 al 5.") # Imprime esto si el usuario introduce algo que no concuerde con las opciones del 1 al 5.
	except Exception as e: # Sirve como manejo de excepciones. Captura la excepción como la variable e y luego imprime un mensaje de error.
		print(f"\nError: {e}")
	
	print("\n////***********************************************////")
