# EXERCIRE 1


def somme1(list):
    res = 0
    for i in range(len(list)):
        res += list[i]
    return res


def somme2(list):
    res = 0
    for i in list:
        res += i
    return res


def somme3(list):
    i = 0
    longueurListe = len(list)
    res = 0
    while i < longueurListe:
        res += list[i]
        i += 1
    return res


def moyenne(list):
    res = 0
    nb_valeurs = 0
    if len(list) == 0:
        print("la liste est vide, résultat : ", res)
    else:
        for i in list:
            res += i
            nb_valeurs += 1
        res = res / nb_valeurs
    return res


def test_exercice1():
    # test somme1
    print("TEST SOMME 1")
    # test liste vide
    print("Test liste vide : ", somme1([]))
    # test somme 11111
    lst2test1 = [1, 10, 100, 1000, 10000]
    print("Test somme 11111 : ", somme1(lst2test1))
    test1 = [1, 4, 6, 8, 3]
    print("test somme 22 : ", somme1(test1))

    # test somme2
    print("TEST SOMME 2")
    # test liste vide
    print("Test liste vide : ", somme2([]))
    # test somme 11111
    lst2test2 = [1, 10, 100, 1000, 10000]
    print("Test somme 11111 : ", somme2(lst2test2))
    test2 = [1, 4, 6, 8, 3]
    print("test somme 22 : ", somme2(test2))

    # test somme3
    print("TEST SOMME 3")
    # test liste vide
    print("Test liste vide : ", somme3([]))
    # test somme 11111
    lst2test3 = [1, 10, 100, 1000, 10000]
    print("Test somme 11111 : ", somme3(lst2test3))
    # test somme
    test3 = [1, 4, 6, 8, 3]
    print("test somme 22 : ", somme3(test3))

    # test moyenne
    print("TEST MOYENNE")
    # test liste vide
    print("Test liste vide : ", moyenne([]))
    # test somme 11111
    lst2test4 = [1, 32, 50, 12, 2354]
    print("Test moyenne 489,8 : ", moyenne(lst2test4))
    # test somme
    test4 = [1, 4, 6, 8, 3]
    print("test moyenne 4,4 : ", moyenne(test4))


test_exercice1()
