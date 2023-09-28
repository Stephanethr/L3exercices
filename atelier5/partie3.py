import numpy as np


def matriceAdjacence(S: list, A: list) -> list:
    tailleMatrice = (len(S), len(S))
    matrice = np.zeros(tailleMatrice)
    for i, j in A:
        if i in S and j in S:
            matrice[i][j] = 1
    return matrice


S = [0, 1, 2, 3]
A = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]

print(matriceAdjacence(S, A))


def matriceAdjacencePont(S: list, A: list) -> list:
    """
    Crée une matrice d'adjacence pondérée à partir d'une liste de sommets et d'une liste d'arcs pondérés.

    Args:
        S (list): Liste des sommets.
        A (list): Liste des arcs pondérés, chaque arc étant représenté sous la forme d'un triplet (i, j, poids).

    Returns:
        numpy.ndarray: La matrice d'adjacence pondérée sous forme d'un tableau NumPy à 2 dimensions.
    """
    tailleMatrice = (len(S), len(S))
    matrice = np.zeros(tailleMatrice)
    for i, j, poids in A:
        if i in S and j in S:
            matrice[i][j] = poids
    return matrice


P = [(0, 1, 11), (0, 2, 5), (1, 2, 7), (2, 3, 6), (3, 1, 8)]
print(matriceAdjacencePont(S, P))


def lireMatriceFichier(nomfichier) -> list:
    with open(nomfichier, "r") as fichier:
        lignes = fichier.readlines()

        # Lire la première ligne pour déterminer la dimension de la matrice
        premiere_ligne = lignes[0].strip().split()
        dimension = len(premiere_ligne)

        # Initialiser la matrice numpy avec des zéros
        matrice = np.zeros((dimension, dimension), dtype=int)

        # Remplir la première ligne de la matrice
        for j, chiffre_str in enumerate(premiere_ligne):
            matrice[0, j] = int(chiffre_str)

        # Remplir le reste des lignes de la matrice
        for i in range(1, dimension):
            nombres_str = lignes[i].strip().split()
            for j, chiffre_str in enumerate(nombres_str):
                matrice[i, j] = int(chiffre_str)

    return matrice


for i in range(0, 5):
    matrice = lireMatriceFichier(f"atelier5\graph{i}.txt")
    print(matrice)
