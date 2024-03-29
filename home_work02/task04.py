# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?
import main

all_white = 7/10 * 6/9 * 9/11 * 8/10
print(f'Вероятность, что все шары белые -  {round(all_white, 4)}')

two_zero = 7/10 * 6/9 * 2/11 * 1/10
zero_two = 3/10 * 2/9 * 9/11 * 8/10
wb_wb = 7/10 * 3/9 * 9/11 * 2/10
wb_bw = 7/10 * 3/9 * 2/11 * 9/10
bw_wb = 3/10 * 7/9 * 9/11 * 2/10
bw_bw = 3/10 * 7/9 * 2/11 * 9/10
two_white = two_zero + zero_two + wb_bw + wb_wb + bw_bw + bw_wb
print(f'Вероятность, что ровно 2 шара белые -  {round(two_white, 4)}')

all_black = 3/10 * 2/9 * 2/11 * 1/10
at_least_one_white = 1 - all_black
print(f'Вероятность, что по меньшей мере 1 белый -  {round(at_least_one_white, 4)}')
