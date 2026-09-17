class Cancion:
    """Nodo de la lista enlazada."""

    def __init__(self, titulo, artista, duracion):
        self.datos = {"titulo": titulo, "artista": artista, "duracion": duracion}
        self.siguiente = None

    def __str__(self):
        d = self.datos
        return f"{d['titulo']} - {d['artista']} ({d['duracion']})"
