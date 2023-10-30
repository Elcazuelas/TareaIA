from time import time
from Ciudad import Ciudad  # Importa las clases desde el otro archivo
import AlgoritmosBusqueda
#crear Ciudad
ciudad = Ciudad()

ciudad.agregar_nodo("A")
ciudad.agregar_nodo("B")
ciudad.agregar_nodo("C")
ciudad.agregar_nodo("D")

ciudad.conectar_calles("A", "B", 1)
ciudad.conectar_calles("B", "D", 1)
ciudad.conectar_calles("C", "D", 2)

start_time = time()
camino_bfs = AlgoritmosBusqueda.bfs(ciudad, "A", "C")
time_bfs = time() - start_time

start_time = time()
camino_dfs = AlgoritmosBusqueda.dfs(ciudad, "A", "C")
time_dfs = time() - start_time

start_time = time()
camino_a_star = AlgoritmosBusqueda.a_star(ciudad, "A", "C")
time_a_star = time() - start_time


if camino:
    nombres_nodos = [nodo.nombre for nodo in camino]
    print("Camino encontrado:", " -> ".join(nombres_nodos), " tiempo ", elapsed_time)
    print("Elapsed time: %0.10f seconds." % elapsed_time)
else:
    print("No se encontró un camino entre los nodos.")