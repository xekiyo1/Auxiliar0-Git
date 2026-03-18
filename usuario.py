class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
<<<<<<< HEAD
       for tarea in self.tareas:
           if tarea.estaLista():
               print(f"La tarea {tarea.obtenerNombre()} está lista")
               print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"[X] {tarea.obtenerNombre()}" )
>>>>>>> 5e10bde1c233c6799aeb07b39fa3d0cc8d3ae0f7
