def iter_to_dictionary(iter):
    """
    Se utiliza qualquer iterável com iteráveis de dois termos (duplas) dentro
    para criar um dicionário com o primeiro o primeiro valor da dupla sendo a
    chave (key) do item e o segundo valor da dupla sendo o valor (value) do item

    EXEMPLO:
    lista_para_dicionario([('nome', 'Heitor'), ('idade', 17), ('altura', 1.72)])
    RETORNA {'nome': 'Heitor', 'idade': 17, 'altura': 1.72}

    :param iter: Qualquer iterável que atenda aos requisitos
    :return: Retorna um dicionário
    """

    dictionary = {}
    for pair in iter:
        dictionary.update({pair[0]: pair[1]})

    return dictionary


if __name__ == '__main__':

    meu_iteravel = [('nome', 'Heitor'), ('idade', 17), ('altura', 1.72)]
    teste = iter_to_dictionary(meu_iteravel)
    
    print(teste)
