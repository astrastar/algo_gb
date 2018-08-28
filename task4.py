# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры

n = int(input('Введите количество элементов: '))


def func(n):
    list = [1]
    for i in range(n - 1):
        a = list[i] / -2
        list.append(a)
    return sum(list)

print(func(n))