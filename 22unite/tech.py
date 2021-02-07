import numpy as np
import pandas
import matplotlib.pyplot as plt
import copy
import random
import time
eg = [22.54, 23.49, 23.28, 23.08, 23.5, 22.71, 19.92, 22.07, 22.07]
nig = [19.24, 21.06, 23.03, 21.36, 22.32, 23.74, 26.55, 26.5, 25.04]
tur = [33.03, 37.11, 32.37, 38.26, 34.91, 35.77, 33.98, 33.91, 36.19]
sa = [1.08, 0.88, 0.99, 0.27, 0.27, 0.28, 0.84, 0.47, 0.78]
eg2 = []
nig2 = []
tur2 = []
sa2 = []
b = []
b2 = []
ratea = 0.005
for i in range(2012, 2021):
    b.append(i)
for i in range(2020, 2035):
    b2.append(i)
for i in range(0, 15):
    if i == 0:
        eg2.append(eg[-1]*(1+ratea))
        nig2.append(nig[-1]*(1+ratea))
        tur2.append(tur[-1]*(1+ratea))
        sa2.append(sa[-1]*(1+ratea))
    else:
        eg2.append(eg2[-1]*(1+ratea))
        nig2.append(nig2[-1]*(1+ratea))
        tur2.append(tur2[-1]*(1+ratea))
        sa2.append(sa2[-1]*(1+ratea))
    ratea += 0.002
fig, ax = plt.subplots()
print(eg2[10], nig2[10], tur2[10], sa2[10])
# ax.plot(b, eg, color='r', linestyle='--')
# plt.axis([2011, 2036, 18, 60])
# ax.plot(b, eg, color='black')
# ax.plot(b2, eg2, color='r', linestyle='--')
# plt.show()
# plt.axis([2011, 2036, 18, 50])
# ax.plot(b, nig, color='black')
# ax.plot(b2, nig2, color='r', linestyle='--')
# plt.show()
# plt.clf()
# plt.axis([2011, 2036, 30, 70])
# ax.plot(b, tur, color='black')
# ax.plot(b2, tur2, color='r', linestyle='--')
# plt.show()
# plt.clf()
# plt.axis([2011, 2036, 0, 2])
# ax.plot(b, sa, color='black')
# ax.plot(b2, sa2, color='r', linestyle='--')
# plt.show()
# plt.clf()
