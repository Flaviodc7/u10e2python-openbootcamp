import tkinter
from tkinter import ttk

window = tkinter.Tk()


lista = ['Fito Paez', 'Charly Garcia', 'Ricardo Mollo', 'Dario Estevanez', 'Beto Vazquez Infinity']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(window, text="Bonita selección")
label.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()
