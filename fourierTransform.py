import numpy as np
import math
arr = np.array([[1,2],[3,4]])
res = arr.copy()
r,c = arr.shape

def changeVal(arr, u , v):
    sumval = 0
    for x in range(r):
        for y in range(c):
            e = pow(-1,2*(u*x+v*y)/r)
            ans = arr[x][y]*e
            sumval += ans
            #print(ans)
    return sumval/r


for i in range(r):
    for j in range(c):
        res[i][j] = changeVal(arr,i,j)

print(res)