from string import Template

class Hangman():

    def __init__(self, palavra, dica):
        self.palavra = palavra
        self.dica = dica
        self.hangman = ""
        self.acertos = []
        self.erros = []
        self.espacos = []

    def hangman_map(self, chute=""):
        self.espacos = []

        if chute in self.acertos or chute in self.erros:
            return f"A letra '{chute}' ja foi chutada, digite outra"

        elif chute not in self.palavra:
            self.erros.append(chute)

        elif chute in self.palavra and chute != "":
            self.acertos.append(chute)

        self.hangman = self.hangman_draw(self.erros)

        for i in self.palavra:
            if i in self.acertos:
                self.espacos.append(f" {i} ")

            else:
                self.espacos.append(f" _ ")

        return self.hangman + ''.join(self.espacos)

    def ganhou(self):
        if " _ " not in self.espacos and len(self.espacos) == len(self.palavra):
            return "Você Ganhou"
        elif len(self.erros) == 6:
            return "Você Perdeu"
        else:
            return True

    def hangman_draw(self, erros):
        hangman = Template("""
        Dica: ${dica}
        Letras Ja chutadas: 
            Erros:   ${erros} 
            Acertos: ${acertos}
            +----+
            |    |
            |    ${erro_1}
            |  ${erro_4} ${erro_2} ${erro_3}
            |   ${erro_5} ${erro_6}
            |
        ========= """)

        hangman = hangman.substitute(
            dica = self.dica,
            erros = erros,
            acertos = self.acertos,
            erro_1 = "O" if len(erros) > 0 else "",
            erro_2 = "|" if len(erros) > 1 else "",
            erro_3 = "/" if len(erros) > 2 else "",
            erro_4 = "\\" if len(erros) > 3 else "",
            erro_5 = "/" if len(erros) > 4 else "",
            erro_6 = "\\" if len(erros) > 5 else ""
        )

        return hangman