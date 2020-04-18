import matplotlib.pyplot as plt
import numpy as np

# b = 4
# p = 1/25
# for n in range(1,10):
#     pf = (1-p)**n
#     ex = (pf * 4 + (1 - pf) * n * 4) / n
#     print(str(n) + " - " + str(ex))

q = 24/25
data = []
x = []
for n in range(1,25):
    x.append(n)
    v = ((q**n + (1-q**n) * n) / n)
    data.append(v)

plt.plot(x,data, linewidth=3)
# plt.legend(['Actual data', 'Theoretical exponential growth - ' + str(growth_constant) + "^x" ], loc='best' ,fontsize=20)
plt.ylabel('Expected Number of Tests of 1 person', fontsize=20)
plt.xlabel('N \n (N tests at a time)', fontsize=20)
plt.title("Expected cost of N Covid-19 tests at time \n With p = 1/25" , fontsize=25)
plt.grid()
plt.show()



