# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

box1 = 10
balls1 = 7
box2 = 11
balls2 = 9

# Какова вероятность того, что все мячи белые?

# Вытаскиваем первый мяч из первого ящика с вероятностью p1:
p1 = balls1 / box1
print(f'Вытаскиваем первый мяч из первого ящика с вероятностью p1:\t{p1}')

# Вытаскиваем второй мяч из первого ящика с вероятностью p2:
p2 = (balls1 - 1) / (box1 - 1)
print(f'Вытаскиваем первый мяч из первого ящика с вероятностью p2:\t{p2}')

# Вытаскиваем первый мяч из второго ящика с вероятностью p3:
p3 = balls2 / box2
print(f'Вытаскиваем первый мяч из первого ящика с вероятностью p3:\t{p3}')

# Вытаскиваем второй мяч из второго ящика с вероятностью p4:
p4 = (balls2 - 1) / (box2 - 1)
print(f'Вытаскиваем первый мяч из первого ящика с вероятностью p4:\t{p4}')

# Что мячи были белыми нужно чтобы наступило И первое событие, И второе, И третье, И четвёртое.
# То есть нужно перемножить все вероятности:
p = p1 * p2 * p3 * p4
print(f'Вероятность вытащить все белые мячи:\t{p}')
# p = 0.3054545454545454 или чуть больше 30%.


# Какова вероятность того, что ровно два мяча белые?

# Данную задачу следует представить ввиде шести подзадач нахождения вероятностей:
# 1. Два мяча вытащены из первого ящика, из второго не вытащены.
# 2. Два мяча вытащены из второго ящика, из первого не вытащены.
# 3. Первый мяч из первого ящика, первый мяч из второго ящика.
# 4. Первый мяч из первого ящика, второй мяч из второго ящика.
# 5. Второй мяч из первого ящика, первый мяч из второго ящика.
# 6. Второй мяч из первого ящика, второй мяч из второго ящика.
p1 = (balls1 / box1) * ((balls1 - 1) / (box1 - 1)) * ((box2 - balls2) / box2) * ((box2 - balls2 - 1) / (box2 - 1))
p2 = ((box1 - balls1) / box1) * ((box1 - balls1 - 1) / (box1 - 1)) * (balls2 / box2) * ((balls2 - 1) / (box2 - 1))
p3 = (balls1 / box1) * ((box1 - balls1) / (box1 - 1)) * (balls1 / box2) * ((box2 - balls2) / (box2 - 1))
p4 = (balls1 / box1) * ((box1 - balls1) / (box1 - 1)) * ((box2 - balls2) / box2) * (balls2 / (box2 - 1))
p5 = ((box1 - balls1) / box1) * (balls1 / (box1 - 1)) * (balls1 / box2) * ((box2 - balls2) / (box2 - 1))
p6 = ((box1 - balls1) / box1) * (balls1 / (box1 - 1)) * ((box2 - balls2) / box2) * (balls2 / (box2 - 1))
# Для получения результирующей вероятности нужно сложить вычисленные вероятности,
# так как это несовестные благоприятствующие события:
p = p1 + p2 + p3 + p4 + p5 + p6
print(f'\n1. Два мяча вытащены из первого ящика, из второго не вытащены, вероятность p1:\t{p1}.'
      f'\n2. Два мяча вытащены из второго ящика, из первого не вытащены, вероятность p2:\t{p2}.'
      f'\n3. Первый мяч из первого ящика, первый мяч из второго ящика, вероятность p3:\t{p3}.'
      f'\n4. Первый мяч из первого ящика, второй мяч из второго ящика, вероятность p4:\t{p4}.'
      f'\n5. Второй мяч из первого ящика, первый мяч из второго ящика, вероятность p5:\t{p5}.'
      f'\n6. Второй мяч из первого ящика, второй мяч из второго ящика, вероятность p6:\t{p6}.'
      f'\nВероятность вытащить ровно два белых мяча:\t{p}.')
# p = 0.18787878787878787 или почти 19%.


# Какова вероятность того, что хотя бы один мяч белый?

# Решение данной задачи крайне трудоёмко, так как для нахождения вероятности необходимо вычислить все вероятности
# комбинаций, где количество белых шаров > 0.
# В данном случае рационально произвести вычисления от противного: вычислить вероятность, где количество белых шаров = 0
# и отнять её от 1, так как все остальные кобинации будут удовлетворять условию.
p1 = (box1 - balls1) / box1
p2 = (box1 - balls1 - 1) / (box1 - 1)
p3 = (box2 - balls2) / box2
p4 = (box2 - balls2 - 1) / (box2 - 1)
p = 1 - p1 * p2 * p3 * p4
print(f'\nВероятность вытащить первый не белый мяч из первой корзины:\t{p1}'
      f'\nВероятность вытащить второй не белый мяч из первой корзины:\t{p2}'
      f'\nВероятность вытащить первый не белый мяч из второй корзины:\t{p3}'
      f'\nВероятность вытащить второй не белый мяч из второй корзины:\t{p4}'
      f'\nВероятность вытащить хотя бы один белый мяч:\t{p}')
# p = 0.9987878787878788 или почти 99,8%.
