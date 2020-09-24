import numpy as np

#Input Matrix
mat = np.array([[0,0,0,0,0], [0,11,12,13,0],[0,12,1,16,0],[0,17,8,9,0], [0,0,0,0,0]])


#Laplacian Filter
filter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

#Sobel-x
#filter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
#Sobel-y
#filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

#Prewitt-x
#filter = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
#Prewitt-y
#filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

#Average Filter
#filter = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])


r1 , c1 = mat.shape
r2 , c2 = filter.shape

mat2 = []
ans = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0, c1-2):
    for j in range(0, r1-2):
        mat2 = []
        val = 0
        for k in range(i, i+3):
            l = []
            for q in range(j, j+3):
                
                l.append(mat[k][q])
            mat2.append(l)
        
        #print("Val", i, j, "  ", mat2, "\n")
        #Apply filter
        for l in range(0,r2):
            for w in range(0,c2):
                
                val += filter[l][w]*mat2[l][w]
                #print(filter[l][w], " ", mat2[l][w])
        #print("VAL", val, "\n", i, j)
        ans[i][j] = val


print(ans)




