# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
#  от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
import math
x = 190
meanX = 178
dX = 25
stndX = math.sqrt(dX)
z = (x-meanX)/stndX
print(f'Рост человека, равный 190 см,от математического ожидания роста в популяции, на {round(z, 3)} сигм')