def iter_to_dictionary(iterable: iter) -> dict:
    """
    Se utiliza qualquer iterável com iteráveis de dois termos (duplas) dentro
    para criar um dicionário com o primeiro o primeiro valor da dupla sendo a
    chave (key) do item e o segundo valor da dupla sendo o valor (value) do item

    EXEMPLO:
    iter_to_dictionary([('nome', 'Heitor'), ('idade', 17), ('altura', 1.72)])
    RETORNA {'nome': 'Heitor', 'idade': 17, 'altura': 1.72}

    :param iterable: Qualquer iterável que atenda aos requisitos
    :return: Retorna um dicionário
    """

    dictionary = {}
    for pair in iterable:
        dictionary.update({pair[0]: pair[1]})

    return dictionary


if __name__ == '__main__':

    my_iter = [('nome', 'Heitor'), ('idade', 17), ('altura', 1.72)]
    my_dict = iter_to_dictionary(my_iter)

    print(my_dict)
