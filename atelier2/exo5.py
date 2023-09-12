def vitrine(nbEmplacements: int, lObjets: list) -> list:
    """_summary_

    Args:
        nbEmplacements (int): _description_
        lObjets (list): _description_

    Returns:
        list: _description_
    """
    lObjetsSorted = sorted(lObjets)
    len_lObjetsSorted = len(lObjetsSorted)
    res = []
    for i in range(len_lObjetsSorted):
        if lObjetsSorted[i] == lObjetsSorted[i] + 1:
            lObjetsSorted.pop(lObjetsSorted[i])

    return lObjetsSorted


# test vitrine
nbEmplacements = 4
lObjets = [1, 2, 2, 3, 4, 5, 5]
print("vitrine : ", vitrine(nbEmplacements, lObjets))
