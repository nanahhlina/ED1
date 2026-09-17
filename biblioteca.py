from models.cancion import Cancion


class Biblioteca:
    """Lista enlazada simple con todas las canciones."""

    def __init__(self):
        self.cabeza = None

    def agregar(self, titulo, artista, duracion):
        nueva = Cancion(titulo, artista, duracion)
        if not self.cabeza:
            self.cabeza = nueva
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    def buscar(self, texto):
        """Busca coincidencias en título o artista."""
        texto = texto.lower()
        resultados = []
        actual = self.cabeza
        while actual:
            if texto in actual.datos["titulo"].lower() or texto in actual.datos["artista"].lower():
                resultados.append(actual)
            actual = actual.siguiente
        return resultados

    def eliminar(self, titulo):
        actual, anterior = self.cabeza, None
        while actual:
            if actual.datos["titulo"] == titulo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior, actual = actual, actual.siguiente
        return False

    def listar(self):
        resultado, actual = [], self.cabeza
        while actual:
            resultado.append(actual)
            actual = actual.siguiente
        return resultado
