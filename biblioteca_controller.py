from models.biblioteca import Biblioteca
from models.playlist import Playlist


class BibliotecaController:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def agregar_cancion(self, titulo, artista, duracion):
        if not titulo or not artista or not duracion:
            raise ValueError("Completa título, artista y duración.")
        self.biblioteca.agregar(titulo, artista, duracion)

    def eliminar_cancion(self, titulo):
        if not self.biblioteca.eliminar(titulo):
            raise ValueError(f"No se encontró '{titulo}'.")

    def buscar(self, texto):
        return self.biblioteca.buscar(texto) if texto else self.biblioteca.listar()

    def obtener_biblioteca(self):
        return self.biblioteca.listar()

    def crear_playlist(self, nombre, titulos):
        if not nombre or not titulos:
            raise ValueError("Ponle un nombre y selecciona canciones.")
        playlist = Playlist(nombre)
        for cancion in self.biblioteca.listar():
            if cancion.datos["titulo"] in titulos:
                playlist.agregar(cancion)
        return playlist
