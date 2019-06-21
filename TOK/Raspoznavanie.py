import numpy as np
import random

def minras(cen0, cen1):
    w = []
    tmp = 0
    #Подсчитываем коэффициенты
    for i in range(len(cen0)):
        tmp += (cen0[i]**2 - cen1[i]**2)
        w.append(2*(cen1[i] - cen0[i]))
    #print(w)
    w.insert(0,tmp)
    #print(w)
    d = w[0]
    for i in range(len(cen0)):
        d += w[i+1]*cen0[i]
    if d < 0:
        for i in range(len(w)):
            w[i] *= -1
    return w

def perceptron(x, ind0, ind1, m):
    c = 0.01
    w = []
    l = 0
    kol = 0
    n = 0
    for i in range(len(x[0])):
        w.append(random.random())
    w = np.array(w)
    #Добавляем признак 1 и удаляем номер класса
    for i in range(len(x)):
        x[i].insert(1, 1)
        del x[i][0]
    #Перемножаем матрицы и находим d
    # print(w)
    for k in range(m):
        for i in range(len(x)):
            d = np.dot(w.transpose(),x[i])
            if i in ind0:
                if d < 0:
                    kol += 1
                    for j in range(len(x[0])):
                        w[j] += c * x[i][j]
            elif i in ind1:
                if d > 0:
                    kol += 1
                    for j in range(len(x[0])):
                        w[j] -= c * x[i][j]
            #print(d,'    ', w, '    ', x[i])
        n += 1
        if kol == 0:
            l += 1
        if l == 2:
            break
        #print(kol)
        kol = 0
    if l == 0:
        print('Количество ошибок не снижено до 0. Пожалуйста, увеличьте количество повторов.')
    print(n)
    return w


def oprkl(w, obj, n):
    d = w[0]
    #print(n)
    #Определяем к какому классу относится объект
    for i in range(1,n+1):
        #print(d, end= ' ')
        #print('     ',w[i],' ',obj[i],'    ',end=' ')
        d += w[i]*obj[i]
        #print(d, end=' ')
    if d > 0:
        return(1)
    elif d < 0:
        return(2)


def kachras(w, cen, d, ind, kl):
    c = 0
    a = 0
    z = 0
    for i in ind:
        z = oprkl(w, d[i], len(cen))
        if  z == kl:
            a += 1
        elif z != kl:
            c += 1
    return ([a, c])