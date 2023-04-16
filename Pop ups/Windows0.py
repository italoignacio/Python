import numpy as np
import tkinter as tk

def get_values():
    global entries
    values = [float(entry.get()) for entry in entries]
    get_values.np_array = np.array(values)
    print("Los valores ingresados son:", get_values.np_array)
    print("La suma de los valores es:", np.sum(get_values.np_array))

root = tk.Tk()

entries = []
for i in range(4):
    label = tk.Label(root, text=f"Ingrese el valor {i+1}: ")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

button = tk.Button(root, text="Aceptar", command=get_values)
button.pack()

root.mainloop()
a=get_values.np_array
print(a)
