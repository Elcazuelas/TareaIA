class Nodo:
    def ___init__(self, nombre):
        self.nombre = nombre
        self.aristas = []

    def agregar_arista(self, nodoDest, distancia):
        self.aristas.append(Arista(self, nodoDest, distancia))

class Arista:
    def __init__(self, nodoA, nodoB, distancia):
        self.nodoA = nodoA
        self.nodoB = nodoB
        self.distancia = distancia

class Ciudad:
    def __init__(self):
        self.mapa = {}

    def agregar_nodo(self, nombre):
        nodo = Nodo(nombre)
        self.mapa[nombre] = nodo

    def conectar_calles(self, nombre_nodoA, nombre_nodoB, distancia):
        nodoA = self.mapa.get(nombre_nodoA)
        nodoB = self.mapa.get(nombre_nodoB)

        if nodoA and nodoB:
            nodoA.agregarArista(nodoB, distancia)
            nodoB.agregarArista(nodoA, distancia)

    def obtener_nodo(self, nombre):
        return self.mapa.get(nombre)
