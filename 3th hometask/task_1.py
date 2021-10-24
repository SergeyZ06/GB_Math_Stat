# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

import math
import numpy as np


list_salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
n = len(list_salary)

expected_value = 0
for salary in list_salary:
    expected_value += salary
expected_value = expected_value / n
# expected_value = 65.3

variance_shifted = 0
for salary in list_salary:
    variance_shifted += math.pow(salary - expected_value, 2)
variance_shifted = variance_shifted / n
# variance_shifted = 950.11

standard_deviation_shifted = math.sqrt(variance_shifted)
# standard_deviation_shifted = 30.823854398825596

variance = 0
for salary in list_salary:
    variance += math.pow(salary - expected_value, 2)
variance = variance / (n - 1)
# variance = 1000.1157894736842

standard_deviation = math.sqrt(variance)
# standard_deviation = 31.624607341019814

print(f'expected_value:\t\t\t\t{expected_value}\n'
      f'variance_shifted:\t\t\t{variance_shifted}\n'
      f'standard_deviation_shifted:\t{standard_deviation_shifted}\n'
      f'variance:\t\t\t\t\t{variance}\n'
      f'standard_deviation:\t\t\t{standard_deviation}\n')


# Checking with NumPy:
np_expected_value = np.mean(list_salary)
# np_expected_value = 65.3
np_variance_shifted = np.var(list_salary)
# np_variance_shifted = 950.1
np_standard_deviation_shifted = np.std(list_salary)
# np_standard_deviation_shifted = 30.823854398825596
np_variance = np.var(list_salary, ddof=1)
# np_variance = 1000.1157894736842
np_standard_deviation = np.std(list_salary, ddof=1)
# np_standard_deviation = 31.624607341019814

print(f'Checking with NumPy:\n'
      f'np_expected_value:\t\t\t\t{np_expected_value}\n'
      f'np_variance_shifted:\t\t\t{np_variance_shifted}\n'
      f'np_standard_deviation_shifted:\t{np_standard_deviation_shifted}\n'
      f'np_variance:\t\t\t\t\t{np_variance}\n'
      f'np_standard_deviation:\t\t\t{np_standard_deviation}')
