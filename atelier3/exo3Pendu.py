def places_lettre(ch: str, mot: str) -> list:
    """_summary_

    Args:
        ch (str): _description_
        mot (str): _description_

    Returns:
        list: _description_
    """
    len_mot = len(mot)
    res = []
    for i in range(len_mot):
        if mot[i] == ch:
            res.append(i)
    return res


mot = input("entrez un mot : ")
ch = input("entrez un caractère à chercher dans le mot précédent : ")
print(places_lettre(ch, mot))


def outputStr(mot: str, lpos: list) -> str:
    """_summary_

    Args:
        mot (str): _description_
        lpos (list): _description_

    Returns:
        str: _description_
    """
