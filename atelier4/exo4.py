from exo3 import choose_element_list


def extract_elements_list(
    list_in_which_to_choose: list, int_nbr_of_element_to_extract: int
) -> list:
    """
    Extrait un nombre donné d'éléments au hasard depuis une liste donnée.

    Args:
        list_in_which_to_choose (list): La liste à partir de laquelle extraire les éléments.
        int_nbr_of_element_to_extract (int): Le nombre d'éléments à extraire.

    Returns:
        list: Une liste contenant les éléments extraits au hasard.
    """
    i = 0  # Initialise un compteur.
    res = []  # Crée une liste vide pour stocker les éléments extraits.

    while (
        i < int_nbr_of_element_to_extract
    ):  # Continue tant que le nombre d'éléments extraits est inférieur à la quantité souhaitée.
        elt = choose_element_list(
            list_in_which_to_choose
        )  # Appelle la fonction choose_element_list pour obtenir un élément aléatoire.
        res.append(elt)  # Ajoute l'élément extrait à la liste de résultats.
        i += 1  # Incrémente le compteur pour suivre le nombre d'éléments extraits.

    return res  # Retourne la liste des éléments extraits au hasard.


list = [1, 32, 4, 5, 7, 8, 0, 9]
nbr = 5

print("Liste de départ", list)
sublist = extract_elements_list(list, nbr)
print(f"La sous liste de {nbr} élément(s) extraite est : ", sublist)
print("Liste de départ après appel de la fonction est : ", list)
