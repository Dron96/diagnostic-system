#from PyQt5 import QtWidgets, QtGui
#import sys
import Raspoznavanie as R
import Func as F


data = []
with open('file.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        data.append(line.split(' '))
headers = (data[0][:])


dat = []
#Записываем числовые значения в отдельный массив
for i in range(1,len(data)):
    dat.append([])
    for j in range (len(data[0])):
        dat[i-1].append(float(data[i][j]))

#Записываем индексы первого и второго класса в разные массивы
    ind1 = []
    ind0 = []
    for i in range(len(dat)):
        if round(dat[i][0]) == 1:
            ind1.append(i)
        else:
            ind0.append(i)

#Числовые характеристики классов
sr0 = []
dis0 = []
for j in range(1,len(dat[0])):
        sr0.append(F.sredn(dat, ind0, j))
        dis0.append(F.disp(dat, ind0, j))

sr1 = []
dis1 = []
for j in range(1,len(dat[0])):
        sr1.append(F.sredn(dat, ind1, j))
        dis1.append(F.disp(dat, ind1, j))
#print(sr1)
#print(dis1)
#
#print(F.vnklras(dat, ind0))
# print(F.vnklras(dat, ind1))
#
# print(F.mezhklras(sr0, sr1))

f = [160, 80.0]
# print(sr0)
# print(sr1)
wmin = R.minras(sr0, sr1)
istmin = R.kachras(wmin, sr0, dat, ind0, 0)
lozhmin = R.kachras(wmin, sr1, dat, ind1, 1)
chuvmin = ist[0]/(ist[0]+ist[1])
specmin = lozh[0]/(lozh[1]+lozh[0])
print(wmin)
print(sr0)
print(sr1)
print(ist)
print(lozh)
print(chuv)
print(spec)
print()


w = R.perceptron(dat, ind0, ind1, 90000)
ist = R.kachras(w, sr0, dat, ind0, 0)
lozh = R.kachras(w, sr1, dat, ind1, 1)
chuv = ist[0]/(ist[0]+ist[1])
spec = lozh[0]/(lozh[1]+lozh[0])
#
# print(w)
# print(sr1)
# print(ist)
# print(lozh)
# print(chuv)
# print(spec)