from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import best_fit_a_rest_to_x as my

#India data
data = [0, 2, 1, 22, 2, 1, 3, 5, 9, 15, 7, 12, 9, 16, 6, 14, 19, 25, 28, 59, 76, 69, 102, 66, 86, 78, 151, 143, 110, 208, 288, 424, 486, 560, 566]

#Cumulative
# cul = 0
# for i in range(0,len(data)):
# 	cul = cul + data[i]
# 	data[i] = cul

# General Data
# data = []
# f = open("data",'r')
# for i in f:
# 	data.append(int(str(i.strip())))
# data = data[::-1]

growth_constant = my.bestA(data)
groeth_show_limit = len(data)

l = len(data)
x = np.linspace(0, l, num=l, endpoint=True)
f2 = interp1d(x, data, kind='cubic')
xnew = np.linspace(0, l, num=200, endpoint=True)

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(0, l+1, 1))
gMax = growth_constant**l
diff = int(gMax / 10)
diff =  diff - (diff % 10) 
ax.set_yticks(np.arange(0, gMax, diff))
plt.plot(x, data, 'o', x[0:groeth_show_limit], (growth_constant)**(x[0:groeth_show_limit]), '--',xnew, f2(xnew))
plt.legend(['Actual data', 'Theoretical exponential growth - ' + str(growth_constant) + "^x" ], loc='best' ,fontsize=20)
plt.xlabel('Time in Days since 1st March ', fontsize=20)
plt.ylabel('Number of Corona Positive Cases Reported', fontsize=20)
plt.title("Covid-19 in India" , fontsize=25)
plt.grid()
plt.show()