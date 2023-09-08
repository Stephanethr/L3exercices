# EXERCIRE 1


def somme1(list: list) -> int:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        int: _description_
    """
    res = 0
    longueur_liste = len(list)
    for i in range(longueur_liste):
        res += list[i]
    return res


def somme2(list: list) -> int:
    """_summary_

    Args:
        list (_type_): _description_

    Returns:
        _type_: _description_
    """
    res = 0
    for i in list:
        res += i
    return res


def somme3(list: list) -> int:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        int: _description_
    """
    i = 0
    longueur_liste = len(list)
    res = 0
    while i < longueur_liste:
        res += list[i]
        i += 1
    return res


def moyenne(list: list) -> float:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        float: _description_
    """
    res = 0
    len_list = len(list)

    if len_list == 0:
        res = 0
    else:
        res = somme1(list) / len_list

    return res


def nb_sup1(list: list, e: int) -> int:
    """_summary_

    Args:
        list (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    len_list = len(list)
    res = 0
    for i in range(len_list):
        if list[i] > e:
            res += 1
    return res


def nb_sup2(list: list, e: int) -> int:
    """_summary_

    Args:
        list (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    res = 0
    for i in list:
        if i > e:
            res += 1
    return res


def moy_sup(list: list, e: int) -> float:
    """_summary_

    Args:
        list (list): _description_
        e (int): _description_

    Returns:
        float: _description_
    """
    list_sup = []
    for elt in list:
        if elt > e:
            list_sup.append(elt)
    return moyenne(list_sup)


def val_max(list: list) -> int:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        int: _description_
    """
    val_max = 0

    for i in list:
        if i > val_max:
            val_max = i
    return val_max


def ind_max(list: list) -> int:
    """_summary_

    Args:
        list (list): _description_

    Returns:
        int: _description_
    """

    # val_max = 0
    ind_max = 0
    len_list = len(list)
    v_max = 0

    for i in range(len_list):
        if list[i] > v_max:
            v_max = list[i]
            ind_max = i

    return ind_max


def test_exercice1():
    list1 = [1, 32, 50, 12, 2354]
    list2 = [1, 4, 6, 8, 3, 23, 9, 45]

    # test somme1
    print("TEST SOMME 1")
    # test liste vide
    print("Test liste vide : ", somme1([]))
    # test somme list1
    print("Test somme list1 : ", somme1(list1))
    print("test somme list2 : ", somme1(list2))

    # test somme2
    print("TEST SOMME 2")
    # test liste vide
    print("Test liste vide : ", somme2([]))
    # test somme list1
    print("Test somme list1 : ", somme2(list1))

    print("test somme list2 : ", somme2(list2))

    # test somme3
    print("TEST SOMME 3")
    # test liste vide
    print("Test liste vide : ", somme3([]))
    # test somme list1
    print("Test somme list1 : ", somme3(list1))
    # test somme
    print("test somme list2 : ", somme3(list2))

    # test moyenne
    print("TEST MOYENNE")
    # test liste vide moyenne
    print("Test liste vide : ", moyenne([]))
    # test moyenne
    print("Test moyenne list1 : ", moyenne(list1))
    # test moyenne

    print("test moyenne list2 : ", moyenne(list2))

    # test nb_sup1
    print("test nb_sup1 : ", nb_sup1(list2, 6))

    # test nb_sup2
    print("test nb_sup2 : ", nb_sup2(list2, 6))

    # test moy_sup
    print("test moy_sup : ", moy_sup(list2, 6))

    # test val_max
    print("test val_max : ", val_max(list2))
    # test val_max
    print("test ind_max : ", ind_max(list2))


test_exercice1()
