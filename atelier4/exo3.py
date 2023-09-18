import random


def choose_element_list(list_in_which_to_choose: list) -> any:
    """_summary_

    Args:
        list_in_which_to_choose (list): _description_

    Returns:
        any: _description_
    """

    return list_in_which_to_choose[random.randint(0, len(list_in_which_to_choose) - 1)]


listtest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45]
print("choix element : ", choose_element_list(listtest))
