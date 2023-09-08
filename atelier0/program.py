type_lettre = ""
poids = 0
tarif = 0
STICKER_SUIVI = 0.50


def tarif(type_lettre, poids):
    if type_lettre == "lettre verte":
        if poids <= 20:
            tarif = 1.16
        elif poids <= 100:
            tarif = 2.32
        elif poids <= 250:
            tarif = 4.00
        elif poids <= 500:
            tarif = 6.00
        elif poids <= 1000:
            tarif = 7.50
        elif poids <= 3000:
            tarif = 10.50
        else:
            print("poids maximum dépassé")

    elif type_lettre == "lettre prioritaire":
        if poids <= 20:
            tarif = 1.43

        elif poids <= 100:
            tarif = 2.86

        elif poids <= 250:
            tarif = 5.26

        elif poids <= 500:
            tarif = 7.89

        elif poids <= 3000:
            tarif = 11.40

        else:
            print("poids maximum dépassé")

    elif type_lettre == "ecopli":
        if poids <= 20:
            tarif = 1.14
        elif poids <= 100:
            tarif = 2.28
        elif poids <= 250:
            tarif = 3.92
        else:
            print("poids maximum dépassé")

    else:
        print("type de lettre inconnu")

    return tarif


# print(tarif("lettre verte", 25))
print(tarif("lettre verte", 99))
# print(tarif("ecopli", 104))
