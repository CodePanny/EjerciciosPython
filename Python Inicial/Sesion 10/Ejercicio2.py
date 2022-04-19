# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos
# seleccionables, también debe de tener un label con el texto que queráis.

import tkinter

window = tkinter.Tk()
list01 = tkinter.Listbox(window)


for food in ["Potatoes", "Coke", "Yogurt", "Ham", "Jam", "Carrots", "Bread", "Cereal", "Crisps"]:
    list01.insert(tkinter.END, food)

list01.pack()

label_example = tkinter.Label(text="Grocery list", bg='pink')
label_example.pack()
window.mainloop()
