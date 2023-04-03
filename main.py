import time
from functions import addition, multiplication

self_name = 'Математический симулятор'


def main():
    print(f'Привет, я {self_name}, а тебя как зовут?')
    name = input('Введите имя: ')
    print(f'Приятно познакомиться, {name}.\nХочешь умножать или складывать?')
    game = input('Выберите игру (Умножение/Сложение): ')
    if game.lower() == 'сложение':
        range_1 = int(input('Выберите диапазон "до" первого числа: '))
        range_2 = int(input('Выберите диапазон "до" второго числа: '))
        print('Чтобы остановить игру, напиши: Стоп')
        time.sleep(2)
        print('Поехали!')
        time.sleep(1)
        return addition(range_1, range_2)
    if game.lower() == 'умножение':
        range_1 = int(input('Выберите диапазон "до" первого числа: '))
        range_2 = int(input('Выберите диапазон "до" второго числа: '))
        print('Чтобы остановить игру, напиши: Стоп')
        time.sleep(2)
        print('Поехали!')
        time.sleep(1)
        return multiplication(range_1, range_2)
    print('Выберите правильную операцию')
    return main()


main()
