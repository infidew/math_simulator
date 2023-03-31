import random


def addition(range_a, range_b):
    a = random.randint(0, range_a)
    b = random.randint(0, range_b)
    c = a + b
    print(f'{a} + {b}')
    d = input('Ответ: ')
    if d.lower() == 'стоп':
        print('Игра остановлена')
        return
    elif d.lower() == 'again':
        return addition(range_a, range_b)
    elif int(d) == c:
        print('Верно!')
    else:
        print(f'Ошибка! Верный ответ: {c}')
    return addition(range_a, range_b)


def multiplication(range_a, range_b):
    a = random.randint(2, range_a)
    b = random.randint(2, range_b)
    c = a * b
    print(f'{a} * {b}')
    d = input('Ответ: ')
    if d.lower() == 'стоп':
        print('Игра остановлена')
        return
    elif d.lower() == 'again':
        return multiplication(range_a, range_b)
    elif int(d) == c:
        print('Верно!')
    else:
        print(f'Ошибка! Верный ответ: {c}')
    return multiplication(range_a, range_b)