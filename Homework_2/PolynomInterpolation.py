import numpy as np
import matplotlib.pyplot as plt


# Исходная функция для аппроксимации
def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(np.sin(x))


# Собираем матрицу A вручную: столбцы 1, x, x^2, ..., x^degree
def build_matrix(x, degree):
    a = np.ones((len(x), 1))
    for i in range(1, degree + 1):
        a = np.column_stack((a, x ** i))
    return a


# Находим коэффициенты полинома
def fit_polynomial(x_data, y_data, degree):
    a = build_matrix(x_data, degree)
    # lstsq возвращает кучу всего, но нам нужен только вектор w
    w = np.linalg.lstsq(a, y_data, rcond=None)[0]
    return w


# Считаем значения полинома в точках x
def predict_polynomial(x, w):
    degree = len(w) - 1
    a = build_matrix(x, degree)
    return a @ w


# Среднеквадратичная ошибка
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def main():
    # Точки, по которым строим полиномы
    x_data = np.linspace(0, 5, 6)
    y_data = f(x_data)

    # Гладкая сетка для красивого графика
    x_plot = np.linspace(0, 5, 300)
    y_true = f(x_plot)

    # Цвета для линий
    colors = ['r', 'g', 'b', 'm', 'c']

    plt.figure(figsize=(12, 7))
    plt.plot(x_plot, y_true, 'k-', linewidth=3, label='Исходная функция f(x)')
    plt.scatter(x_data, y_data, color='red', s=100, zorder=5,
                label='Точки данных (6 шт.)')

    print("=" * 50)
    print(f"{'Степень':<10} {'Коэф.':<10} {'MSE':<15}")
    print("=" * 50)

    # Пробегаемся по степеням от 1 до 5
    for deg, color in zip([1, 2, 3, 4, 5], colors):
        w = fit_polynomial(x_data, y_data, deg)
        y_pred = predict_polynomial(x_plot, w)
        error = mse(y_true, y_pred)

        print(f"{deg:<10} {len(w):<10} {error:<15.6f}")

        plt.plot(x_plot, y_pred, color=color, linestyle='--', linewidth=1.5,
                 label=f'Степень {deg} (MSE={error:.3f})')

    print("=" * 50)

    # Покажем коэффициенты для 5-й степени
    w5 = fit_polynomial(x_data, y_data, 5)
    print("\nКоэффициенты для степени 5:")
    for i in range(len(w5)):
        print(f"  w{i} = {w5[i]:+.6f}")

    plt.title('Интерполяция сложной функции полиномами 1-5 степени')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()