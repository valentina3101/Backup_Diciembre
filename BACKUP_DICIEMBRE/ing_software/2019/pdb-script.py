def sum(lst):
    """Devuelve la suma de los elementos de la lista lst"""
    sum = 0
    i = 0
    while lst != [] or i != len(lst) - 1:
        sum += lst.pop(i)
        i += 1
    return sum


if __name__ == '__main__':
    digits = [i for i in range(10)]
    print(sum(digits))
