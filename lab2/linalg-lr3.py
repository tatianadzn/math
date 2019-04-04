import numpy as np


def create_p_matrix():
    P = np.zeros((4, 4))
    P[0, 0] = -1.7
    P[0, 1] = 3.6
    P[1, 0] = 1.7
    P[1, 1] = -5.3
    P[1, 2] = 7.2
    P[2, 1] = 1.7
    P[2, 2] = -8.9
    P[2, 3] = 7.2
    P[3, 2] = 1.7
    P[3, 3] = -7.2
    return P


P = create_p_matrix()

Z = np.zeros(4)

print(P)
print(Z)
result = np.linalg.lstsq(P, Z)

print(result)
