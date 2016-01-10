#!/usr/bin/python
#coding = utf-8

from gredient_decent import *
from numpy import *

dataSet_tra, labels_tra = loadDataSet('./horse-colic.data')
dataSet_tst, labels_tst = loadDataSet('./horse-colic.test')
weights = gredient_decent(dataSet_tra, labels_tra)

def test():
    points = (dataSet_tst * weights).transpose()
    points = sigmod(points)
    m, n = shape(points)
    points = points - ones((1, n)) / 2
    err = 0;
    lstPoint = points.tolist()
    labels = labels_tst.tolist()
    for i in xrange(m):
        if lstPoint[0][i] < 0 & int(labels[0][i]) == 1:
                err += 1
        if lstPoint[0][i] > 0 & int(labels[0][i]) == 0:
                err += 1
    return err, n
            

err, sums = test()
print err, sums
print err / sums
