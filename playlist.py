from models.cancion import Cancion


class Playlist:
    """Nueva lista enlazada formada por canciones elegidas de la biblioteca."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza = None

    def agregar(self, cancion):
        nueva = Cancion(cancion.datos["titulo"], cancion.datos["artista"], cancion.datos["duracion"])
        if not self.cabeza:
            self.cabeza = nueva
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    def listar(self):
        resultado, actual = [], self.cabeza
        while actual:
            resultado.append(actual)
            actual = actual.siguiente
        return resultado
