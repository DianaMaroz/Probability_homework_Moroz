# 3.На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен:
# a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

# Поскольку не укаано иное, будем считать, что в общем случае спортсмены стреляют равновероятно, т.е. вероятность выстрела для каждого равна 1/3

#Общая вероятность попадания

p_B = 1/3
p_AB1 = 0.9
p_AB2 = 0.8
p_AB3 = 0.6
p_A = p_AB1 * p_B +  p_AB2 * p_B + p_AB3 * p_B
p_B1A = p_AB1*p_B / p_A
p_B2A = p_AB2*p_B / p_A
p_B3A = p_AB3*p_B / p_A

print(f'Вероятность, что успешный выстрел произведен: \n'
      f'а) первым спортсменом - {round(p_B1A, 5)} \n'
      f'а) вторым спортсменом - {round(p_B2A, 5)} \n'
      f'а) третьим спортсменом - {round(p_B3A, 5)} ')