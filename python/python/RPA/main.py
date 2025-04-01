from tkinter import *

#tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Defeni um tamanho fixo para a tela
janela.geometry("600x600")

#Label - É onde escrevemos os textos que queremos que o usuário leia
instrucao = Label(text="\nOlá, mundo!", font="Arial 40")

#pack - Coloca os objetos dentro da janela / tela
instrucao.pack() #pack - cria e centraliza e deixa um em baixo do outro

#Label - É onde escrevemos os textos que queremos que o usuário leia
instrucao_2 = Label(text="\nCurso de TKinter!", font="Arial 40")

#pack - Coloca os objetos dentro da janela / tela
instrucao_2.pack() #pack - cria e centraliza e deixa um em baixo do outro


#Altera o título da tela
janela.title("Interface Gráfica")

#mainloop - No Tkinter uma janela funciona como um loop infinito
#A janela que o Python mostra na verdade é um programa em funcionamento
janela.mainloop()