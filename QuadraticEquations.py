import math

"""
Решает квадратное уравнение ax² + bx + c = 0.
Возвращает строку с корнями или сообщением об их отсутствии.
"""
def solve_quadratic(a, b, c):

    d = b ** 2 - 4 * a * c

    if a == 0:
        # Уравнение не квадратное, а линейное: bx + c = 0
        if b == 0:
            return 'Уравнение не имеет решений' if c != 0 else 'Бесконечно много решений'
        x = -c / b
        return f'Линейное уравнение, x = {round(x, 3)}'

    if d < 0:
        return 'Нет вещественных корней'
    elif d == 0:
        x = -b / (2 * a)
        return f'x = {round(x, 3)}' # округляем до трёх знаков после запятой
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        return f'x1 = {round(x1, 3)}\nx2 = {round(x2, 3)}'


def main():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(solve_quadratic(a, b, c))

if __name__ == '__main__':
    main()