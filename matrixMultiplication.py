import math
import cmath
z1 = complex(0,1)
z2 = complex(0,-1)

X = [
    [0,1,2,1],
    [1,2,3,2],
    [2,3,4,3],
    [1,2,3,2]]

'''X = [
    [0.5,0.5,0.5,0.5],
    [0,0,0,0],
    [0.5,0.5,0.5,0.5],
    [0,0,0,0]]'''

Y = [
    [1,1,1,1],
    [1,z2,-1,z1],
    [1,-1,1,-1],
    [1,z1,-1,z2]
    ]

y = [
    [1/4, 1/4, 1/4,  1/4],
    [1/4, z1/4, -1/4, z2/4],
    [1/4, -1/4, 1/4, -1/4],
    [1/4, z2/4, -1/4, z1/4],
    ]

r = 4
c = 4



result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]

result2 = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]

result3 = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]


def display(res):
    for i in range(r):
        for j in range(c):
            print(res[i][j], end = "   " )
        print("\n")

def multiply1(X,Y):
    for i in range(r):
    # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):

                #print(X[i][k], "    ", Y[k][j], "  ", i, j)
                result[j][i] +=  Y[k][j]*X[i][k]
                
def multiply2(X,Y):
    for i in range(r):
    # iterate through columns of Y
        for j in range(len(X[0])):
            # iterate through rows of Y
            for k in range(len(Y)):

                #print(X[i][k], "    ", Y[k][j], "  ", i, j)
                result2[j][i] +=  Y[k][j]*X[i][k]

multiply1(X,Y)
multiply2(result, Y)
display(result2)







