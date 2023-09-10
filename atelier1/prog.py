import random
from math import *
from datetime import *


# EXERCICE 1


def message_imc(imc: float) -> str:
    if imc <= 0:
        return str(imc) + " erreur de la valeur"
    elif imc < 16.5:
        return str(imc) + " dénutrition ou famine"
    elif imc <= 18.5:
        return str(imc) + " maigreur"
    elif imc <= 30.0:
        return str(imc) + " surpoids"
    elif imc <= 35.0:
        return str(imc) + " obésité modérée"
    elif imc <= 40.0:
        return str(imc) + " obésité sévère"
    else:
        return str(imc) + " obésité morbide"


def test_imc(nbEssai):
    while nbEssai > 0:
        print("résultat IMC : ", message_imc(random.randint(-20, 50.0)))
        nbEssai -= 1


test_imc(20)


# EXERCICE 2


def est_bissextile(year):
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0


def test_year():
    year = [4, 100, 400, 444, 2024, 2004, 1998, 2005]
    for y in year:
        if est_bissextile(y):
            print(y, " : est bissexstile")
        else:
            print(y, " : n'est pas bissextile")


test_year()


# EXERCIE 3

# QUESTION 1


def discriminant(a, b, c):
    delta = b * b - 4 * a * c

    return delta


# QUESTION 2


def racine_unique(a, b):
    x = -b / (2 * a)

    return x


a = -5
b = 7
c = 7
delta = discriminant(a, b, c)
print("resultat discriminant : ", str(delta))

# QUESTION 3


def racine_double(a, b, delta, num):
    if delta < 0:
        return False
    else:
        if num == 1:
            x1 = (-b + sqrt(delta)) / (2 * a)
            return x1

        elif num == 2:
            x2 = (-b - sqrt(delta)) / (2 * a)
            return x2


print(racine_double(a, b, delta, 1))
print(racine_double(a, b, delta, 2))

# QUESTION 4


def str_equation(a, b, c):
    # Représenter le terme ax2
    if a == 1:
        ax2_str = "x2"
    elif a == -1:
        ax2_str = "-x2"
    else:
        ax2_str = f"{a}x2"

    # Représenter le terme bx
    if b == 0:
        bx_str = ""
    elif b == 1:
        bx_str = " + x"
    elif b == -1:
        bx_str = " - x"
    elif b > 0:
        bx_str = f" + {b}x"
    else:
        bx_str = f" - {-b}x"

    # Représenter le terme constant c
    if c == 0:
        c_str = ""
    elif c > 0 and (
        a != 0 or b != 0
    ):  # If a or b is non zero, we might need a "+" sign
        c_str = f" + {c}"
    else:
        c_str = f" {c}"

    # Assembler l'équation
    equation = f"{ax2_str}{bx_str}{c_str} = 0"
    return equation


# Tester la fonction avec des cas supplémentaires
test_cases = [(2, 3, 4), (1, 0, 4), (1, -1, -1)]
results = [str_equation(a, b, c) for a, b, c in test_cases]
print(results)

# QUESTION 5


def solution_equation(a, b, c):
    str_solution = ""

    delta = discriminant(a, b, c)
    x = racine_unique(a, b)
    x1 = racine_double(a, b, delta, 1)
    x2 = racine_double(a, b, delta, 2)

    if delta < 0:
        str_solution = (
            "solution de l'équation : "
            + str_equation(a, b, c)
            + "\n pas de racine réelle"
        )
    elif delta == 0:
        str_solution = (
            "Solution de l'équation : "
            + str_equation(a, b, c)
            + "\n Racine unique : x = "
            + str(x)
        )
    else:
        str_solution = (
            "Solution de l'équation : "
            + str_equation(a, b, c)
            + "\n Deux racines : \n x1 = "
            + str(x1)
            + "\n x2 = "
            + str(x2)
        )

    return str_solution


# test solution_equation
def test_solution():
    print(
        "---------------------SOLUTION EQUATION PAS DE RACINE REELLE-----------------------------"
    )
    print(solution_equation(5, -4, 48))
    print(
        "---------------------SOLUTION EQUATION RACINE UNIQUE-----------------------------"
    )
    print(solution_equation(1, 1, 1))
    print(
        "---------------------SOLUTION EQUATION RACINE DOUBLE-----------------------------"
    )
    print(solution_equation(-5, -4, 48))


test_solution()

# EXERCICE 4


# Fonction pour vérifier si une date est valide
def date_est_valide(jour: int, mois: int, annee: int) -> bool:
    """_summary_

    Args:
        jour (int): _description_
        mois (int): _description_
        annee (int): _description_

    Returns:
        bool: _description_
    """

    if mois < 1 or mois > 12:
        return False
    if jour < 1 or jour > 31:
        return False
    if mois == 2:
        if est_bissextile(annee):
            return jour <= 29
        else:
            return jour <= 28
    elif mois in [4, 6, 9, 11]:
        return jour <= 30
    else:
        return True

# Fonction pour saisir une date de naissance depuis le clavier
def saisie_date_naissance() -> date:
    while True:
        try:
            annee = int(input("Entrez l'année de naissance : "))
            mois = int(input("Entrez le mois de naissance : "))
            jour = int(input("Entrez le jour de naissance : "))
            if date_est_valide(jour, mois, annee):
                return datetime.date(annee, mois, jour)  # Utilisation de datetime.date() pour créer un objet date
            else:
                print("Date invalide. Veuillez entrer une date de naissance valide.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer des entiers pour l'année, le mois et le jour.")


# Fonction pour calculer l'âge
def age(date_naissance: date) -> int:
    """_summary_

    Args:
        date_naissance (date): _description_

    Returns:
        int: _description_
    """
    aujourdhui = datetime.date.today()
    age = aujourdhui.year - date_naissance.year - ((aujourdhui.month, aujourdhui.day) < (date_naissance.month, date_naissance.day))
    return age

# Fonction pour vérifier si une personne est majeure
def est_majeur(date_naissance: date) -> bool:
    """_summary_

    Args:
        date_naissance (date): _description_

    Returns:
        bool: _description_
    """
    return age(date_naissance) >= 18


d = datetime.date(1998, 4, 8)

print(d)

# Procédure de test d'accès
def test_acces():
    date_naissance = saisie_date_naissance()
    age_personne = age(date_naissance)
    if est_majeur(date_naissance):
        print(f"Bonjour, vous avez {age_personne} ans, Accès autorisé.")
    else:
        print(f"Désolé, vous avez {age_personne} ans, Accès interdit.")

# Test des fonctions et procédures
test_acces()