import numpy as np

mat2 = [[0,0,0],[10,10,10],[10,10,10]]
#Laplacian Filter
#filter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

#Sobel-x
#filter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
#Sobel-y
filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

#Prewitt-x
#filter = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
#Prewitt-y
#filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

#Average Filter
#filter = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

val = 0

for l in range(0,3):
    for w in range(0,3):
        val += filter[l][w]*mat2[l][w]
        #print(filter[l][w], " ", mat2[l][w])
        
print("VAL", val)
        