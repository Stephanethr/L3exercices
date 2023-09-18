import random
from exo1 import gen_list_random_int


def mix_list(list_to_mix: list) -> list:
    """_summary_

    Args:
        list_to_mix (list): _description_

    Returns:
        list: _description_
    """
    len_list_to_mix = len(list_to_mix)
    mixed_list = []
    i = 0
    while len(mixed_list) < len_list_to_mix:
        if list_to_mix[i] not in mixed_list:
            mixed_list.insert(random.randint(0, len_list_to_mix), list_to_mix[i])
            i += 1
            if list_to_mix == mixed_list:
                mixed_list.clear()
                i = 0

    return mixed_list


liste_triee = gen_list_random_int(3, 0, 50)
liste_mixee = mix_list(liste_triee)
print("liste triée : ", liste_triee, " ; Liste mélangée : ", liste_mixee)
