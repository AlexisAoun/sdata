import numpy as np

#exo 1
def g(x):
    return (x**3)*np.exp((x/4)-x**2)

def simNaive(nSim=10000):
    somme = 0
    for i in range(nSim):
        u = np.random.random()*200 - 100
        somme += g(u)
    return (200/nSim)*somme 

print(simNaive(1000000))

