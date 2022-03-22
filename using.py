import numpy as np
from tabulate import tabulate
from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    name = ['Степень важности','Яндекс Go', 'maxim', 'Ситимобил', 'Gett', 'Uber Russia']
    char = ['Ср. стоимость поездки', 'Функциональная пригодность', 'Временные характеристики', 'Удобство использования', 'Уровень производительности', 'Сопровождаемость/модифицируемость',
            'Эффективность,результативность']
    m = np.array([[1, 92.6, 91.2, 86.2, 94.3, 100, 91.2],
                  [2, 79.3, 82.4, 81.3, 75.7, 91, 81.4],
                  [3, 82.1, 87.3, 92.1, 83.9, 85, 85.2],
                  [3, 85.3, 89.5, 91.3, 91.4, 97, 87.3],
                  [2, 88.7, 92.4, 87.5, 93.9, 100, 91.4]])
    wei = np.array([0.01, 0.4, 0.1, 0.15, 0.1, 0.7, 0.17])




    dh = DecisionHelper(m, wei)
    print("+------Исходная таблица------+")
    print(tabulate(np.row_stack((wei,m)), headers=char, tablefmt="grid", showindex=name, numalign="center"))
    print("+----------------------------+")
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
