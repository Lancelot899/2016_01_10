#!/usr/bin/python
#coding = utf-8

from numpy import *


def loadDataSet(path):
    dataMat = []
    labelMat = []
    fr = open(path)
    for line in fr.readlines():
        lineArr = line.strip().replace('?', '0').split(' ')
        lineData = []
        for data in lineArr:
            lineData.append(float(data))
        lineData = lineData[0: len(lineData)]
        dataMat.append(lineData)
        labelMat.append(int(lineData[-1]))
    dataMat_ = mat(dataMat)
    labelVec = mat(labelMat).transpose()
    m, n =  shape(labelVec)
    labelVec -= ones((m,1))
    return dataMat_, labelVec

def sigmod(inX):
    return 1.0 / (1 + exp(-inX))

def gredient_decent(dataMat, labelVec, alpha = 0.001, maxCycle = 1000000):
    m,n = shape(dataMat)
    weights = ones((n, 1))
    for k in xrange(m):
        if k > maxCycle:
            break
        h = sigmod(dataMat * weights)
        error = labelVec - h
        weights = weights + alpha * dataMat.transpose() * error
    return weights

if __name__ == '__main__':
    dataSet, labels = loadDataSet('./horse-colic.data')
    print gredient_decent(dataSet, labels, 0.001, 1000000)
