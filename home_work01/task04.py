# 4. В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

num_ticket = 100
num_win = 2
ticket = 2

all_win_probability = 1
for i in range(ticket):
      all_win_probability *= (num_win - i)/(num_ticket - i)

print(f'Вероятность того, что  2 приобретенных билета окажутся выигрышными - '
      f'{round(all_win_probability, 5)} или {round(all_win_probability * 100, 3)}%')