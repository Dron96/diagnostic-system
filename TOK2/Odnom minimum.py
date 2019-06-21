from pylab import *
import math
import random

print('\tСравнение методов минимизации')
print('Введите количество измерений')
n = int(input())
print('Введите погрешность')
e = float(input())

t = (1+5**0.5)/2

dichLn = []
fibLn = []
ZSLn = []
I = []

def Fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return Fib(x-1) + Fib(x-2)

#Метод золотого сечения
for i in range(1,n+1):
    if i == 1:
        ZSLn.append(1)
    else:
        ZSLn.append(1/t**(i))
    I.append(i)

#Метод Фиббоначи
for i in range(1,n+1):
    if i == 1:
        fibLn.append(1)
    elif i == 2:
        fibLn.append((Fib(n - 1) / Fib(n) + ((-1) ** n / Fib(n)) * e))
    else:
        fibLn.append((1 / Fib(i) + (Fib(i-2) / Fib(i)) * e))

#Метод дихотомии
for i in range(1,n+1):
    if i == 1:
        dichLn.append(1)
    elif i == 2:
        dichLn.append(1/2+e/2)
    elif i > 2 and (i%2 == 0):
        dichLn.append(dichLn[i-2]/2 + e/2)
    else:
        dichLn.append(dichLn[i-2]) #Потому что массив все-таки начинается с индекса 0



# print(dichLn)
# print(fibLn)
# print(ZSLn)
# print(len(I), len(dichLn), len(fibLn), len(ZSLn))

figure()
plot(I, dichLn, label ='Дихотомия')
plot(I, fibLn, label = 'Фибоначчи')
plot(I, ZSLn, label = 'Золотое сечение')

legend(loc = 1)
xticks(range(len(I)+1))
xlabel('x')
ylabel('y')
title('Сравнение методов минимизации')
show()


def fun(x):
    f = math.exp(x)+x*x
    return f
def dfun(x):
    df = exp(x)+2*x
    return df
def d2fun(x):
    df = exp(x)+2
    return df

def zolsechmin(e, a = 0, b = 1):
    x1 = a + (2 - t) * (b - a)
    x2 = a+(t-1)*(b-a)

    f1 = fun(x1)
    f2 = fun(x2)

    i = 0
    min = 0
    while abs(b-a) >= e:
        if f1 <= f2:
            min = x1
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (2 - t) * (b - a)
            f1 = fun(x1)

        else:
            min = x2
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (t - 1) * (b - a)
            f2 = fun(x2)
        i = i + 1
    return ([min, fun(min), i])

def Parabola(a, b, e):
    x0 = random.randrange(a, b)
    x1 = x0 - (dfun(x0)/d2fun(x0))
    x = []
    x.append(x0)
    x.append(x1)
    for i in range(1,100):
        x.append(x[i]-(dfun(x[i])/d2fun(x[i])))
        if abs(fun(x[i+1])-fun(x[i]))<e:
            print(x)
            return [x[i+1], fun(x[i+1]), i+1]



print("\tАлгоритмы нахождения экстремума:\n\n\tАлгоритм золотого сечения:")
print("Введите погрешность:")
e = float(input())
print("Введите начало промежутка:")
a = float(input())
print("Введите конец промежутка:")
b = float(input())
#print("Ответ: [минимум, функция в точке минимуму, количество измерений]")
z = zolsechmin (e, a, b)
print('\tОтвет')
print('Минимум: ', round(z[0], 5))
print('Значение функции: ', round(z[1], 5))
print('Необходимое количество измерений: ', z[2])

print("\n\tМетод парабол:")
print("Введите погрешность:")
e = float(input())
print("Введите начало промежутка:")
a = float(input())
print("Введите конец промежутка:")
b = float(input())
p=Parabola(a, b, e)
print('\tОтвет')
print('Минимум: ', round(p[0], 5))
print('Значение функции: ', round(p[1], 5))
print('Необходимое количество измерений: ', p[2])




