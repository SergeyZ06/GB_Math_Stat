# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].

import numpy as np


def mse(b1_, x_, y_, n_):
    return np.sum((b1_ * x_ - y_) ** 2) / n_


def mse_p(b1_, x_, y_, n_):
    return np.sum((b1_ * x_ - y_) * x_) * 2 / n_


X = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
y = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
n = len(X)
X = np.array(X).reshape(n, 1)
y = np.array(y).reshape(n, 1)
# Первоначальное значение коэффициента B1:
B1 = 0.1
# Скорость обучения:
alpha = 0.000001

# Кортеж для хранения результатов итераций.
tuple_result = (0, 0, 0)

amount_of_iterations = 1001

for i in range(amount_of_iterations):
    B1 = B1 - alpha * mse_p(B1, X, y, n)
    mse_current = mse(B1, X, y, n)

    # Для всех итераций начиная со второй, если mse перестала убывать:
    if i > 0 and mse_current > tuple_result[2]:
        # вывести результат предпоследний итерации с наименьшей mse и завершить итерирование.
        print(f'Iteration {tuple_result[0]}: \tB1 = {tuple_result[1]}, \tmse = {tuple_result[2]}.')
        break

    tuple_result = (i, B1, mse_current)

# Iteration 628: 	B1 = 5.889820285147628, 	mse = 56516.85841571966.
