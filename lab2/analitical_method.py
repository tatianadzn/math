import numpy as np


def create_p_matrix():
    P = np.zeros((9, 8))
    P[0, 0] = 0.2
    P[0, 1] = 0.8
    P[1, 1] = 0.3
    P[1, 2] = 0.7
    P[2, 2] = 0.1
    P[2, 3] = 0.9
    P[3, 2] = 0.4
    P[3, 3] = 0.1
    P[3, 4] = 0.5
    P[4, 4] = 0.5
    P[4, 5] = 0.5
    P[5, 5] = 0.2
    P[5, 6] = 0.2
    P[5, 7] = 0.6
    P[6, 5] = 0.5
    P[6, 6] = 0.5
    P[7, 0] = 0.6
    P[7, 7] = 0.4
    return P


P = create_p_matrix()
P = np.transpose(P)

i = 0
while i < 8:
    P[i, i] -= 1
    i += 1

newrow = np.ones(9)
newrow[8] = 0
P = np.vstack([P, newrow])


Z = np.zeros(9)
Z[8] = 1
print(P)
print(Z)
result = np.linalg.lstsq(P, Z)

print(result)
