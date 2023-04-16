import tkinter as tk

def submit_data():
    # Obtener los valores ingresados por el usuario
    val1 = entry1.get()
    val2 = entry2.get()
    val3 = entry3.get()
    val4 = entry4.get()
    # Cerrar la ventana emergente
    window.destroy()


# Crear la ventana emergente
window = tk.Tk()
window.title("Ingresar datos")

# Crear los campos de entrada de datos
label1 = tk.Label(window, text="Valor 1:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Valor 2:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

label3 = tk.Label(window, text="Valor 3:")
label3.pack()
entry3 = tk.Entry(window)
entry3.pack()

label4 = tk.Label(window, text="Valor 4:")
label4.pack()
entry4 = tk.Entry(window)
entry4.pack()

# Crear el botón de envío de datos
submit_button = tk.Button(window, text="Enviar", command=submit_data)
submit_button.pack()

# Mostrar la ventana emergente
window.mainloop()


