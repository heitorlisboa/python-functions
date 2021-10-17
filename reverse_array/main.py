def reverse_array(array):
    init = 0
    end = len(array) - 1
    while init < end:
        tmp = array[init]
        array[init] = array[end]
        array[end] = tmp

        init += 1
        end -= 1
    return array


if __name__ == '__main__':
    lista = [0, 1, 2, 3]
    print(reverse_array(lista))
