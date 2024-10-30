
def title_to_number(title):

    if len(set([x.isalpha() for x in title])) > 1:
        raise ValueError('Digite apenas letras')

    alfa = 'abcdefghijklmnopqrstuvwxyz'
    dicionario = dict([(x[1],x[0]+1) for x in enumerate(alfa)])

    title = title.lower()
    resultado = 0
    max_exponent = len(title)

    for i in (range(max_exponent)):
        n_value = max_exponent - i - 1
        resultado += (26**n_value)*dicionario[title[i]]
        
    return resultado

