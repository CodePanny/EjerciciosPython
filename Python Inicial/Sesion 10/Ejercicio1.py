# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que
# contenga un botón de reinicio para que lo deje como al principio
# Al principio no tiene que haber una opción seleccionada.

from tkinter import *


def reset():
    select.set('None')


window = Tk()
select = StringVar()
select.set('None')

Radiobutton(window, text="Red", variable=select, value='Red').pack(anchor=N)
Radiobutton(window, text="Blue", variable=select, value='Blue').pack(anchor=N)
Radiobutton(window, text="Yellow", variable=select, value='Yellow').pack(anchor=N)
Radiobutton(window, text="Purple", variable=select, value='Purple').pack(anchor=N)

Button(window, text="Restart", command=reset).pack()

window.mainloop()
