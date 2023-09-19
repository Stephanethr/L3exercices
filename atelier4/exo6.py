from exo1 import gen_list_random_int
import random
import matplotlib.pyplot as plt
import numpy as np
import time


def sort_list(lst: list) -> list:
    """
    Trie une liste d'éléments dans l'ordre croissant en utilisant l'algorithme de tri par sélection.

    Args:
        lst (list): La liste à trier.

    Returns:
        list: Une nouvelle liste contenant les éléments triés dans l'ordre croissant.
    """
    res = []  # Crée une liste vide pour stocker les éléments triés.
    lst_copy = list(lst)  # Copie la liste d'origine pour ne pas la modifier.
    len_lst = len(lst_copy)  # Obtient la longueur de la liste copiée.

    for _ in range(len_lst):
        min_elt = min(lst_copy)  # Trouve le plus petit élément dans la liste copiée.
        res.append(min_elt)  # Ajoute l'élément minimum à la liste résultante.
        lst_copy.remove(min_elt)  # Retire l'élément minimum de la liste copiée.

    return res  # Retourne la liste résultante triée.


"""
test = [1, 6, 3, 7, 4, 8, 0, 5]
print("liste non triée : ", test, " liste triée : ", sort_list(test))
"""


def perf_sort(
    sort_list: callable, sorted: callable, duree_list: list, nbr_exec: int
) -> tuple:
    """
    Mesure les performances des fonctions sort_list et sorted sur des listes de différentes longueurs.

    Args:
        sort_list (callable): Une fonction de tri personnalisée.
        sorted (callable): La fonction de tri intégrée (par exemple, sorted).
        duree_list (list): Une liste des longueurs des listes à tester.
        nbr_exec (int): Le nombre d'exécutions à effectuer pour chaque longueur de liste.

    Returns:
        tuple: Un tuple contenant deux listes de temps d'exécution moyen pour sort_list et sorted respectivement.
    """
    tps_exec_sort_list = (
        []
    )  # Crée une liste pour stocker les temps d'exécution moyen de sort_list.
    tps_exec_sorted = (
        []
    )  # Crée une liste pour stocker les temps d'exécution moyen de sorted.

    for i in duree_list:
        tps_sort_list = 0  # Initialise le temps d'exécution pour sort_list.
        tps_sorted = 0  # Initialise le temps d'exécution pour sorted.

        list_test = gen_list_random_int(
            i, 0, i
        )  # Génère une liste aléatoire de longueur i.

        for _ in range(nbr_exec):
            # Mesure le temps d'exécution de sort_list.
            start_pc = time.perf_counter()
            sort_list(list_test)
            end_pc = time.perf_counter()
            tps_sort_list += end_pc - start_pc

            # Mesure le temps d'exécution de sorted.
            start_pc = time.perf_counter()
            sorted(list_test)
            end_pc = time.perf_counter()
            tps_sorted += end_pc - start_pc

        # Calcule le temps d'exécution moyen pour sort_list et sorted et les ajoute aux listes correspondantes.
        tps_exec_sort_list.append(tps_sort_list / nbr_exec)
        tps_exec_sorted.append(tps_sorted / nbr_exec)

    return (tps_exec_sort_list, tps_exec_sorted)


"""
list_exec = [10, 20, 50, 100]
resultat_perf = perf_sort(sort_list, sorted, list_exec, 10)
print(resultat_perf)


x_axis_list = np.arange(0, 5.5, 0.5)
fig, ax = plt.subplots()

ax.plot(list_exec, resultat_perf[0], "bo-", label="sort_list")
ax.plot(list_exec, resultat_perf[1], "r*-", label="sorted")
ax.set(
    xlabel="Abscisse x",
    ylabel="Ordonnée y",
    title="Comparaison des performances de sort_list et sorted",
)
ax.legend(loc="upper center", shadow=True, fontsize="x-large")
plt.show()
"""
