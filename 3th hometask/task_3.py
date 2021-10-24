# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

# Вероятности попаданий каждого из спортсменов:
P_A1 = 0.9
P_A2 = 0.8
P_A3 = 0.6

# Вероятности выстрела каждого из спортсменов:
P_B1 = 1 / 3
P_B2 = 1 / 3
P_B3 = 1 / 3

# Полная вероятность попадания в мишень одним любым спортсменом:
P_A = P_B1 * P_A1 + P_B2 * P_A2 + P_B3 * P_A3
# P_A = 0.7666666666666666

# Вероятность, что в мишень попал первый спортсмен:
P_B1_A1 = P_B1 * P_A1 / P_A
# P_B1_A = 0.391304347826087

# Вероятность, что в мишень попал второй спортсмен:
P_B2_A2 = P_B2 * P_A2 / P_A
# P_B1_A = 0.3478260869565218

# Вероятность, что в мишень попал третий спортсмен:
P_B3_A3 = P_B3 * P_A3 / P_A
# P_B1_A = 0.2608695652173913

print(f'Вероятность, что в мишень попал первый спортсмен:\t{P_B1_A1}\n'
      f'Вероятность, что в мишень попал второй спортсмен:\t{P_B2_A2}\n'
      f'Вероятность, что в мишень попал третий спортсмен:\t{P_B3_A3}')
