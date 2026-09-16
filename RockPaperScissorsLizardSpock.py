import random

"""Возвращает название фигуры по её номеру."""
def get_word(n):
    if n == 1:
        return 'Камень'
    elif n == 2:
        return 'Ножницы'
    elif n == 3:
        return 'Бумага'
    elif n == 4:
        return 'Ящерица'
    else:
        return 'Спок'

"""
Играет один раунд против компьютера.
Возвращает строку с результатом.
"""
def game(user_word):
    n = random.randint(1, 5)
    pc_word = get_word(n)

    header = f'Пользователь: {user_word}, Компьютер: {pc_word}\n'

    # Ничья
    if user_word == pc_word:
        return header + 'Ничья!'

    # Победы пользователя
    if user_word == 'Камень' and pc_word == 'Ножницы':
        return header + 'Выиграл пользователь: камень ломает ножницы'
    if user_word == 'Камень' and pc_word == 'Ящерица':
        return header + 'Выиграл пользователь: камень давит ящерицу'

    if user_word == 'Ножницы' and pc_word == 'Бумага':
        return header + 'Выиграл пользователь: ножницы режут бумагу'
    if user_word == 'Ножницы' and pc_word == 'Ящерица':
        return header + 'Выиграл пользователь: ножницы обезглавливают ящерицу'

    if user_word == 'Бумага' and pc_word == 'Камень':
        return header + 'Выиграл пользователь: бумага накрывает камень'
    if user_word == 'Бумага' and pc_word == 'Спок':
        return header + 'Выиграл пользователь: бумага подставляет Спока'

    if user_word == 'Ящерица' and pc_word == 'Бумага':
        return header + 'Выиграл пользователь: ящерица ест бумагу'
    if user_word == 'Ящерица' and pc_word == 'Спок':
        return header + 'Выиграл пользователь: ящерица травит Спока'

    if user_word == 'Спок' and pc_word == 'Камень':
        return header + 'Выиграл пользователь: Спок испаряет камень'
    if user_word == 'Спок' and pc_word == 'Ножницы':
        return header + 'Выиграл пользователь: Спок ломает ножницы'

    # Победы компьютера
    if user_word == 'Ножницы' and pc_word == 'Камень':
        return header + 'Выиграл компьютер: камень ломает ножницы'
    if user_word == 'Ящерица' and pc_word == 'Камень':
        return header + 'Выиграл компьютер: камень давит ящерицу'

    if user_word == 'Бумага' and pc_word == 'Ножницы':
        return header + 'Выиграл компьютер: ножницы режут бумагу'
    if user_word == 'Ящерица' and pc_word == 'Ножницы':
        return header + 'Выиграл компьютер: ножницы обезглавливают ящерицу'

    if user_word == 'Камень' and pc_word == 'Бумага':
        return header + 'Выиграл компьютер: бумага накрывает камень'
    if user_word == 'Спок' and pc_word == 'Бумага':
        return header + 'Выиграл компьютер: бумага подставляет Спока'

    if user_word == 'Бумага' and pc_word == 'Ящерица':
        return header + 'Выиграл компьютер: ящерица ест бумагу'
    if user_word == 'Спок' and pc_word == 'Ящерица':
        return header + 'Выиграл компьютер: ящерица травит Спока'

    if user_word == 'Камень' and pc_word == 'Спок':
        return header + 'Выиграл компьютер: Спок испаряет камень'
    if user_word == 'Ножницы' and pc_word == 'Спок':
        return header + 'Выиграл компьютер: Спок ломает ножницы'

    # Сюда попасть невозможно, но на всякий случай
    return header + 'Что-то пошло не так'


def main():
    print('Варианты: Камень, Ножницы, Бумага, Ящерица, Спок')
    user_word = input('Ваш ход: ').strip().capitalize()

    valid = ('Камень', 'Ножницы', 'Бумага', 'Ящерица', 'Спок')
    if user_word not in valid:
        print('Некорректный ввод. Попробуйте ещё раз.')
        return

    print(game(user_word))


if __name__ == '__main__':
    main()