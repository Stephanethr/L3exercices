import random


def gen_list_random_int(len_list=10, int_binf=0, int_bsup=9) -> list:
    """
    Génère une liste de nombres entiers aléatoires dans une plage spécifiée.

    Args:
        len_list (int): La longueur de la liste à générer (par défaut : 10).
        int_binf (int): La borne inférieure de la plage (par défaut : 0).
        int_bsup (int): La borne supérieure de la plage (par défaut : 9).

    Returns:
        list: Une liste de nombres entiers aléatoires.
    """
    int_nbr = []  # Crée une liste vide pour stocker les nombres entiers.

    while (
        len(int_nbr) < len_list
    ):  # Continue jusqu'à ce que la liste atteigne la longueur spécifiée.
        random_number = random.randint(
            int_binf, int_bsup
        )  # Génère un nombre aléatoire dans la plage spécifiée.
        int_nbr.append(random_number)  # Ajoute le nombre aléatoire à la liste.

    return int_nbr  # Retourne la liste de nombres entiers aléatoires.


def gen_list_random_int_v2(len_list=10, int_binf=0, int_bsup=9) -> list:
    return [random.randint(int_binf, int_bsup - 1) for _ in range(len_list)]


"""
print(gen_list_random_int())
print(gen_list_random_int(15, 0, 100))
"""
