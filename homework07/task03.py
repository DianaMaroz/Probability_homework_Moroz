# 3 ) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
# две зависимые выборки - критерий Уилкоксона

import numpy as np
from scipy import stats
pr1 = np.array([150, 160, 165, 145, 155])
pr2 = np.array([140, 155, 150,  130, 135])


result = stats.wilcoxon(pr1, pr2)
print(result)
if result[1] > 0.05:
    print('Различий нет с достоверностью 95%')
else:
    print('Различия значимы с достоверностью 95%')