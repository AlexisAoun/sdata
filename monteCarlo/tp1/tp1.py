import numpy as np
import math

#exo 1
def simX(p=0.2):
    r = np.random.random()
    x = 0
    if r > p:
        x = 1
    return x

def monteCarlo(nSim = 10000):
    c = 0
    for i in range(nSim):
        x = simX() 
        if x == 0:
            c += 1
    res = c/nSim
    return res

#exo 2
def poisson(k,l):
    res = np.exp(-l)*(pow(l,k)/math.factorial(k))
    return res

def simXPoisson(l=2):
    r = np.random.random()
    x = 0
    p = poisson(x,l)
    while (r>p):
        x += 1
        p = p + poisson(x,l)
    return x


