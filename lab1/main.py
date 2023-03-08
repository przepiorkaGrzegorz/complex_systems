import numpy as np
import matplotlib.pyplot as plt



def R_matrix(L, p):
    r = np.random.rand(L, L)
    R = np.zeros((L, L))
    for i in range(0, L):
        for j in range(0, L):
            if r[i, j] <= p:
                R[i, j] = 1
            elif r[i, j] > p:
                R[i, j] = 0
    return R


def Find(L, a, b, c, d, Lw):
	x = L[a, b]
	y = L[c, d]
	find_rc = Find_prim(L, x, Lw)
	row = find_rc[0]
	col = find_rc[1]

	for i in range(0, len(col)):
		aa = row[i]
		bb = col[i]
		L[aa, bb] = y
	return L


def Find_prim(a, b, Lw):
	size = a.shape
	row = np.array([], dtype=np.int64)
	col = np.array([], dtype=np.int64)
	for i in range(0, Lw):
		for j in range(0, Lw):
			if a[i, j] == b:
				row = np.append(row, i)
				col = np.append(col, j)

	return [[row], [col]]


def Label(L, p):
	R = R_matrix(L, p)
	iD = 1
	label = np.zeros((L, L))
	for i in range(0, L):
		for j in range(0, L):
			if R[i, j]:
				l_a = Above_left(i, j, R)
				above = l_a[0]
				left = l_a[1]

				if left == 0 and above == 0:
					label[i, j] = iD
					iD = iD + 1
				elif left != 0 and above == 0:
					label[i, j] = label[i, j-1]
				elif left == 0 and above != 0:
					label[i, j] = label[i-1, j]
				else:
					Lab_prim = Find(label, i, j-1, i-1, j, L)
					label = Lab_prim
					label[i, j] = label[i-1, j]
	return label


def Above_left(i, j, R):
	if i > 0 and j > 0:
		above = R[i-1, j]
		left = R[i,j-1]
	elif i > 0 and j == 0:
		above = R[i-1, j]
		left = 0
	elif i == 0 and j > 0:
		above = 0
		left = R[i, j-1]
	else:
		above = 0
		left = 0
	return (above, left)


def per(tab):
	left_side = tab[:, 0]
	left_side = left_side[left_side != 0]
	right_side = tab[:, -1]
	for Lel in left_side:
		if Lel in right_side:
			return 1
		return 0



if __name__ == "__main__":
    # Lw = 128
    # ptab=np.linspace(0.4,0.8,3)
    # MC=1e2
    # out=[]

    # for p in ptab:
    #     percol = 0
    #     for _ in range(int(MC)):
    #         L = Label(Lw,p)
    #         if per(L):
    #             percol+=1
    #     out.append(percol)
    #     print(p)
	
    # plt.plot(ptab,out)
    # plt.show()

    Lw = 15
    p = 0.6
    L = Label(Lw, p)
    print(L)

    plt.imshow(L, cmap='inferno')
    plt.colorbar()
    plt.show()