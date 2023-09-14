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
    print(mots_Nlettres(lst_mot, "o"))


test(mots_Nlettres)
