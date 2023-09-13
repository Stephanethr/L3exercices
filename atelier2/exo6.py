import random


def present(L: list, e: int) -> bool:
    """_summary_

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        bool: _description_
    """

    return e in L


def test_present(present: callable):
    """_summary_

    Args:
        present (callable): _description_
    """
    print("---------------------------")
    # Test avec une liste vide
    if present([], 0):
        print("ECHEC : test liste vide")
    else:
        print("SUCCES : test liste vide")

    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test en début de liste
    if present(L, L[0]):
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")

    # Test en fin de liste
    if present(L, L[-1]):
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")

    # Test en milieu de liste
    if present(L, len(L) // 2):
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")

    # Test avec un entier non présent dans la liste
    if present(L, random.randint(max(L), max(L) + 50)):
        print("ECHEC : test absence")
    else:
        print("SUCCES : test absence")

    print("---------------------------")


# test


# VERSION 1
def present1(L, e):
    for i in range(0, len(L), 1):
        if L[i] == e:
            return True
        else:
            return False
    return False


def correction_present1(L, e):
    len_L = len(L)
    for i in range(0, len_L, 1):
        if L[i] == e:
            return True
    return False


# VERSION 2
def present2(L, e):
    b = True
    for i in range(0, len(L), 1):
        if L[i] == e:
            b = True
        else:
            b = False
    return b


def correction_present2(L, e):
    len_L = len(L)
    b = False
    for i in range(0, len_L, 1):
        if L[i] == e:
            b = True
    return b


# VERSION 3
def present3(L, e):
    b = True
    for i in range(0, len(L), 1):
        return L[i] == e


def correction_present3(L, e):
    len_L = len(L)
    for i in range(0, len_L, 1):
        if L[i] == e:
            return True
    return False


# VERSION 4
def present4(L, e):
    b = False
    i = 0
    while i < len(L) and b:
        if L[i] == e:
            b = True
    return b


def correction_present4(L, e):
    b = False
    i = 0
    len_L = len(L)
    while i < len_L:
        if L[i] == e:
            b = True
        i += 1
    return b


print("TEST PRESENT")
test_present(present)

print("TEST PRESENT 1")
test_present(present1)

print("TEST PRESENT 2")
test_present(present2)

print("TEST PRESENT 3")
test_present(present3)

print("TEST PRESENT 4")
test_present(present4)


print("TEST CORRECTION PRESENT 1")
test_present(correction_present1)

print("TEST CORRECTION PRESENT 2")
test_present(correction_present2)

print("TEST CORRECTION PRESENT 3")
test_present(correction_present3)

print("TEST CORRECTION PRESENT 4")
test_present(correction_present4)


def pos(L: list, e: int) -> list:
    """_summary_

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        list: _description_
    """
    len_L = len(L)
    res = []
    for i in range(len_L):
        if L[i] == e:
            res.append(i)
    return res


# VERSION 1
def pos1(L, e):
    Lres = list(L)
    for i in range(0, len(L), 1):
        if L[i] == e:
            Lres += [i]
    return Lres


def correction_pos1(L, e):
    Lres = []
    len_L = len(L)
    for i in range(0, len_L, 1):
        if L[i] == e:
            Lres += [i]
    return Lres


# VERSION 2
def pos2(L, e):
    Lres = list(L)
    for i in range(0, len(L), 1):
        if L[i] == e:
            Lres[i] = i
    return Lres


def correction_pos2(L, e):
    Lres = []
    len_L = len(L)
    for i in range(0, len_L, 1):
        if L[i] == e:
            Lres += [i]
    return Lres


# VERSION 3
def pos3(L, e):
    nb = L.count(e)
    Lres = [0] * nb
    for i in range(0, len(L), 1):
        if L[i] == e:
            Lres.append(i)
    return Lres


def correction_pos3(L, e):
    Lres = []
    for i in range(0, len(L), 1):
        if L[i] == e:
            Lres.append(i)
    return Lres


# VERSION 4
def pos4(L, e):
    nb = L.count(e)
    Lres = [0] * nb
    j = 0
    for i in range(0, len(L), 1):
        if L[i] == e:
            Lres[j] = i
    return Lres


def correction_pos4(L, e):
    Lres = []
    for i in range(0, len(L), 1):
        if L[i] == e:
            Lres.append(i)
    return Lres


def test_pos(pos: callable):
    """_summary_

    Args:
        pos (callable): _description_
    """

    L = [3, 4, 5, 7, 2, 7]
    e = 7
    print("position de 7 dans la liste L : ", pos(L, e))
    print("---------------------------")


print("TEST POS")
test_pos(pos)

print("TEST POS 1")
test_pos(pos1)

print("TEST POS 2")
test_pos(pos2)

print("TEST POS 3")
test_pos(pos3)

print("TEST POS 4")
test_pos(pos4)

print("TEST CORRECTION POS 1")
test_pos(correction_pos1)

print("TEST CORRECTION POS 2")
test_pos(correction_pos2)

print("TEST CORRECTION POS 3")
test_pos(correction_pos3)

print("TEST CORRECTION POS 4")
test_pos(correction_pos4)
