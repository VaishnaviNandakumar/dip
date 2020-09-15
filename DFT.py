import math
import cmath
x = complex(0,-1)
N = 4
n = 3
k = 3
for i in range(0, n+1):
	for j in range(0, k+1):
		print(i,j, end = "                ")
		z = (i*j)/N
		X = 2*z*x
		ans = cmath.exp(X)
		print(int(ans.real), "  ", ans.imag)
