def position_v1(list: list, elt: int) -> int:
    """_summary_

    Args:
        list (list): _description_
        elt (int): _description_

    Returns:
        int: indice of elt in list
    """
    len_list = len(list)
    for index in range(len_list):
        if elt == list[index]:
            return index
    return -1


def position_v2(list: list, elt: int) -> int:
    """_summary_

    Args:
        list (list): _description_
        elt (int): _description_

    Returns:
        int: indice of elt in list
    """
    len_list = len(list)
    index = 0
    while index < len_list:
        if elt == list[index]:
            return index
        index += 1
    return -1


list = [1, 5, 7, 4, 2, 8, 9]
elt = 8

print("position v1", position_v1(list, elt))
print("position v2", position_v2(list, elt))


def nb_occurences(list: list, elt: int) -> int:
    """_summary_

    Args:
        list (list): _description_
        elt (int): _description_

    Returns:
        int: _description_
    """
    occurences = 0

    for number in list:
        if elt == number:
            occurences += 1
    return occurences


# test nb_occurences
list_occurences = [1, 5, 3, 3, 6, 7, 8, 56, 4, 3, 3, 2, 2, 8, 8]
print("test nb_occurences : ", nb_occurences(list_occurences, 3))


def est_triee_v1(list: list) -> bool:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        bool: _description_
    """
    len_list = len(list) - 1
    for i in range(len_list):
        if list[i] > list[i + 1]:
            return False
    return True


def est_triee_v2(list: list) -> bool:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        bool: _description_
    """
    len_list = len(list) - 1
    i = 0

    while i < len_list:
        if list[i] > list[i + 1]:
            return False
        i += 1
    return True


# test est_triee

list_triee = [1, 2, 3, 4, 5, 6, 7, 8]
list_pas_triee = [1, 5, 3, 6, 7, 8]

print("test v1 triee : ", est_triee_v1(list_triee))
print("test v2 triee : ", est_triee_v1(list_triee))
print("test v1 pas triee : ", est_triee_v1(list_pas_triee))
print("test v2 pas triee : ", est_triee_v1(list_pas_triee))


def position_tri(list: list, elt: int) -> int:
    """_summary_

    Args:
        list (list): _description_
        elt (int): _description_

    Returns:
        int: _description_
    """
    len_list = len(list)
    left, right = 0, len_list - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == elt:
            return mid
        elif list[mid] < elt:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# test position tri


def a_repetitions(list) -> bool:
    """_summary_

    Args:
        list (_type_): _description_

    Returns:
        bool: _description_
    """
    len_list = len(list)
    list_repetition = []
    i = 0
    while i < len_list:
        if list[i] not in list_repetition:
            list_repetition.append(list[i])
        else:
            return True
        i += 1
    return False


# test a_repetition

print("liste avec repetition (attente true): " + str(a_repetitions(list_occurences)))
print("liste sans repetition (attente false): " + str(a_repetitions(list_triee)))


# EXO 3


def separer(L: list) -> list:
    """_summary_

    Args:
        L (list): _description_

    Returns:
        list: _description_
    """

    LSEP = []  # Initialisation de la liste LSEP

    # Ajout des nombres négatifs à gauche
    for num in L:
        if num < 0:
            LSEP.append(num)

    # Ajout des zéros au milieu
    for num in L:
        if num == 0:
            LSEP.append(num)

    # Ajout des nombres positifs à droite
    for num in L:
        if num > 0:
            LSEP.append(num)

    return LSEP


# Exemple d'utilisation
liste = [3, 0, -2, 5, 0, -1, 4]
resultat = separer(liste)
print(resultat)  # [-2, -1, 0, 0, 3, 5, 4]
