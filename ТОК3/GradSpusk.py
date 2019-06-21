import numpy as np
import math

def fun(x,y):
    z = np.exp((x**2+y**2))+2*x-3.5*y
    return z


#Метод Хуга-Дживса
def grad(x, y, e, h):

    for i in range(1, 1000):
        a = []
        a.append(fun(x, y))
        a.append(fun(x+h, y))
        a.append(fun(x-h, y))
        a.append(fun(x, y+h))
        a.append(fun(x, y-h))

        f = fun(x, y)

        m = a.index(min(a))

        if m == 0:
            h /= 2
            if h < 10**(-6):
                print('h меньше 0,000001')
                #return ['h мало', fun(x, y), x, y, i]
            else:
                continue
        if m == 1:
            x += h
        if m == 2:
            x -= h
        if m == 3:
            y += h
        if m == 4:
            y -= h

        print([fun(x,y), x, y, i-1])

        if (abs(fun(x,y)-f) < e):
            return [fun(x,y), x, y, i]
print('\t\tМетод Хуга-Дживса')
print('Введите x: ', end='')
x =float(input())
print('Введите y: ', end='')
y =float(input())
print('Введите шаг: ', end='')
h =float(input())
print('Введите погрешность: ', end='')
e =float(input())


print('\t\tОтвет')
ans = grad(x, y, e, h)
print('Точка минимума: (', round(ans[1], 3), ';', round(ans[2], 3), ')')
print('Значение функции: ', round(ans[0], 3))
print('Необходимое количество измерений: ', ans[3])