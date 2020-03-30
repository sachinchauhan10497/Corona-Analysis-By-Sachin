from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

data = [0, 2, 1, 22, 2, 1, 3, 5, 9, 15, 7, 12, 9, 16, 6, 14, 19, 25, 28, 59, 76, 69, 102, 66, 86, 78, 151, 143, 110]
growth_constant = 1.20


l = len(data)
x = np.linspace(0, l, num=l, endpoint=True)
f2 = interp1d(x, data, kind='cubic')
xnew = np.linspace(0, l, num=200, endpoint=True)
plt.plot(x, data, 'o', x, (growth_constant)**(x), '--',xnew, f2(xnew))
plt.legend(['Actual data', 'Theoretical exponential growth'], loc='best')
plt.show()