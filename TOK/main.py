from interface import *
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import Raspoznavanie as R
import Func as F
import numpy as np

dat = []
headers = []
ind1 = []
ind0 = []


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global dat
        global headers
        global ind0
        global ind1
        self.ui.pushButton.clicked.connect(lambda: self.showDialog())
        print(dat)
        self.ui.pushButton_2.clicked.connect(lambda: self.chislhar(dat, headers, ind0, ind1))
        self.ui.pushButton_4.clicked.connect(lambda: self.raspozn(dat, ind0, ind1))
        self.ui.pushButton_3.clicked.connect(lambda: self.newobj())

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './')
        self.ui.lineEdit.setText(fname[0])
        data = []
        with open(fname[0], 'r') as f:
            for line in f:
                line = line.strip()
                data.append(line.split(' '))
        global headers
        headers = (data[0][:])
        global dat
        dat = []
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setRowCount(len(data)-1)
        # Устанавливаем заголовки таблицы
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        #Массив dat будет хранить все числовые значения
        for i in range(1, len(data)):
            dat.append([])
            for j in range(len(data[0])):
                dat[i - 1].append(float(data[i][j]))
                self.ui.tableWidget.setItem(i-1, j, QtWidgets.QTableWidgetItem(data[i][j]))
        return (dat)

    def table(self, num, a):
        if type(num) == float:
            num = round(num, 3)
        tab = QtWidgets.QTableWidgetItem(str(num))
        if a == 's':
            tab.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        elif a == 'r':
            tab.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        elif a == 'l':
            tab.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        return tab

    def chislhar(self, dat, headers, ind0, ind1):
        #Рассчитываем индексы классов
        for i in range(len(dat)):
            if round(dat[i][0]) == 1:
                ind0.append(i)
            else:
                ind1.append(i)
        # Числовые характеристики 0 класса
        sr0 = []
        dis0 = []
        for j in range(1, len(dat[0])):
            sr0.append(F.sredn(dat, ind0, j))
            dis0.append(F.disp(dat, ind0, j))
        # Числовые характеристики 1 класса
        sr1 = []
        dis1 = []
        for j in range(1, len(dat[0])):
            sr1.append(F.sredn(dat, ind1, j))
            dis1.append(F.disp(dat, ind1, j))

        #Заносим все в таблицу
        self.ui.tableWidget_2.setColumnCount((len(dat[0])-1)*2+1)
        self.ui.tableWidget_2.setRowCount(6)
        # Устанавливаем заголовки таблицы
        #self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget_2.setSpan(0, 1, 1, (len(dat[0])-1))
        self.ui.tableWidget_2.setItem(0, 1, self.table('Класс 1', 's'))
        self.ui.tableWidget_2.setItem(0, len(headers), self.table('Класс 2', 's'))
        self.ui.tableWidget_2.setSpan(0, len(dat[0]), 1, (len(dat[0]) - 1) * 2)
        for i in range(1, len(headers)):
            self.ui.tableWidget_2.setItem(1, i, self.table(headers[i], 's'))
            self.ui.tableWidget_2.setItem(1, i+len(headers)-1, self.table(headers[i],'s'))
        self.ui.tableWidget_2.setItem(2, 0, self.table("Среднее:", 'l'))
        self.ui.tableWidget_2.setItem(3, 0, self.table("Дисперсия:", 'l'))
        self.ui.tableWidget_2.setItem(4, 0, self.table("Внутриклас. рас.:", 'l'))
        self.ui.tableWidget_2.setItem(5, 0, self.table("Межклас. рас.:", 'l'))
        self.ui.tableWidget_2.setSpan(4, 1, 1, (len(dat[0]) - 1))
        self.ui.tableWidget_2.setSpan(4, len(dat[0]), 1, (len(dat[0]) - 1)*2)
        self.ui.tableWidget_2.setSpan(5, 1, 1, (len(dat[0]) - 1)*2)

        # Числовые характеристики классов
        sr0 = []
        dis0 = []
        for j in range(1, len(dat[0])):
            sr0.append(F.sredn(dat, ind0, j))
            dis0.append(F.disp(dat, ind0, j))

        sr1 = []
        dis1 = []
        for j in range(1, len(dat[0])):
            sr1.append(F.sredn(dat, ind1, j))
            dis1.append(F.disp(dat, ind1, j))

        for i in range(len(sr0)):
            self.ui.tableWidget_2.setItem(2, i+1, self.table(sr0[i], 'r'))
            self.ui.tableWidget_2.setItem(3, i + 1, self.table(dis0[i], 'r'))
        for i in range(len(sr1)):
            self.ui.tableWidget_2.setItem(2, i+len(sr1)+1, self.table(sr1[i], 'r'))
            self.ui.tableWidget_2.setItem(3, i+len(sr1)+1, self.table(dis1[i], 'r'))

        self.ui.tableWidget_2.setItem(4, 1, self.table(F.vnklras(dat, ind0), 's'))
        self.ui.tableWidget_2.setItem(4, len(sr0)+1, self.table(F.vnklras(dat, ind1), 's'))
        self.ui.tableWidget_2.setItem(5, 1, self.table(F.mezhklras(sr0, sr1), 's'))

    def raspozn(self, dat, ind0, ind1):

        # Числовые характеристики классов
        sr0 = []
        dis0 = []
        for j in range(1, len(dat[0])):
            sr0.append(F.sredn(dat, ind0, j))
            dis0.append(F.disp(dat, ind0, j))

        sr1 = []
        dis1 = []
        for j in range(1, len(dat[0])):
            sr1.append(F.sredn(dat, ind1, j))
            dis1.append(F.disp(dat, ind1, j))

        global wmin
        global w

        wmin = R.minras(sr0, sr1)
        ist = R.kachras(wmin, sr0, dat, ind0, 1)
        lozh = R.kachras(wmin, sr1, dat, ind1, 2)
        chuvmin = ist[0] / (ist[0] + ist[1])
        specmin = lozh[0] / (lozh[1] + lozh[0])
        perosmin = (ist[0] + lozh[0]) / (ist[0] + ist[1] + lozh[0] + lozh[1])


        w = R.perceptron(dat, ind0, ind1, 90000)
        ist = R.kachras(w, sr0, dat, ind0, 1)
        lozh = R.kachras(w, sr1, dat, ind1, 2)
        chuv = ist[0] / (ist[0] + ist[1])
        spec = lozh[0] / (lozh[1] + lozh[0])
        peros = (ist[0]+lozh[0]) / (ist[0]+ist[1]+lozh[0]+lozh[1])

        self.ui.tableWidget_3.setColumnCount(len(dat[0])+1)
        self.ui.tableWidget_3.setRowCount(6)

        self.ui.tableWidget_3.setSpan(0, 0, 1, (len(wmin) + 1))
        self.ui.tableWidget_3.setItem(0, 0, self.table("Минимум расстояния", 's'))
        for i in range(len(wmin)):
            self.ui.tableWidget_3.setItem(1, i + 1, self.table(i, 'r'))
            self.ui.tableWidget_3.setItem(2, i + 1, self.table(wmin[i], 'r'))
        self.ui.tableWidget_3.setItem(2, 0, self.table('Коэффициенты:', 's'))


        self.ui.tableWidget_3.setSpan(3, 0, 1, (len(w) + 1))
        self.ui.tableWidget_3.setItem(3, 0, self.table("Перцептрон", 's'))
        self.ui.tableWidget_3.setItem(5, 0, self.table('Коэффициенты:', 's'))
        for i in range(len(w)):
            self.ui.tableWidget_3.setItem(5, i + 1, self.table(float(w[i]), 'r'))
            self.ui.tableWidget_3.setItem(4, i + 1, self.table(i, 'r'))

        self.ui.tableWidget_4.setColumnCount(2)
        self.ui.tableWidget_4.setRowCount(8)

        self.ui.tableWidget_4.setSpan(0, 0, 1, 2)
        self.ui.tableWidget_4.setItem(0, 0, self.table("Минимум расстояния", 's'))
        self.ui.tableWidget_4.setItem(1, 0, self.table('Se=', 'l'))
        self.ui.tableWidget_4.setItem(2, 0, self.table('Sp=', 'l'))
        self.ui.tableWidget_4.setItem(3, 0, self.table('Процент ошибок:', 'l'))
        self.ui.tableWidget_4.setItem(1, 1, self.table(chuvmin, 'r'))
        self.ui.tableWidget_4.setItem(2, 1, self.table(specmin, 'r'))
        self.ui.tableWidget_4.setItem(3, 1, self.table(100 - (perosmin*100), 'r'))

        self.ui.tableWidget_4.setSpan(4, 0, 1, 2)
        self.ui.tableWidget_4.setItem(4, 0, self.table("Перцептрон", 's'))
        self.ui.tableWidget_4.setItem(5, 0, self.table('Se=', 'l'))
        self.ui.tableWidget_4.setItem(6, 0, self.table('Sp=', 'l'))
        self.ui.tableWidget_4.setItem(7, 0, self.table('Процент ошибок:', 'l'))
        self.ui.tableWidget_4.setItem(5, 1, self.table(chuv, 'r'))
        self.ui.tableWidget_4.setItem(6, 1, self.table(spec, 'r'))
        self.ui.tableWidget_4.setItem(7, 1, self.table(100 - (peros*100), 'r'))


    def newobj(self):
        self.ui.label_4.setText("По минимуму расстояния объект относится к ")
        s = self.ui.textEdit.toPlainText()
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = float(s[i])
        s.insert(0, 1)
        p = R.oprkl(w, s, len(s)-1)
        m = R.oprkl(wmin, s, len(s)-1)


        self.ui.label_4.setText("По минимуму расстояния объект относится к "+ str(m) + ' классу')
        self.ui.label_5.setText("По перцептрону объект относится к " + str(p) + ' классу')







if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
