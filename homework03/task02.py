# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
#  Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
#  Какова вероятность того, что 3 мяча белые?

import main

# возможные варианты - 2 белых из первого ящика, 1 белый из второго
# 1 белый из первого и 2 белых из второго
# 0 белых из первого и 3 белых из второго

two_one_white = (main.combination(5, 2) * main.combination(3, 0) / main.combination(8, 2)) * (main.combination(5, 1)*main.combination(7, 3)/main.combination(12, 4))
one_two_white = (main.combination(5, 1) * main.combination(3, 1) / main.combination(8, 2)) * (main.combination(5, 2)*main.combination(7, 2)/main.combination(12, 4))
zero_three_white = (main.combination(5, 0) * main.combination(3, 2) / main.combination(8, 2)) * (main.combination(5, 3)*main.combination(7, 1)/main.combination(12, 4))
three_white = two_one_white + one_two_white + zero_three_white

print(f'Вероятность, что 3 мяча белые - {round(three_white, 4)}')
