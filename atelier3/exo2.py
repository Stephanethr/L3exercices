# 1
def mots_Nlettres(lst_mot: list, n: str) -> list:
    """_summary_

    Args:
        lst_mot (list): _description_
        n (str): _description_

    Returns:
        list: _description_
    """
    lst_n_in_lst_mot = []
    len_lst = len(lst_mot)
    for index in range(len_lst):
        if lst_mot[index].find(n) != -1:
            lst_n_in_lst_mot.append(lst_mot[index])

    return lst_n_in_lst_mot


def test(mots_Nlettres: callable):
    lst_mot = [
        "jouer",
        "bonjour",
        "punir",
        "jour",
        "aurevoir",
        "revoir",
        "pouvoir",
        "cour",
        "abajour",
        "finir",
        "aimer",
    ]
    lettre = "o"
    print(f"mots contenant la lettre {lettre} : ", mots_Nlettres(lst_mot, lettre))


test(mots_Nlettres)

# 2


def commence_par(mot: str, prefixe: str) -> bool:
    """_summary_

    Args:
        mot (str): _description_
        suffixe (str): _description_

    Returns:
        bool: _description_
    """
    res = False
    if len(prefixe) < len(mot):
        if prefixe in mot and mot.find(prefixe) == 0:
            res = True

    return res


# def commence_par_v2(mot: str, prefixe: str) -> bool:
#    return mot == prefixe + mot[len(prefixe) :]

# return prefixe == mot[: len(prefixe)]


def finit_par(mot: str, suffixe: str) -> bool:
    """_summary_

    Args:
        mot (str): _description_
        suffixe (str): _description_

    Returns:
        bool: _description_
    """
    res = True
    # Vérifie si la longueur du suffixe est supérieure à la longueur du mot
    if len(suffixe) > len(mot):
        res = False

    # Compare la fin du mot avec le suffixe
    if mot[-len(suffixe) :] == suffixe:
        return res


print("test commence par : ", commence_par("bonjour", "bon"))
print("test finit par : ", finit_par("MAISONS", "SONS"))


def finissent_par(lst_mot: list, suffixe: str) -> list:
    """_summary_

    Args:
        lst_mot (list): _description_
        suffixe (str): _description_

    Returns:
        list: _description_
    """
    lst_res = []

    for mot in lst_mot:
        if finit_par(mot, suffixe):
            lst_res.append(mot)
    return lst_res


def finissent_par_v2(lst_mot: list, suffixe: str) -> list:
    return [mot for mot in lst_mot if finit_par(mot, suffixe)]


def commencent_par(lst_mot: list, prefixe: str) -> list:
    """_summary_

    Args:
        lst_mot (list): _description_
        suffixe (str): _description_

    Returns:
        list: _description_
    """
    lst_res = []

    for mot in lst_mot:
        if commence_par(mot, prefixe):
            lst_res.append(mot)
    return lst_res


lst_mot = [
    "jouer",
    "bonjour",
    "punir",
    "jour",
    "aurevoir",
    "revoir",
    "pouvoir",
    "cour",
    "abajour",
    "finir",
    "aimer",
]

suffixe = "voir"
prefixe = "re"

print(f"finissent par {suffixe} : ", finissent_par(lst_mot, suffixe))
print(f"finissent par v2 {suffixe} : ", finissent_par(lst_mot, suffixe))

print(f"commencent par {prefixe} : ", commencent_par(lst_mot, prefixe))


def list_mots(lst_mot: list, prefixe: str, suffixe: str, n: str) -> list:
    """_summary_

    Args:
        lst_mot (list): _description_
        prefixe (str): _description_
        suffixe (str): _description_
        n (int): _description_

    Returns:
        list: _description_
    """
    lst_res = []
    lst_mot_n_lettre = mots_Nlettres(lst_mot, n)

    for mot in lst_mot_n_lettre:
        if commence_par(mot, prefixe) and finit_par(mot, suffixe):
            lst_res.append(mot)
    return lst_res


n = "e"
print("list mots : ", list_mots(lst_mot, prefixe, suffixe, n))


def dictionnaire(fichier: str) -> list:
    """_summary_

    Args:
        fichier (str): _description_

    Returns:
        list: _description_
    """
    fichier = open(fichier, "r")
    line = fichier.readline()
    res = []
    while line != "":
        res.append(line)
        line = fichier.readline()
    return res


# print(dictionnaire("./atelier3/littre.txt"))
