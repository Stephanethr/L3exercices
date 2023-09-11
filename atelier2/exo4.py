# Question 1


def histo(F: list) -> list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """
    H = []
    maxValeur = max(F)
    H = [0] * (maxValeur + 1)
    for valeur in F:
        H[valeur] += 1
    return H


# test def histo
list = [1, 4, 5, 3, 7, 9, 3, 2, 2, 5, 6]
print("def histo : ", histo(list))


def est_injective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H = histo(F)
    res = False
    i = 0
    len_list = len(H)

    while i < len_list:
        if H[i] <= 1:
            res = True
        else:
            return False
        i += 1
    return res


# test def est_injective
listInjective = [1, 2, 3, 4, 5, 6, 7, 9]
print("def est_injective (False) : ", str(est_injective(list)))
print("def est_injective (True) : ", str(est_injective(listInjective)))


def est_surjective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H = histo(F)
    res = False
    i = 0
    len_list = len(H)
    print(H)
    while i < len_list:
        if H[i] >= 1:
            res = True
        else:
            return False
        i += 1
    return res


# test est_surjective

listSurjective = [0, 1, 1, 2, 3, 4, 5, 6, 6]

print("est surjective (True) : ", est_surjective(listSurjective))
print("est surjective (False) : ", est_surjective(listInjective))


def est_bijective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    if est_injective(F) and est_surjective(F):
        return True
    return False


# test est bijective
listBijective = [3, 0, 6, 7, 4, 2, 1, 5]
print(listBijective, " est bijective : ", est_bijective(listBijective))

# Question 2
