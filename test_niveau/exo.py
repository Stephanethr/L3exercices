def close_to_zero(mylist: list) -> float:
    res = 0
    # liste des nombres supérieurs à 0
    sup_list = []
    # Liste des nombres inférieurs à 0
    inf_list = []

    for e in mylist:
        # on ajoute les nombres supérieurs à la sup_list
        if e > 0:
            sup_list.append(e)
        # sinon on les ajoute à la liste inférieur
        else:
            inf_list.append(e)

    # trie des listes afin d'avoir le plus petit à l'indexe 0
    sup_list = sorted(sup_list)
    inf_list = sorted(inf_list, reverse=True)

    # on récupère ces chiffres dans une variable
    small_sup = sup_list[0]
    small_inf = inf_list[0]

    # on les multiplies par eux même afin de pouvoir les comparer (moins x moins = plus)
    if (small_sup * small_sup) < (small_inf * small_inf):
        return small_sup
    else:
        return small_inf


list = [7, -10, 13, 8, 4, -7.2, -12, -3.7, 3.5, -1.7, 2]
print(close_to_zero(list))
