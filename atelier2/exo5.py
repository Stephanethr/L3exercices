def vitrine(nbEmplacements: int, lObjets: list) -> list:
    """_summary_

    Args:
        nbEmplacements (int): _description_
        lObjets (list): _description_

    Returns:
        list: _description_
    """
    listSorted = sorted(lObjets)
    len_list = len(listSorted)
    res = [[], []]
    for i in range(len_list - 1):
        if listSorted[i] == listSorted[i + 1]:
            res[1].append(listSorted[i + 1])
        else:
            res[0].append(listSorted[i])

    return res


# test vitrine
nbEmplacements = 4
lObjets = [1, 2, 2, 3, 4, 5, 5]
print("vitrine : ", vitrine(nbEmplacements, lObjets))


def placer_objets_dans_vitrines(nbEmplacements, lObjets):
    # Créer une liste de vitrines, chaque vitrine étant une liste vide
    vitrines = [[]]
    len_lObjets = len(lObjets)
    # Parcourir la liste d'objets
    for index in range(len_lObjets):
        # Vérifier si le nombre maximum d'objets par vitrine est atteint
        if len(vitrines) >= nbEmplacements:
            # Si oui, créer une nouvelle vitrine
            vitrines.append([])

        # Vérifier si l'objet peut être placé dans la vitrine actuelle sans violer la contrainte
        if lObjets[index] not in vitrines:
            vitrines.append(lObjets[index])
        else:
            # Si l'objet existe déjà dans la vitrine actuelle, le placer dans la prochaine vitrine
            vitrines.append(lObjets[index])

    # Vérifier si la répartition est valide
    """
    somme_objets = sum(len(vitrine) for vitrine in vitrines)
    if somme_objets == len(lObjets):
        return vitrines
    else:
        print("répartition non valide")
    """
    return vitrines


# Exemple d'utilisation
nbEmplacements = 4
lObjets = [1, 2, 2, 3, 4, 5, 5]
resultat = placer_objets_dans_vitrines(nbEmplacements, lObjets)

if resultat:
    print("Configuration possible :")
    for i, vitrine in enumerate(resultat):
        print(f"Vitrine {i + 1}:", vitrine)
else:
    print("Aucune configuration possible pour les objets donnés.")
