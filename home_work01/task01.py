# 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import main

num_card = 52
num_clubs = 13
card = 4

all_clubs_probability = 1
for i in range(card):
      all_clubs_probability *= (num_clubs - i)/(num_card - i)
print(f'Вероятность того, что все 4 карты крести - '
      f'{round(all_clubs_probability, 4)} или {round(all_clubs_probability * 100, 2)}%')

# рассчитаем общее количество комбинаций из 4 карт из колоды в 52 карты
all_card_comb = main.combination(num_card, card)
# рассчитаем количество комбинаций из 4 карт, без тузов, т.е. от общего количества отнимем 4
without_aces_comb = main.combination((num_card - 4), card)
# разница между этими показателями и будет равна количеству комбинаций, которые будут содержать как минимум один туз
at_least_one_ace_comb = all_card_comb - without_aces_comb
# вероятность того, что из четырех карт, хотя бы один туз - отношение комбинаций с тузами к общему количеству комбинаций
at_least_one_ace_prob = at_least_one_ace_comb / all_card_comb

print(f'Вероятность того, что из 4 карт, хотя бы один туз'
      f' - {round(at_least_one_ace_prob, 4)} или {round(at_least_one_ace_prob * 100, 2)}%')
