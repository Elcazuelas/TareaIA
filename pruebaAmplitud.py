from ciudad import Ciudad  # Importa las clases desde el otro archivo

def bfs(ciudad, nombre_nodo_inicio, nombre_nodo_destino):
    nodo_inicio = ciudad.obtener_nodo(nombre_nodo_inicio)
    nodo_destino = ciudad.obtener_nodo(nombre_nodo_destino)

    if nodo_inicio is None or nodo_destino is None:
        return None

    visitados = set()
    cola = []
    cola.append([nodo_inicio])

    while cola:
        camino = cola.pop(0)
        nodo_actual = camino[-1]

        if nodo_actual == nodo_destino:
            return camino

        if nodo_actual not in visitados:
            for arista in nodo_actual.aristas:
                nodo_vecino = arista.nodoB
                nuevo_camino = list(camino)
                nuevo_camino.append(nodo_vecino)
                cola.append(nuevo_camino)

            visitados.add(nodo_actual)

    return None  # Si no se encontró un camino

def dfs(ciudad, nombre_nodo_inicio, nombre_nodo_destino):
    nodo_inicio = ciudad.obtener_nodo(nombre_nodo_inicio)
    nodo_destino = ciudad.obtener_nodo(nombre_nodo_destino)

    if nodo_inicio is None or nodo_destino is None:
        return None

    visitados = set()
    pila = []
    pila.append([nodo_inicio])

    while pila:
        camino = pila.pop()
        nodo_actual = camino[-1]

        if nodo_actual == nodo_destino:
            return camino

        if nodo_actual not in visitados:
            for arista in nodo_actual.aristas:
                nodo_vecino = arista.nodoB
                nuevo_camino = list(camino)
                nuevo_camino.append(nodo_vecino)
                pila.append(nuevo_camino)

            visitados.add(nodo_actual)

    return None  # Si no se encontró un camino

if __name__ == "__main__":
    ciudad = Ciudad()

    ciudad.agregar_nodo("A")
    ciudad.agregar_nodo("B")
    ciudad.agregar_nodo("C")
    ciudad.agregar_nodo("D")

    ciudad.conectar_calles("A", "B", 1)
    ciudad.conectar_calles("B", "C", 2)
    ciudad.conectar_calles("B", "D", 1)
    ciudad.conectar_calles("C", "D", 2)

    camino = bfs(ciudad, "A", "C")

    if camino:
        nombres_nodos = [nodo.nombre for nodo in camino]
        print("Camino encontrado:", " -> ".join(nombres_nodos))
    else:
        print("No se encontró un camino entre los nodos.")