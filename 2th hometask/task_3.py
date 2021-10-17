# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

import math

p = 0.5
k = 70
n = 144

# Для решения данной задачи нужно использовать формулу Бернулли, так как это биномиальное распределение:
# - дискретная случайная велчина;
# - известна точная вероятность события;
# - небольшое число испытаний;
# - высокая вероятность наступления событий.

# Сочетание 70 из 144:
C_70_144 = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(f'Сочетание 70 из 144:\t{C_70_144}')

# p в степени k:
p_k = math.pow(p, k)
print(f'p в степени k:\t{p_k}')

# q = (1 - p) в степени (n - k):
q = math.pow(1 - p, n - k)
print(f'q = (1 - p) в степени (n - k):\t{q}')

# Результирующая вероятность:
P_X = C_70_144 * p_k * q
print(f'Результирующая вероятность:\t{P_X}')
# P_X = 0.06281178035144776 или чуть более 6,28%.
