#Program to find the eigen values and eigen vectors.
#Developed by: Rohith s
#RegisterNumber: 25008317
import numpy as np
a= np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
b,c = np.linalg.eig(a)
print("Eigen values are",b,"and","Eigen Vectors are",c)
