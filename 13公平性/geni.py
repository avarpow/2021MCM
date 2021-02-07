import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline


def GiniIndex(p):
    '''基尼系数'''
    print(sorted(np.append(p, 0)))
    cum = np.cumsum(sorted(np.append(p, 0)))
    sum = cum[-1]
    print(sum)
    x = np.array(range(len(cum))) / len(p)
    y = cum / sum
    print(x)
    print(y)
    B = np.trapz(y, x=x)
    A = 0.5 - B
    G = A / (A + B)
    '''绘图'''
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', -0))
    ax.spines['left'].set_position(('data', 0))
    plt.xticks([0, 1.0])
    plt.yticks([1.0])
    # plt.axis('scaled')
    x_smooth = np.linspace(x.min(), x.max(), 100)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    ax.plot(x_smooth, y_smooth, color='black')
    ax.plot(x, x, color='black')
    ax.plot([0, 1, 1, 1], [0, 0, 0, 1], color='black')
    ax.fill_between(x, y)
    ax.fill_between(x, x, y, where=y <= x)
    # ax.set_xlabel('职位')
    # ax.set_ylabel('工资')
    plt.show()
    return G


a = {0.692231678, 0.604865727, 0.400560007, 0.888232389, 0.435880916, 0.44186524, 0.569818907, 0.179671533, 0.263131087, 0.256777553, 0.555905742,
     0.449678715, 0.156087969, 0.269505293, 0.747053679, 0.52501312, 0.491588083, 0.289762659, 0.311839404, 0.482538485, 0.474888507, 1.089070557, 0.424187297}
b = {1.447373173, 1.264701479, 0.837522793, 1.857187085, 0.911374565, 0.923887067, 1.191422795, 0.375671563, 0.550175453, 0.536890976, 1.16233204,
     0.940224104, 0.326361168, 0.56350315, 1.561999383, 1.097739282, 1.027851551, 0.605858865, 0.652018684, 1.008929929, 0.992934746, 2.277115534, 0.886924614, }
print(GiniIndex(list(a)))  # 0.27963407313931665
