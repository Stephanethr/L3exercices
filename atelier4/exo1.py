import random


def gen_list_random_int(len_list=10, int_binf=0, int_bsup=10) -> list:
    int_nbr = []
    while len(int_nbr) < len_list:
        random_number = random.randint(int_binf, int_bsup)
        if random_number not in int_nbr:
            int_nbr.append(random_number)
    return sorted(int_nbr)


print(gen_list_random_int())
print(gen_list_random_int(50, 0, 100))
