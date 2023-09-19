import random
from exo1 import gen_list_random_int


def mix_list(list_to_mix: list) -> list:
    """
    Mélange une liste donnée de manière aléatoire.

    Args:
        list_to_mix (list): La liste à mélanger.

    Returns:
        list: Une nouvelle liste contenant les éléments de la liste d'entrée mélangés de manière aléatoire.
    """
    len_list_to_mix = len(list_to_mix)  # Obtient la longueur de la liste à mélanger.
    mixed_list = []  # Crée une liste vide pour stocker la liste mélangée.
    i = 0  # Initialise un compteur pour parcourir la liste d'entrée.

    while (
        len(mixed_list) < len_list_to_mix
    ):  # Continue jusqu'à ce que la liste mélangée atteigne la même longueur que la liste d'entrée.
        # Insère l'élément de la liste d'entrée à une position aléatoire dans la liste mélangée.
        mixed_list.insert(random.randint(0, len_list_to_mix), list_to_mix[i])
        i += 1  # Passe à l'élément suivant de la liste d'entrée.

        # Si la liste mélangée devient identique à la liste d'entrée, réinitialise la liste mélangée et le compteur.
        if list_to_mix == mixed_list:
            mixed_list.clear()
            i = 0

    return mixed_list  # Retourne la liste mélangée de manière aléatoire.


"""
liste_triee = gen_list_random_int(6, 0, 50)
liste_mixee = mix_list(liste_triee)
print("liste triée : ", liste_triee, " ; Liste mélangée : ", liste_mixee)
"""
