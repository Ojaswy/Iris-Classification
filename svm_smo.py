# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:52:03 2018

@author: ssoder
"""

"""
******************************************************************************
Platt's Pseudo-code for calculation of a Support Vector Machine
    utilizing the Sequential Minimal Optimization Algorithm.

J. Platt. Sequential Minimal Optimization: A Fast Algorithm for 
    Training Support Vector Machines. 
    Microsoft Research
    Technical Report MSR-TR-98-14, April 21, 1998.
    
Modification to second choice heuristic taken from:
G. Mak. The Implementation of Support Vector Machines using the Sequential
    Minimal Optimization Algorithm.
    School of Computer Science, McGill University
    Master's Thesis, April 2000

******************************************************************************
main routine:
    numChanged = 0;
    examineAll = 1;
    while (numChanged > 0 | examineAll)
    {
        numChanged = 0;
        if (examineAll)
            loop I over all training examples
                numChanged += examineExample(I)
        else
            loop I over examples where alpha is not 0 & not C
                numChanged += examineExample(I)
        if (examineAll == 1)
            examineAll = 0
            else if (numChanged == 0)
            examineAll = 1
    }

procedure examineExample(i2)
    y2 = target[i2]
    alph2 = Lagrange multiplier for i2
    E2 = SVM output on point[i2] – y2 (check in error cache)
    r2 = E2*y2
    if ((r2 < -tol && alph2 < C) || (r2 > tol && alph2 > 0))
    {
        if (number of non-zero & non-C alpha > 1)
        {
            i1 = result of second choice heuristic (section 2.2)
            if takeStep(i1,i2)
                return 1
        }
        loop over all non-zero and non-C alpha, starting at a random point
        {
            i1 = identity of current alpha
            if takeStep(i1,i2)
                return 1
        }
        loop over all possible i1, starting at a random point
        {
            i1 = loop variable
            if (takeStep(i1,i2)
                return 1
        }
    }
    return 0
endprocedure

target = desired output vector
point = training point matrix

procedure takeStep(i1,i2)
    if (i1 == i2) return 0
    alph1 = Lagrange multiplier for i1
    y1 = target[i1]
    E1 = SVM output on point[i1] – y1 (check in error cache)
    s = y1*y2
    Compute L, H via equations (13) and (14)
    if (L == H)
        return 0
    k11 = kernel(point[i1],point[i1])
    k12 = kernel(point[i1],point[i2])
    k22 = kernel(point[i2],point[i2])
    eta = k11+k22-2*k12
    if (eta > 0)
    {
        a2 = alph2 + y2*(E1-E2)/eta
        if (a2 < L) a2 = L
        else if (a2 > H) a2 = H
    }
    else
    {
        Lobj = objective function at a2=L
        Hobj = objective function at a2=H
        if (Lobj < Hobj-eps)
            a2 = L
        else if (Lobj > Hobj+eps)
            a2 = H
        else
            a2 = alph2
    }
    if (|a2-alph2| < eps*(a2+alph2+eps))
        return 0
    a1 = alph1+s*(alph2-a2)
    Update threshold to reflect change in Lagrange multipliers
    Update weight vector to reflect change in a1 & a2, if SVM is linear
    Update error cache using new Lagrange multipliers
    Store a1 in the alpha array
    Store a2 in the alpha array
    return 1
endprocedure


"""






class svm(object):

    def __init__(self,kerneltype = 'linear',C=1,epsilon=0.001,d=None,sigma=None):
        self.kernels = {
            'linear' : self._linearkernel,
            'polynomial' : self._polykernel,
            'RBF' : self._rbfkernel
        }
        self.C = C
        self.epsilon = epsilon
        self.kerneltype = kerneltype
        self._maxiterations = 10,000

    def _initalize(self,X,Y):
        n_samples, n_features = X.shape
        lamult = np.zeros(n_samples+1)
        kij = self.kernels[self.kerneltype]
        weight = np.zeroes(n_features+1)
        nonbound = np.zeroes(n_samples+1)
        unboundindex = 0
        errorcache = 0
        nonzerolambda = 0

    def _labelcleaning(self,Y):
        targetlabels = []
        j=0








    def train(self,X,Y):
        numChanged = 0
        examineAll = 1
        count = 0
        self._initalize(X,Y)


        pass

    def classify(self):
        pass

    def _cleaninputs(self):
        #Check your inputs to make sure they work properly. Come back to this.
        pass

    def _examine(self):
        pass

    def _takestep(self,lm1,lm2):
        if lm1 == lm2:
            return 0
        y1 = target[lm1]
        pass

    def _linearkernel(self,xi,xj):
        return np.dot(xi,xj.T)

    def _polykernel(self,xi,xj,d):
        return (1+np.dot(xi,xj.T))**d

    def _rbfkernel(self,xi,xj,sigma):
        eqn = (-la.norm(xi-xj)**2)/(2*sigma**2)
        return exp(eqn)