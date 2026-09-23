import numpy as np


# Генерируем n случайных чисел от low до high
def gen_data(n, low, high):
    return np.random.uniform(low, high, n)


# Среднее значение
def calc_mean(data):
    return np.sum(data) / len(data)


# Стандартное отклонение (выборочное, n-1)
def calc_std(data, mean):
    diff = data - mean
    return np.sqrt(np.sum(diff ** 2) / (len(data) - 1))


# 95% доверительный интервал для среднего: M ± 1.995 * sigma / sqrt(n)
def calc_interval(mean, std, n):
    se = std / np.sqrt(n)
    return mean - 1.995 * se, mean + 1.995 * se


def main():
    n = 100
    data = gen_data(n, 20, 200)

    m = calc_mean(data)
    sigma = calc_std(data, m)
    low, high = calc_interval(m, sigma, n)

    print("Количество чисел:", n)
    print("Среднее M =", round(m, 4))
    print("Отклонение sigma =", round(sigma, 4))
    print("95%-й интервал: [", round(low, 4), ";", round(high, 4), "]")


if __name__ == "__main__":
    main()