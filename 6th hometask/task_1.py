# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import math
import numpy as np


zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

# Так как len(zp) = len(ks) вычислим n только для первого массива:
n = len(zp)

# Смещённая оценка мат. ожидания для zp:
M_zp = 0
for x in zp:
    M_zp += x
M_zp = M_zp / n
# M_zp = 101.4

# Смещённая оценка дисперсии для zp:
D_zp = 0
for x in zp:
    D_zp += math.pow(x - M_zp, 2)
D_zp = D_zp / n
# D_zp = 3494.6400000000003

# Смещённая оценка стандартного квадратичного отклонения для zp:
std_zp = math.sqrt(D_zp)
# std_zp = 59.115480206118605


# Смещённая оценка мат. ожидания для ks:
M_ks = 0
for x in ks:
    M_ks += x
M_ks = M_ks / n
# M_ks = 709.9

# Смещённая оценка дисперсии для ks:
D_ks = 0
for x in ks:
    D_ks += math.pow(x - M_ks, 2)
D_ks = D_ks / n
# D_ks = 30468.890000000007

# Смещённая оценка стандартного квадратичного отклонения для ks:
std_ks = math.sqrt(D_ks)
# std_ks = 174.55340157098058


# Для вычисления ковариации zp и ks вычислим их совместное несмещённое мат. ожидание:
M_zp_ks = 0
for i in range(n):
    M_zp_ks += zp[i] * ks[i]
M_zp_ks = M_zp_ks / n
# M_zp_ks = 81141.7

# Вычислим ковариацию для zp и ks:
cov_zp_ks_calculated = M_zp_ks - M_zp * M_ks
# cov_zp_ks_calculated = 9157.839999999997
print(f'cov_zp_ks_calculated = {cov_zp_ks_calculated}')

# Вычислим коэффициент корреляции:
cor_zp_ks_calculated = cov_zp_ks_calculated / (std_ks * std_zp)
# cor_zp_ks_calculated = 0.8874900920739158
print(f'cor_zp_ks_calculated = {cor_zp_ks_calculated}')


# Теперь воспользуемся библиотекой numpy:

cov_zp_ks_func = np.cov(zp, ks, ddof=0)[0][1]
# cov_zp_ks_func = 9157.84
print(f'cov_zp_ks_func = {cov_zp_ks_func}')

cor_zp_ks_func = np.corrcoef(zp, ks)[0][1]
# cor_zp_ks_func = 0.8874900920739162
print(f'cor_zp_ks_func = {cor_zp_ks_func}')
