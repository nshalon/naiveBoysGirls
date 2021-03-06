from genTrainFeatures import genTrainFeatures
from naivebayesCL import naivebayesCL
from classifyLinear import classifyLinear
import numpy as np

xTr, yTr = genTrainFeatures("girls.train.split", "boys.train.split")
w, b = naivebayesCL(xTr,yTr)

preds = classifyLinear(xTr, w, b)

print("train:", np.sum(yTr.ravel() == preds.ravel()) / yTr.shape[1])

xTe, yTe = genTrainFeatures("girls.test.split", "boys.test.split")

preds = classifyLinear(xTe, w, b)

print(ord("!"))
print("test:", np.sum(yTe.ravel() == preds.ravel()) / yTe.shape[1])




