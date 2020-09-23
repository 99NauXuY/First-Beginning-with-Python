import numpy as np
zero = np.zeros(10)
one = np.ones(10)
five = np.ones(10)*5
tento = np.arange(10,51)
eventento = np.arange(10,51,2)
matrix = np.arange(9).reshape(3,3)
identity = np.eye(3)
randamnum = np.random.rand(1)
randomarr = np.random.rand(25)
procent = np.arange(1,101).reshape(10,10) / 100
linspace = np.linspace(0,1,20)
mat = np.arange(1,26).reshape(5,5)
#print(mat[2:,1:])
#print(mat[3,4])
#print(mat[:3,1])
#print(mat[3])
print(mat.sum())
#Berechnet Abweichung
print(mat.std())
print(mat.sum(axis=0))
