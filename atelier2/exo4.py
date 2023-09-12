from exo1 import val_max

import matplotlib.pyplot as plt

# Question 1


def histo(F: list) -> list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """
    if len(F) == 0:
        print("Erreur : La liste est vide")
    else:
        H = []
        maxValeur = max(F)
        H = [0] * (maxValeur + 1)
        for valeur in F:
            H[valeur] += 1
        return H


# test def histo
list = [1, 4, 5, 3, 7, 9, 3, 2, 2, 5, 6]

print("def histo : ", histo(list))
print("def histo liste vide : ", histo([]))


def est_injective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H = histo(F)
    res = True
    i = 0
    len_list = len(H)

    while i < len_list:
        if H[i] > 1:
            res = False
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
    res = True
    i = 0
    len_list = len(H)
    while i < len_list:
        if H[i] < 1:
            res = False
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
    return est_injective(F) and est_surjective(F)


# test est bijective
listBijective = [3, 0, 6, 7, 4, 2, 1, 5]
print(listBijective, " est bijective : ", est_bijective(listBijective))

# Question 2


def afficheHisto(listHisto):
    H = histo(listHisto)
    MAXOCC = val_max(H)
    len_H = len(H)
    for i in range(MAXOCC):
        for index in range(len_H):
            if H[index] >= 1 and MAXOCC - i == H[index]:
                print("   #", end="")
                H[index] -= 1
            else:
                print("    ", end="")
        print("\n")
    print("|", end="")
    print(" --|" * len_H, "\n", end="")
    for i in range(len_H):
        print("  ", i, end="")


# def afficheHistoV2(F: list):

listHisto = [1, 4, 5, 3, 7, 9, 3, 2, 2, 5, 6, 11]

afficheHisto(listHisto)

# Question 3


def affiche_histo_v2(F: list):
    plt.hist(F, histtype="bar", color="red")

    plt.show()


# affiche_histo_v2(listHisto)
