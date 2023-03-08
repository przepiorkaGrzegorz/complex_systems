import numpy as np
import matplotlib.pyplot as plt
import random

Time = 101
N = 61
survive = [3, 5, 6, 7, 8]
birth = [4, 6, 7, 8]
shots = [0, 1, 2, 5, 10, 50, 100]
table = np.zeros((N, N))


def start(table: np.ndarray):
    for i in range(N):
        for j in range(N):
            table[i][j] = random.randint(0, 1)

def neighNum(table: np.ndarray, i: int, j: int) -> int:
    return int(table[i][(j + 1) % N] + table[i][j - 1] + \
            table[(i + 1) % N][j - 1] + table[(i + 1) % N][j] + \
            table[(i + 1) % N][(j + 1) % N] + table[i - 1][(j + 1) % N] + \
            table[i - 1][j] + table[i - 1][j - 1])

def plot(table: np.ndarray, ver: int, t: int):
    plt.imshow(table)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, N-1)
    plt.ylim(0, N-1)
    plt.title(f"ver = {ver + 1}, t = {t}")
    plt.savefig(f"ver_{ver + 1}_time_{t}.jpg")


if __name__ == "__main__":

    for ver in range(3):
        start(table)

        for t in range(Time):
            tmp = np.zeros((N, N))

            for i in range(N):
                for j in range(N):
                    if neighNum(table, i, j) in birth and table[i][j] == 0:
                        tmp[i][j] = 1
                    if neighNum(table, i, j) in survive and table[i][j] == 1:
                        tmp[i][j] = 1
            
            table = tmp

            if t in shots:
                plot(table, ver, t)