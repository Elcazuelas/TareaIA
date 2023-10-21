class Nodo:
    def init(self, nombre):
        self.nombre = nombre
        self.aristas = []

    def agregar_arista(self, nodo_destino, distancia):
        self.aristas.append(Arista(self, nodo_destino, distancia))

class Arista:
    def init(self, nodo_a, nodo_b, distancia):
        self.nodo_a = nodo_a
        self.nodo_b = nodo_b
        self.distancia = distancia

class Ciudad:
    def init(self):
        self.mapa = {}

    def agregar_nodo(self, nombre):
        nodo = Nodo(nombre)
        self.mapa[nombre] = nodo

    def conectar_calles(self, nombre_nodo_a, nombre_nodo_b, distancia):
        nodo_a = self.mapa.get(nombre_nodo_a)
        nodo_b = self.mapa.get(nombre_nodo_b)

        if nodo_a and nodo_b:
            nodo_a.agregar_arista(nodo_b, distancia)
            nodo_b.agregar_arista(nodo_a, distancia)

    def obtener_nodo(self, nombre):
        return self.mapa.get(nombre)
