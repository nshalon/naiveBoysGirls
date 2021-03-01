#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayes(x, y, x1):
# =============================================================================
#function logratio = naivebayes(x,y,x1);
#
#Computation of log P(Y|X=x1) using Bayes Rule
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#x1: input vector of d dimensions (dx1)
#
#Output:
#logratio: log (P(Y = 1|X=x1)/P(Y=-1|X=x1))
# =============================================================================


    
    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    X1= np.matrix(x1)
    
    # Pre-configuring the size of matrix X
    d, n = X.shape

    pos_prior, neg_prior = naivebayesPY(X, y)
    pos_probs, neg_probs = naivebayesPXY(X, y)
    pos_posterior = np.sum(np.log(np.power(pos_probs, X1)))
    neg_posterior = np.sum(np.log(np.power(neg_probs, X1)))
    logratio = (pos_posterior + np.log(pos_prior)) - (neg_posterior + np.log(neg_prior))
    
    return logratio
