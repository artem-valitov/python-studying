import math


# Исходная функция
def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(math.sin(x))


# Метод трапеций для интеграла от a до b с n разбиениями
def trapezoid(f, a, b, n):
    h = (b - a) / n

    # Крайние точки с половинным весом
    total = (f(a) + f(b)) / 2.0

    # Внутренние точки с весом 1
    for i in range(1, n):
        total = total + f(a + i * h)

    return h * total


def main():
    a = 0.0
    b = 1.0
    n = 100

    result = trapezoid(f, a, b, n)

    print("Метод трапеций")
    print("Пределы:", a, "->", b)
    print("Разбиений:", n)
    print("Шаг h =", (b - a) / n)
    print("Интеграл =", round(result, 6))


if __name__ == "__main__":
    main()