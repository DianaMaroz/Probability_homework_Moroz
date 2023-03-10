# 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
import main
# рассчитаем количество возможных комбинаций из трех цифр,
# при этом порядок не имеет значение
symbol_amount = 10
num_amount = 3
num_comb = main.combination(10, 3)

# поскольку цифры не повторяются и попытка введения кода одна, то благоприятный исход равен 1
first_try_prob = 1/num_comb
print(f'Вероятность того, что человек, не знающий код, откроет дверь с первой попытки'
      f' - {round(first_try_prob, 4)} или {round(first_try_prob * 100, 2)}%')