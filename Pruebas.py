import time
import sys
from AlgoritmosBusqueda import *
from ciudad import *

if __name__ == "__main__":
    ciudad = Ciudad()

    for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ciudad.agregar_nodo(letra)

    # Conectar calles con distancias en formato decimal
    ciudad.conectar_calles("A", "B", 1.5)
    ciudad.conectar_calles("A", "C", 2.2)
    ciudad.conectar_calles("B", "D", 1.8)
    ciudad.conectar_calles("C", "E", 2.3)
    ciudad.conectar_calles("D", "F", 1.7)
    ciudad.conectar_calles("E", "G", 2.5)
    ciudad.conectar_calles("F", "H", 1.6)
    ciudad.conectar_calles("G", "I", 3.0)
    ciudad.conectar_calles("H", "J", 2.2)
    ciudad.conectar_calles("I", "K", 1.9)
    ciudad.conectar_calles("J", "L", 2.7)
    ciudad.conectar_calles("K", "M", 1.8)
    ciudad.conectar_calles("L", "N", 2.6)
    ciudad.conectar_calles("M", "O", 1.7)
    ciudad.conectar_calles("N", "P", 3.2)
    ciudad.conectar_calles("O", "Q", 2.1)
    ciudad.conectar_calles("P", "R", 2.8)
    ciudad.conectar_calles("Q", "S", 1.6)
    ciudad.conectar_calles("R", "T", 3.1)
    ciudad.conectar_calles("S", "U", 2.9)
    ciudad.conectar_calles("U", "V", 2.4)
    ciudad.conectar_calles("V", "W", 1.9)
    ciudad.conectar_calles("W", "F", 2.1)

    
    # Medir el tiempo de ejecución y otros datos de BFS
    start_time = time.time_ns()
    camino_bfs = bfs(ciudad, "A", "W")
    end_time = time.time_ns()

    if camino_bfs:
        nombres_nodos_bfs = [nodo.nombre for nodo in camino_bfs]
        print("BFS")
        print("Camino encontrado: ", " -> ".join(nombres_nodos_bfs))
        print("Tiempo de ejecución: ", end_time - start_time, "nanosegundos")
        print("Complejidad Espacial: ", sys.getsizeof(camino_bfs), "bytes")
        print("Número de Nodos Explorados: ", len(camino_bfs))
        print("\n")
    else:
        print("No se encontró un camino con BFS.")

    # Medir el tiempo de ejecución y otros datos de DFS
    start_time = time.time_ns()
    camino_dfs = dfs(ciudad, "A", "W")
    end_time = time.time_ns()

    if camino_dfs:
        nombres_nodos_dfs = [nodo.nombre for nodo in camino_dfs]
        print("DFS")
        print("Camino encontrado: ", " -> ".join(nombres_nodos_dfs))
        print("Tiempo de ejecución: ", end_time - start_time, "nanosegundos")
        print("Complejidad Espacial: ", sys.getsizeof(camino_dfs), "bytes")
        print("Número de Nodos Explorados: ", len(camino_dfs))
        print("\n")
    else:
        print("No se encontró un camino con DFS.")

    # Medir el tiempo de ejecución y otros datos de A*
    start_time = time.time_ns()
    camino_a_star = a_star(ciudad, "A", "W")
    end_time = time.time_ns()

    if camino_a_star:
        nombres_nodos_a_star = [nodo.nombre for nodo in camino_a_star]
        print("A-Star")
        print("Camino encontrado: ", " -> ".join(nombres_nodos_a_star))
        print("Tiempo de ejecución: ", end_time - start_time, "nanosegundos")
        print("Complejidad Espacial: ", sys.getsizeof(camino_a_star), "bytes")
        print("Número de Nodos Explorados: ", len(camino_a_star))
        print("\n")
    else:
        print("No se encontró un camino con A*.")
