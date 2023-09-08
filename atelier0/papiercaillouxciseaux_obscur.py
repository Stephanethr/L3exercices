import random


main_game = input(
    "Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? "
).upper()

if main_game == "O":
    joueur1 = input("Quel est votre nom ? ")
    nomJ1 = print("Bienvenu ", joueur1, " nous allons jouer ensemble \n")
    joueur2 = "Machine"

scoreJ1 = 0
nombre_partie = 0

if main_game == "N":
    joueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ", joueur1, " nous allons jouer ensemble")
    joueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ", joueur2, " nous allons jouer ensemble \n")


liste_choix = ["pierre", "papier", "ciseaux", "puit"]
continuer = True
scoreJ2 = 0

while continuer:
    nombre_partie += 1
    choix_j1 = input(
        "{nom} faîtes votre choix parmi ({liste}): ".format(
            nom=joueur1, liste=liste_choix
        )
    ).lower()
    legal_choice = choix_j1 in liste_choix

    while legal_choice == False:
        print("Je n'ai pas compris votre réponse")
        print("Joueur ", joueur1)
        choix_j1 = input(
            " faîtes votre choix parmi ({liste}): ".format(liste=liste_choix)
        )
        legal_choice = choix_j1 in liste_choix

    if main_game == "O":
        choix_j2 = liste_choix[random.randint(0, 2)]

    if main_game == "N":
        print("Joueur", joueur2)
        choix_j2 = input(
            " faîtes votre choix parmi ({liste}): ".format(liste=liste_choix)
        )
        legal_choice = choix_j2 in liste_choix

        while legal_choice == False:
            print("Je n'ai pas compris votre réponse")
            print("Joueur ", joueur2)
            choix_j1 = input(
                " faîtes votre choix parmi ({liste}): ".format(liste=liste_choix)
            )
            legal_choice = choix_j2 in liste_choix

    # On affiche les choix de chacun
    print("Si on récapitule :", joueur1, choix_j1, "et", joueur2, choix_j2, "\n")

    # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat

    if choix_j1 == choix_j2:
        gagnant = "aucun de vous, vous être ex æquo"
        print(
            "Les scores à l'issue de cette manche sont donc",
            joueur1,
            scoreJ1,
            "et",
            joueur2,
            scoreJ2,
            "\n",
        )

    if choix_j1 == "pierre" and choix_j2 == "ciseaux":
        gagnant = joueur1
        scoreJ1 += 1

    if choix_j1 == "ciseaux" and choix_j2 == "papier":
        gagnant = joueur1
        scoreJ1 += 1

    if choix_j1 == "papier" and choix_j2 == "pierre":
        gagnant = joueur1
        scoreJ1 += 1

    if choix_j1 == "puit" and choix_j2 == "ciseaux":
        gagnant = joueur1
        scoreJ1 += 1

    if choix_j1 == "puit" and choix_j2 == "pierre":
        gagnant = joueur1
        scoreJ1 += 1

    else:
        gagnant = joueur2
        scoreJ2 += 1

    print("le gagnant est", gagnant)
    print(
        "Les scores à l'issue de cette manche sont donc",
        joueur1,
        scoreJ1,
        "et",
        joueur2,
        scoreJ2,
        "\n",
    )

    if nombre_partie < 5:
        continuer = True
    else:
        continuer = False

    if continuer:
        # On propose de continuer ou de s'arrêter
        restart = input(
            "Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(
                joueur1, joueur2
            )
        ).upper()

        if restart == "N":
            continuer = False

        else:
            continuer = True

            print("On continue")

if continuer == False:
    print("Merci d'avoir joué ! A bientôt")
