def sredn(d, ind, zn):
    n = len(ind)
    sr = 0
    for i in ind:
        sr += d[i][zn]
    sr /= n
    return sr

def disp(d, ind, zn):
    n = len(ind)
    di = 0
    sr = sredn(d, ind, zn)
    for i in ind:
        di += (d[i][zn] - sr)**2
    di /= (n-1)
    di = di**0.5
    return di

def vnklras(d, ind):
    n = len(ind)
    sd = 0
    for j in range(1,len(d[0])):
        sd += disp(d, ind, j)**2
    sd *= 2
    return sd

def mezhklras(sr1, sr2):
    s=0
    for i in range(len(sr1)):
        s += (sr1[i] - sr2[i])**2
    s = s ** 0.5
    return s

