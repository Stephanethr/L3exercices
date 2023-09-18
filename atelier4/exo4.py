from exo3 import choose_element_list


def extract_elements_list(
    list_in_which_to_choose: list, int_nbr_of_element_to_extract: int
) -> list:
    """_summary_

    Args:
        list_in_which_to_choose (list): _description_
        int_nbr_of_element_to_extract (int): _description_

    Returns:
        list: _description_
    """
    i = 0
    res = []
    while i < int_nbr_of_element_to_extract:
        elt = choose_element_list(list_in_which_to_choose)
        if elt not in res:
            res.append(elt)
            i += 1

    return res


list = [1, 32, 4, 5, 7, 8, 0, 9]
nbr = 6

print("Liste de départ", list)
sublist = extract_elements_list(list, nbr)
print(f"La sous liste de {nbr} élément(s) extraite est : ", sublist)
print("Liste de départ après appel de la fonction est : ", list)
