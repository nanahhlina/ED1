import tkinter as tk

class VistaPolinomio:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Generador de Polinomio")

        tk.Label(self.ventana, text="Términos (formato: coef,exp coef,exp ...)").pack()
        self.entrada = tk.Entry(self.ventana, width=40)
        self.entrada.pack()

        tk.Button(self.ventana, text="Generar", command=self.generar).pack()

        self.resultado = tk.Label(self.ventana, text="")
        self.resultado.pack()

    def generar(self):
        texto = self.entrada.get()
        terminos = []
        for par in texto.split():
            coef, exp = par.split(",")
            terminos.append((float(coef), int(exp)))
        self.controlador.crear_polinomio(terminos)

    def mostrar_polinomio(self, polinomio):
        self.resultado.config(text=f"Polinomio: {polinomio}")

    def iniciar(self):
        self.ventana.mainloop()