from tkinter import *


window = Tk()
window.title("Interface Gráfica")
window.geometry("600x600")

for linha in range(5):
    for coluna in range(3):
        tabela = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1
        )
        
        tabela.grid(row=linha, column=coluna)
        cria_label = Label(master=tabela, text=f"Linha: {linha}\nColuna: {coluna}", padx=5, pady=5)
        cria_label.pack()

#Mainloop -> No tkinter uma janela funciona como um loop infinito
window.mainloop()
