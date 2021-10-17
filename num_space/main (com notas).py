def num_space(num):
    from math import ceil

    cont = spaces = 0
    space_count = (len(str(int(num))) - 1) // 3  # Determina a quantidade de espaços que serão adicionados.
    """Caso o valor len str int "num" for 3, o resultado será 0, porque (3 - 1) // 3 == 2 // 3 == 0,
    e caso o valor seja 4, o resultado será 1, porque (4 - 1) // 3 == 3 // 3 = 1.
    Dessa maneira, só contará 1 espaço a mais para adicionar pra cada vez 
    que o valor do len for maior do que cada múltiplo de 3.
    Por exemplo: 7 terá 2 espaços, porque 7 é maior que 3 e maior que 6,
    ou seja, maior que 2 múltiplos de 3 (o 3 e o 6)."""

    inv_num_list = list(str(int(num))[::-1])  # Cria uma lista com cada caractere da string da parte intera de "num".

    while space_count > 0:  # Enquanto a quantidade de espaços para adicionar for maior que 1.
        cont += 3  # Conta 3 casas pra colocar um espaço.
        place = cont + spaces  # Lugar onde vai colocar o espaço.
        inv_num_list.insert(place, ' ')  # Adiciona o espaço na lista.
        spaces += 1  # Aumenta 1 na quantidade de espaços que já foram adicionados.
        """Caso tenha adicionado mais 1 espaço, a lista terá 1 casa a mais,
        portanto precisa contar 1 casa a mais no lugar onde for adicionar o espaço,
        por isso a variável "place" recebe a variável "cont" + a variável "spaces"."""
        space_count -= 1  # Diminui 1 na quantidade de espaços para adicionar.

    num_list = inv_num_list[::-1]  # Desinverte a lista.

    if num - int(num) == 0:  # Se o resto for 0,
        x = 0  # vão ser 0 digitos depois da vírgula.
    else:  # Se o resto NÃO for 0,
        x = len(str(num)) - len(str(int(num))) - 1  # vão ser (len str "num" - len str int "num") digitos depois da vírgula.
        num_list.append('.')  # Se tiver digitos depois da vírgula, adiciona um ponto.
    rest = str(ceil((num - int(num)) * 10 ** x))  # Pega os números depois da vírgula, tira a virgula e arredonda pra cima.
    if x > 0:  # Se tiver mais do que 0 digitos depois da vírgula.
        for c in range(0, x):
            num_list.append(rest[c])  # Adiciona à lista cada digito de "rest" de 0 até x.

    format_num = ''.join(num_list)
    return format_num


if __name__ == '__main__':
    print(num_space(input('Digite um número decimal: ')))