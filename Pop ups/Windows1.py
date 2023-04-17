import tkinter as tk

class VentanaEmergente:

    def __init__(self, parent):
        self.parent = parent
        self.valor1 = None
        self.valor2 = None
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Ventana Emergente")
        
        tk.Label(self.ventana, text="Valor 1:").grid(row=0, column=0)
        self.valor1_entry = tk.Entry(self.ventana)
        self.valor1_entry.grid(row=0, column=1)
        
        tk.Label(self.ventana, text="Valor 2:").grid(row=1, column=0)
        self.valor2_entry = tk.Entry(self.ventana)
        self.valor2_entry.grid(row=1, column=1)
        
        self.boton_continuar = tk.Button(self.ventana, text="Continuar", command=self.on_continuar)
        self.boton_continuar.grid(row=2, column=1)

        self.ventana.bind("<Return>", self.on_continuar)

        self.valor1_entry.focus_set()
        self.ventana.grab_set()

    def on_continuar(self, event=None):
        self.valor1 = self.valor1_entry.get()
        self.valor2 = self.valor2_entry.get()
        self.parent.focus_set()
        self.ventana.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    boton_mostrar = tk.Button(root, text="Mostrar ventana emergente", command=lambda: VentanaEmergente(root))
    boton_mostrar.pack()
    root.mainloop()
