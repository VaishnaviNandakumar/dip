import math
import cmath


def display(res):
    for i in range(3):
        for j in range(3):
            print(res[i][j], end = "   " )
        print("\n")


D = [
[1.414,1,1.414],
[1, 0, 1],
[1.414,1,1.414]]

#Butterworth
n = 2
D0 = 1.2
butterworth = [
[0,0,0],
[0,0,0],
[0,0,0]]

gaussian = [
[0,0,0],
[0,0,0],
[0,0,0]]

#Butterworth
for i in range(3):
    for j in range(3):
        x = (D[i][j]/D0)**(2*n)
        butterworth[i][j] = 1/(1+x)

display(butterworth)

#Gaussian
for i in range(3):
    for j in range(3):
        x = (-1*(D[i][j]**2))/(2*(D0**2))
        gaussian[i][j] = math.exp(x)

#display(gaussian)