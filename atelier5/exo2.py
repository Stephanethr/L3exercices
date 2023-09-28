# Question 1
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 14])


def my_searchsorted(table: list, num: int) -> int:
    """_summary_

    Args:
        table (list): _description_
        num (int): _description_

    Returns:
        int: _description_
    """
    len_table = len(table)
    res = None
    for i in range(len_table):
        if table[i] == num:
            res = i
    return res


print("test my searchsorted : ", my_searchsorted(arr, 6))

print("test numpy.where : ", np.where(arr == 4))


def my_where(table: list, num: int) -> list:
    indice_num = my_searchsorted(table, num)
    res = [[indice_num], type(indice_num)]
    return res


print("test my_where : ", my_where(arr, 4))


def my_add(A: list, B: list) -> list:
    """
    Additionne deux matrices représentées sous forme de listes de listes.

    Args:
        A (list): La première matrice représentée sous forme de liste de listes.
        B (list): La deuxième matrice représentée sous forme de liste de listes.

    Returns:
        list: Une nouvelle matrice qui est le résultat de l'addition des deux matrices.
              Retourne None si les dimensions des matrices ne sont pas compatibles.

    Raises:
        None

    Exemple:
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> my_add(A, B)
        [[6, 8], [10, 12]]

        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6, 7], [8, 9, 10]]
        >>> my_add(A, B)
        None
    """
    len_A = len(A)
    len_B = len(B)

    # Vérifie que les matrices ont la même dimension.
    if len_A != len_B or len(A[0]) != len(B[0]):
        return None

    new_matrix = []

    # Additionne les éléments correspondants des deux matrices.
    for line in range(len_A):
        line_matrix = []
        for col in range(len(A[line])):
            line_matrix.append(A[line][col] + B[line][col])
        new_matrix.append(line_matrix)
    return new_matrix


A = [[3, 1], [6, 4]]
B = [[1, 8], [4, 2]]

print("test my_add : ", my_add(A, B))

import random


def gen_matrice3x3():
    matrice = np.array(([0] * 3, [0] * 3, [0] * 3))
    for line in range(len(matrice)):
        for col in range(len(matrice[line])):
            matrice[line, col] = random.randint(0, 9)
    return matrice


print("--------------------------------------")
matrice = gen_matrice3x3()
print("matrice de base : \n", matrice)

# additionne 10 à la matrice
for line in range(len(matrice)):
    for col in range(len(matrice[line])):
        matrice[line, col] += 10
print("matrice + 10 : \n", matrice)

# multiplie matrice par 2
print("matrice x 2 : \n", matrice * 2)

# affiche la ligne 2
print("matrice ligne 2 : \n", matrice[1])

# affiche la colonne 3
print("matrice colonne 3 : \n")

for line in range(len(matrice)):
    print([matrice[line, 2]])

# extraire sous matrice 2x2 du coin supérieur gauche de la matrice
M = []
for line in range(len(matrice)):
    for col in range(len(matrice[line])):
        if line < 2 and col < 2:
            M += [matrice[line][col]]
print("matrice 2x2 : \n")
print(M)
