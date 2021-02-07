import numpy as np
import pandas
import matplotlib.pyplot as plt
import copy
b = []
for i in range(2012, 2031):
    b.append(i)
a = [75.89, 79.54, 79.67, 82.97, 81, 82.5, 81.29, 82.95, 84.08]
ratea = 0.012892881
rateb = 0.033483761
a_up = copy.deepcopy(a)
for i in range(0, 10):
    a.append(a[-1]*(1+ratea))
    a_up.append(a_up[-1]*(1+rateb))
print(len(a))
print(len(b))
print(a)
print(b)
print(a_up)


# fig, ax = plt.subplots()
# ax.plot(b, a_up, color='r', linestyle='--')
# ax.plot(b, a, color='black')
# plt.axis([2011, 2032, 70, 125])
# plt.show()
