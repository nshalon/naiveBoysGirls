from genTrainFeatures import genTrainFeatures
from naivebayesCL import naivebayesCL
from classifyLinear import classifyLinear
import numpy as np

xTr, yTr = genTrainFeatures("girls.train.split", "boys.train.split")
w, b = naivebayesCL(xTr,yTr)

xTe, yTe = genTrainFeatures("girls.test.split", "boys.test.split")

preds = classifyLinear(xTe, w, b)

print(np.sum(yTe.ravel() == preds.ravel()) / yTe.shape[1])




