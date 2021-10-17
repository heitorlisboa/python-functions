def num_space(num):
    from math import ceil

    cont = spaces = 0
    space_count = (len(str(int(num))) - 1) // 3

    inv_num_list = list(str(int(num))[::-1])

    while space_count > 0:
        cont += 3
        place = cont + spaces
        inv_num_list.insert(place, ' ')
        spaces += 1
        space_count -= 1

    num_list = inv_num_list[::-1]

    if num - int(num) == 0:
        x = 0
    else:
        x = len(str(num)) - len(str(int(num))) - 1
        num_list.append('.')
    rest = str(ceil((num - int(num)) * 10 ** x))
    if x > 0:
        for c in range(0, x):
            num_list.append(rest[c])

    format_num = ''.join(num_list)
    return format_num


if __name__ == '__main__':
    print(num_space(input('Digite um número decimal: ')))
