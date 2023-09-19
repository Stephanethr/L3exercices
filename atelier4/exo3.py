import random


def choose_element_list(list_in_which_to_choose: list) -> any:
    """
    Choisi un élément au hasard dans une liste donnée.

    Args:
        list_in_which_to_choose (list): La liste à partir de laquelle choisir un élément.

    Returns:
        any: L'élément choisi au hasard de la liste.
    """
    # Utilise random.randint pour générer un index aléatoire dans la plage des indices de la liste.
    random_index = random.randint(0, len(list_in_which_to_choose) - 1)

    # Retourne l'élément de la liste correspondant à l'index aléatoire.
    return list_in_which_to_choose[random_index]


listtest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45]
print("choix element : ", choose_element_list(listtest))
