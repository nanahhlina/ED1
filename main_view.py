import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Biblioteca de Canciones")
        self.geometry("500x420")

        form = ttk.Frame(self)
        form.pack(fill="x", padx=10, pady=10)
        self.e_titulo = self._campo(form, "Título", 0)
        self.e_artista = self._campo(form, "Artista", 1)
        self.e_duracion = self._campo(form, "Duración", 2)
        ttk.Button(form, text="Añadir", command=self._agregar).grid(row=3, column=0, columnspan=2, pady=5)

        buscar = ttk.Frame(self)
        buscar.pack(fill="x", padx=10)
        self.e_buscar = ttk.Entry(buscar)
        self.e_buscar.pack(side="left", fill="x", expand=True)
        ttk.Button(buscar, text="Buscar", command=self._buscar).pack(side="left", padx=5)

        self.listbox = tk.Listbox(self, selectmode="extended")
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        botones = ttk.Frame(self)
        botones.pack(fill="x", padx=10, pady=5)
        ttk.Button(botones, text="Eliminar", command=self._eliminar).pack(side="left", padx=5)
        ttk.Button(botones, text="Crear playlist", command=self._crear_playlist).pack(side="left", padx=5)

        self._refrescar()

    def _campo(self, padre, etiqueta, fila):
        ttk.Label(padre, text=etiqueta).grid(row=fila, column=0, sticky="w")
        entry = ttk.Entry(padre)
        entry.grid(row=fila, column=1, sticky="ew", pady=2)
        padre.columnconfigure(1, weight=1)
        return entry

    def _refrescar(self, canciones=None):
        self.listbox.delete(0, tk.END)
        for c in canciones if canciones is not None else self.controller.obtener_biblioteca():
            self.listbox.insert(tk.END, str(c))

    def _titulos_seleccionados(self):
        return [self.listbox.get(i).split(" - ")[0] for i in self.listbox.curselection()]

    def _agregar(self):
        try:
            self.controller.agregar_cancion(self.e_titulo.get(), self.e_artista.get(), self.e_duracion.get())
            self.e_titulo.delete(0, tk.END)
            self.e_artista.delete(0, tk.END)
            self.e_duracion.delete(0, tk.END)
            self._refrescar()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def _buscar(self):
        self._refrescar(self.controller.buscar(self.e_buscar.get()))

    def _eliminar(self):
        for titulo in self._titulos_seleccionados():
            try:
                self.controller.eliminar_cancion(titulo)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        self._refrescar()

    def _crear_playlist(self):
        titulos = self._titulos_seleccionados()
        if not titulos:
            messagebox.showwarning("Playlist", "Selecciona canciones primero.")
            return
        nombre = simpledialog.askstring("Nueva playlist", "Nombre:", parent=self)
        if not nombre:
            return
        try:
            playlist = self.controller.crear_playlist(nombre, titulos)
            ventana = tk.Toplevel(self)
            ventana.title(playlist.nombre)
            lb = tk.Listbox(ventana)
            lb.pack(fill="both", expand=True)
            for c in playlist.listar():
                lb.insert(tk.END, str(c))
        except ValueError as e:
            messagebox.showerror("Error", str(e))
