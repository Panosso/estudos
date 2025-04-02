from tkinter import *


window = Tk()
window.title("Interface Gráfica")
window.geometry("600x600")

rot1 = Label(window, text="\nPython", relief=RAISED, bg="green", foreground="white", font="Arial 40")

texto = """ Testo de mais
de uma linha
do python
"""

rot2 = Label(window, text=texto, relief=RAISED, font="Arial 40")

rot1.pack()
rot2.pack()

#Mainloop -> No tkinter uma janela funciona como um loop infinito
window.mainloop()
