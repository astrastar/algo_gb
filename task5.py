# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.


# q = 0
# while q < 10:
#     for i in range(32, 128):
#         pair = f' код: {i} - символ: {chr(i)} '
#         print(pair, end='\n')
#     q += 1


def func(start, stop, step):
    # start = 32
    # stop = 128
    # step = 10
    while start < stop - step:
        row = ''
        for i in range(start, start + step):
            pair = f' код: {i} - символ: {chr(i)} '
            row += pair
        print(row)
        start += step

func(32, 127, 10)