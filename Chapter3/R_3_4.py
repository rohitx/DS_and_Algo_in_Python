'''
R-3.4: Give an example of a function that is plotted the same on a log-log scale
as it is on the standard scale.

Answer: the linear function: f(n) = n is an example of a function that is the
same on a log-log scale and on the standard scale.

'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.1)
y = x

plt.plot(x, y, 'r-')
#plt.yscale('log')
#plt.xscale('log')
plt.show()
