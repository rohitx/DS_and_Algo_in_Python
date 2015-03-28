'''
R-3.1: Graph th functions 8 n, 4 n log n, 2 n^2, n^3, and 2^n using a logarithmic
scale for the x- and y-axes; that is, if the function value f(n) is y, plot this
as a point with x-coordinate at log n and y-coordinate at log y.

'''
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 60)
y1 = 8*n
y2 = 4*n*np.log10(n)
y3 = 2*n**2
y4 = n**3
y5 = 2**n

plt.plot(n, y5, 'b-', label='2$^2$')
plt.plot(n, y1, 'r-', label='8n')
plt.plot(n, y2, 'g-', label='4nlog(n)')
plt.plot(n, y3, 'y-', label='2n$^2$')
plt.plot(n, y4, 'k-', label='n$^3$')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('log n')
plt.ylabel('log y')
plt.legend(numpoints=1, loc=2)
plt.show()
