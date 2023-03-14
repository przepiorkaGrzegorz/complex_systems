import matplotlib.pyplot as plt
import random
import numpy as np
import time

# #zad1
# r = 2
#
# for x0 in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
#     x_tab = [x0]
#
#     for i in range(50):
#
#         x_tab.append(r*x_tab[-1]*(1 - x_tab[-1]))
#
#     plt.plot(x_tab, label='x0=' + str(x0))

# plt.legend(loc='lower right')
# plt.savefig("zad1.pdf")
# plt.show()
#
# #zad2
#
# for r in [1, 2, 3, 3.5, 3.55, 3.6]:
#      x_tab = [0.5]
#
#      for i in range(300):
#
#          x_tab.append(r*x_tab[-1]*(1 - x_tab[-1]))
#      plt.plot(x_tab[-25:], label='r=' + str(r))
#
#      plt.legend(loc='lower right')
#      plt.savefig("zad2_r=" + str(r) + ".pdf")
#      plt.show()
#
#zad3


if __name__ == "__main__":
    N = 1000
    r_tab = np.linspace(3.54, 3.55, 1000)

    for r in r_tab:
        x_tab = [0.5]
        for i in range(N):
            x_tab.append(r * x_tab[-1] * (1 - x_tab[-1]))

        u = np.unique(x_tab[round(0.9*N): N])
        r2 = r * np.ones(len(u))
        plt.plot(r2, u, 'k.')

    plt.savefig("zad3_3.pdf")
    plt.show()