from tkinter import *
from tkinter import messagebox

def show_msg():

    messagebox.showinfo("Mensagem", "Ola Mundo!")

janela = Tk()

janela.title("Botoes")
janela.geometry("600x600")

btn_default = Button(janela, text="Click Here", bg="Black", fg="White", font="Arial 40")

#Command ->  Executa um código
btn_ola_mundo = Button(janela, text="Ola Mundo", command = show_msg)

btn_sair = Button(janela, text="Fechar a tela.", command = janela.destroy)

btn_default.pack()
btn_ola_mundo.pack()
btn_sair.pack()
janela.mainloop()