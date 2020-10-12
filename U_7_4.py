import math
import random
def Rn(a):
    x=random.randint(0,10)
    if a==x:
        print(x)#для проверки
        print('Победа')
    else:
        print(x)  # для проверки
        print('Повторите ещё раз')
a=int(input('Введите число : '))
Rn(a)
