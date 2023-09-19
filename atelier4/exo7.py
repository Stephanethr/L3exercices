from exo6 import sort_list  # Importez la fonction sort_list de exo6.py.
from exo2 import mix_list  # Importez la fonction mix_list de exo2.py.


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


def tri_selection(lst: list) -> list:
    res = []
    # for i in range()
