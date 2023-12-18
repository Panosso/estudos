# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hangman

def chute_validacao():
    chute = str(input("Digite uma letra: ")).upper()[0]

    return chute

def hangman_start():
    palavra = str(input("Digite a palavra a ser colocada na força: ")).upper()
    dica = str(input("Dica: "))
    continuar = True
    jogo = hangman.Hangman(palavra, dica)

    print(jogo.hangman_map())

    while continuar:

        chute = chute_validacao()
        print(chute)
        print(jogo.hangman_map(chute))

        continuar = False if jogo.ganhou() in ("Você Ganhou", "Você Perdeu") else True

        if not continuar:
            print(f"Palavra: {palavra}")
            print(jogo.ganhou())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangman_start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
