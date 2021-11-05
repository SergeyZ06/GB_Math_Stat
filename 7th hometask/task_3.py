# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import numpy as np


def mse(b0_, b1_, x_, y_, n_):
    return np.sum((b0_ + b1_ * x_ - y_) ** 2) / n_


# Производная по B0:
def mse_p_b0(b0_, b1_, x_, y_, n_):
    return np.sum(b0_ + b1_ * x_ - y_) * 2 / n_


# Производная по B1:
def mse_p_b1(b0_, b1_, x_, y_, n_):
    return np.sum((b0_ + b1_ * x_ - y_) * x_) * 2 / n_


X = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
y = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
n = len(X)
X = np.array(X).reshape(n, 1)
y = np.array(y).reshape(n, 1)
# Первоначальные значения коэффициентов B0 и B1:
B0 = 1
B1 = 1
# Скорость обучения:
alpha = 0.00005

# Кортеж для хранения результатов итераций.
tuple_result = (0, 0, 0, 0)

amount_of_iterations = 500001

for i in range(amount_of_iterations):
    # Переопределение значений, чтобы избежать перекрёстного влияния коэффициентов.
    B0_prev = B0
    B1_prev = B1
    B0 = B0_prev - alpha * mse_p_b0(B0_prev, B1_prev, X, y, n)
    B1 = B1_prev - alpha * mse_p_b1(B0_prev, B1_prev, X, y, n)
    mse_current = mse(B0, B1, X, y, n)
    tuple_result = (i, B0, B1, mse_current)
    print(f'Iteration {tuple_result[0]}: \tB0 = {tuple_result[1]}, \tB1 = {tuple_result[2]},'
          f' \tmse = {tuple_result[3]}.')

# Iteration 500000: 	B0 = 444.17598171116276, 	B1 = 2.620549007524087, 	mse = 6470.414201656671.
