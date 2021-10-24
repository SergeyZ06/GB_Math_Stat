# Устройство состоит из трех деталей.
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

# Вероятность выхода из строя первой детали:
P_A1 = 0.1
# Вероятность выхода из строя второй детали:
P_A2 = 0.2
# Вероятность выхода из строя третьей детали:
P_A3 = 0.25


# Задача а). все детали
# (Выйдет из строя первая деталь) И (Выйдет из строя вторая деталь) И (Выйдет из строя третья деталь)
P_A = P_A1 * P_A2 * P_A3
# P_A = 0.005000000000000001
print(f'Вероятность выхода из строя трёх деталей в первый месяц:\t\t{P_A}')


# Задача б). только две детали

# Вероятность того, что из строя выйдут первая и вторая детали, а третья не выйдет:
P_B1 = P_A1 * P_A2 * (1 - P_A3)
# P_B1 = 0.015000000000000003

# Вероятность того, что из строя выйдут первая и третья детали, а вторая не выйдет:
P_B2 = P_A1 * (1 - P_A2) * P_A3
# P_B2 = 0.020000000000000004

# Вероятность того, что из строя выйдут вторая и третья детали, а первая не выйдет:
P_B3 = (1 - P_A1) * P_A2 * P_A3
# P_B3 = 0.045000000000000005

# Вероятность того, что из строя выйдут только две детали:
P_B = P_B1 + P_B2 + P_B3
# P_B = 0.08000000000000002

print(f'Вероятность того, что из строя выйдут только две детали:\t\t{P_B}')


# Задача в). хотя бы одна деталь
P_C = 1 - (1 - P_A1) * (1 - P_A2) * (1 - P_A3)
print(f'Вероятность того, что из строя выйдет хотя бы одна деталь:\t\t{P_C}')


# Задача г). от одной до двух деталей?

# Вероятность выхода из строя всех трёх делатей можно заимствовать из Задачи а:
P_D1 = P_A
# P_D1 = 0.005000000000000001

# Вероятность того, что ни одна деталь не выйдет из строя:
P_D2 = (1 - P_A1) * (1 - P_A2) * (1 - P_A3)
# P_D2 = 0.54

# Вероятность того, что из строя выйдут от одной до двух деталей:
P_D = 1 - P_D1 - P_D2
# P_D = 0.45499999999999996

print(f'Вероятность того, что из строя выйдут от одной до двух деталей:\t{P_D}')