import numpy as np
import random


A = np.random.randint(0, 10, [4, 4])
I = np.identity(4)

print(A)
print(I)


def matrice_trace(matrix: list) -> list:
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]

    return trace


trace = matrice_trace(A)
trace_numpy = A.trace()
print(trace)
print(trace_numpy)


def est_symetrique(matrix: list) -> bool:
    res = True
    for line in range(len(matrix)):
        for col in range(len(matrix[line])):
            if matrix[line][col] != matrix[col][line]:
                res = False
    return res


N = 4
b = np.random.random_integers(0, 10, size=(N, N))
b_symm = (b + b.T) / 2

print(f"{A} est symétrique : ", est_symetrique(A))
print(f"{b_symm} est symétrique : ", est_symetrique(b_symm))


def produit_diagonal(matrix: list) -> list:
    res = 1
    for i in range(len(matrix)):
        res = res * matrix[i][i]

    return res


print(f"produit diagonal de\n {A} : ", produit_diagonal(A))
print("matrice A est diagonale : ", est_symetrique((A + A.T) / 2))
print("calcul produit de la diagonale de la matrice I : ", produit_diagonal(I))
print("A : \n", A, "\nA.T : \n", A.T)


A_inv = np.linalg.inv(A)
print(A_inv)

print(
    "inverser la matrice A et la multiplier par A pour obtenir une matrice proche de I : \n",
    A * A_inv,
)
