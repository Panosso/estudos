def forca_tipo(*tipos):
    #str, int
    print(tipos)
    def decorador(funcao):
        #Aqui eu passo a função repete_msg
        def converte(*args, **kwargs):
            #Valor da variavel msg --> 'Teste de msg'
            #Valor da variavel vezes --> 10
            print(args)
            print(list(zip(args, tipos)))
            #('teste de msg', str), (10, int)
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                #Primeiro laço:
                # tipo = str
                # valor = 'Teste de msg'
                # novo_args = str('Tesde de msg')
                #
                #Segundo laço:
                # tipo = int
                # valor = 10
                # novo_args = int(10)
                #
                novo_args.append(tipo(valor))

            print(novo_args)
            print('Voltando pra função')
            return funcao(*novo_args, **kwargs)
            
        return converte

    return decorador
    

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    print('Voltei')
    print(msg * vezes)


repete_msg('Tesde de msg', 10)
