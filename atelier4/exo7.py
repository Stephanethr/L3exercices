from exo6 import sort_list  # Importez la fonction sort_list de exo6.py.
from exo2 import mix_list  # Importez la fonction mix_list de exo2.py.

# Question 1


def stupid_sort(lst_to_sort: list) -> list:
    """
    Implémente l'algorithme "stupid sort" pour trier une liste.

    Args:
        lst_to_sort (list): La liste à trier.

    Returns:
        list: Une nouvelle liste contenant les éléments triés.
    """
    res = list(lst_to_sort)  # Crée une copie de la liste à trier.
    sorted_list = sort_list(
        lst_to_sort
    )  # Trie la liste d'origine pour obtenir une liste triée de référence.
    i = 0
    # Continue à mélanger la liste jusqu'à ce qu'elle soit triée.
    while res != sorted_list:
        res = mix_list(res)  # Mélange la liste en utilisant la fonction mix_list.
        print(res, i)  # Affiche la liste actuelle après chaque mélange.
        i += 1

    return res  # Retourne la liste triée.


lst = [1, 6, 7, 2, 9, 4]
# print(stupid_sort(lst))  # Appelle la fonction pour trier la liste et l'affiche.

# Question 2


def tri_insertion(lst: list) -> list:
    """
    Trie une liste d'éléments en utilisant l'algorithme de tri par insertion.

    Args:
        lst (list): La liste à trier.

    Returns:
        list: Une nouvelle liste contenant les éléments triés dans l'ordre croissant.
    """
    lst_copy = list(
        lst
    )  # Crée une copie de la liste d'origine pour ne pas la modifier.
    len_list = len(lst_copy)  # Obtient la longueur de la liste copiée.

    for i in range(1, len_list):
        x = lst_copy[i]  # Récupère l'élément à la position i.
        j = i

        # Déplace les éléments plus grands que x vers la droite pour faire de la place à x.
        while j > 0 and lst_copy[j - 1] > x:
            lst_copy[j] = lst_copy[j - 1]
            j -= 1

        lst_copy[j] = x  # Insère x à la position correcte dans la liste triée.

    return lst_copy  # Retourne la liste triée.


print(tri_insertion(lst))


# Question 3


def tri_selection(lst: list) -> list:
    """
    Trie un tableau t par ordre croissant en utilisant l'algorithme de tri par sélection.

    Args:
        t (list): Le tableau à trier.

    Returns:
        list: Le tableau trié par ordre croissant.
    """
    t = lst.copy()
    n = len(t)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if t[j] < t[min_index]:
                min_index = j
        if min_index != i:
            t[i], t[min_index] = t[min_index], t[i]
    return t


print(f"test tri_selection avec comme list {lst} : ", tri_selection(lst))


# Question 4


def buble_sort(list_to_sort: list) -> list:
    lst = list_to_sort.copy()
    len_list = len(lst)
    for i in range(len_list - 1):
        for j in range(0, len_list - i - 1):
            print(lst)
            if lst[j + 1] < lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


lst2 = [4, 2, 3, 1]
print(f"test buble_sort avec comme list {lst2} : ", buble_sort(lst2))
