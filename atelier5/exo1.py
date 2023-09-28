# Question 3


def somme_recursive(lst: list) -> int:
    """
    Calcule la somme des éléments d'une liste de manière récursive.

    Args:
    liste (list): La liste dont on souhaite calculer la somme.

    Returns:
    int or float: La somme des éléments de la liste.

    Raises:
    ValueError: Si la liste est vide.

    Example:
    >>> somme([1, 2, 3, 4, 5])
    15
    >>> somme([])
    Traceback (most recent call last):
        ...
    ValueError: La liste est vide.
    """
    len_list = len(lst)
    # Vérifier si la liste est vide
    if len_list == 0:
        raise ValueError("La liste est vide.")

    # Cas de base : si la liste ne contient qu'un élément, retourner cet élément
    if len_list == 1:
        return lst[0]

    # Cas récursif : ajouter le premier élément à la somme des éléments restants
    else:
        return lst[0] + somme_recursive(lst[1:])


lst = [2, 5, 7, 4, 2, 6]
res = somme_recursive(lst)
print(res)

# Question 2


def factorielle_recursive(nbr: int) -> int:
    """_summary_

    Args:
        nbr (int): _description_

    Returns:
        int: _description_
    """
    if nbr == 0:
        return 1
    else:
        return nbr * factorielle_recursive(nbr - 1)


res_facto = factorielle_recursive(5)

print(res_facto)

# Question 3


def longueur(lst: list) -> int:
    """_summary_

    Args:
        lst (list): _description_

    Returns:
        int: _description_
    """

    if not lst:
        return 0
    else:
        return 1 + longueur(lst[1:])


res_long = longueur(lst)
print(res_long)

# Question 4


def find_min(lst: list) -> int:
    mini = None
    if len(lst) == 0:
        raise ValueError("erreur")
    elif len(lst) == 1:
        mini = lst[0]
    else:
        mini = find_min(lst[1:])
        if mini > lst[0]:
            mini = lst[0]
    return mini


res_find = find_min(lst)
print(res_find)

# Question 5


def list_paires(lst: list) -> list:
    """
    Cette fonction prend une liste en entrée et renvoie une nouvelle liste contenant
    uniquement les éléments pairs de la liste d'origine.

    Args:
    lst (list): La liste d'entiers en entrée.

    Returns:
    list: Une nouvelle liste contenant les éléments pairs de la liste d'entrée.

    Raises:
    ValueError: Si la liste d'entrée est vide.

    Exemple:
    >>> list_paires([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> list_paires([1, 3, 5])
    []
    >>> list_paires([])  # Ceci provoquera une ValueError
    Traceback (most recent call last):
        ...
    ValueError: liste vide
    """
    if lst == []:
        return []
    else:
        if lst[0] % 2 == 0:
            # Si le premier élément de la liste est pair, il est ajouté à la liste 'pairs'
            return [lst[0]] + list_paires(lst[1:])
        else:
            # Si le premier élément de la liste n'est pas pair, récursion avec la liste restante
            return list_paires(lst[1:])


res_pairs = list_paires(lst)
print(res_pairs)

# Question 6


def concat_list(lst: list) -> list:
    if lst == []:
        return []
    else:
        return lst[0] + concat_list(lst[1:])


lst2lst = [[0, 1], [2, 3], [4], [6, 7]]
res_concat = concat_list(lst2lst)
print(f"concaténation de la liste {lst2lst} :", res_concat)
