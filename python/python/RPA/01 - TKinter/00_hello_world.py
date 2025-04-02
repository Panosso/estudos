from tkinter import Tk, Label


#TK - Biblioteca do TKinter
windows = Tk()

#Altera o título da tela.
windows.title("Interface Gráfica")

#Define o tamanho da janela.
windows.geometry("400x400")

#Cria um label
ola_mundo = Label(text="Ola Mundo", font="Arial 40")

#Adiciona o objeto a tela principal
ola_mundo.pack()

#Mainloop -> No tkinter uma janela funciona como um loop infinito
windows.mainloop()
