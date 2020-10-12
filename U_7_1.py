import math
def Geron(a,b,c):
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Площадь треугольника = ',S)
a,b,c=map(int,input('Введите три стороны ').split())
Geron(a,b,c)

