import numpy as np


def create_p_matrix():
    P = np.zeros((8, 8))
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


def numerical_method(p, pi, epsilon):
    eps_ = 1
    count = 0
    temp = np.dot(p, pi)
    temp_old = p
    while eps_ > epsilon:
        temp = np.dot(temp, p)
        eps_ = np.sum(np.square(temp - temp_old))
        count += 1
        print(count, eps_)
        temp_old = temp
    return temp


P = create_p_matrix()
PI_Zero = np.zeros(8)
PI_Zero[1] = 1

eps = 0.000001

Z = numerical_method(P, PI_Zero, eps)

print(Z)
