# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step 1: 
Import the numpy module to use the built-in functions for calculation
### Step 2: 
Prepare the lists from each linear equations and assign in np.array()
### Step 3: 
Using the np.linalg.eig(),  we get two results (first is eigenvalue and second is eigenvector) of the given matrix.
### Step 4: 
End the program
## Program:
```
#Developed by: Rohith s
#RegisterNumber: 25008317
import numpy as np
a= np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
b,c = np.linalg.eig(a)
print("Eigen values are",b,"and","Eigen Vectors are",c)

```
## Output:
<img width="1302" height="175" alt="image" src="https://github.com/user-attachments/assets/c27bd6ab-bcb6-4d95-984f-249e88a20be6" />

## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
