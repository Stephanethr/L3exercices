import random


def places_lettre(ch: str, mot: str) -> list:
    """_summary_

    Args:
        ch (str): _description_
        mot (str): _description_

    Returns:
        list: _description_
    """
    len_mot = len(mot)
    res = []
    for i in range(len_mot):
        if mot[i] == ch:
            res.append(i)
    return res


def outputStr(mot: str, lpos: list) -> str:
    """_summary_

    Args:
        mot (str): _description_
        lpos (list): _description_

    Returns:
        str: _description_
    """
    res = ""
    for i in range(len(mot)):
        if i in lpos:
            res += mot[i]
        else:
            res += "_"
    return res


def runGame():
    word_list = ["paris", "londres", "madrid", "berlin", "new-york"]

    selected_word = random.choice(word_list)

    errors = 0

    guessed_letters = []

    while errors < 5:
        current_state = outputStr(selected_word, guessed_letters)
        print(f"Mot actuel: {current_state}")

        guess = input("Devinez une lettre : ")

        if guess in guessed_letters:
            print("Vous avez déjà deviné cette lettre.")
            continue

        letter_indices = places_lettre(guess, selected_word)

        if letter_indices:
            print(
                f"La lettre '{guess}' est dans le mot aux positions {', '.join(map(str, letter_indices))}."
            )
            guessed_letters.append(guess)
        else:
            errors += 1

            if errors == 1:
                print("|______")
            elif errors == 2:
                print("| T ")
            elif errors == 3:
                print("| O ")
            elif errors == 4:
                print("|/ \\")
            elif errors == 5:
                print("|---] ")

        remaining_attempts = 5 - errors
        print(f"Nombre de coups restants : {remaining_attempts}")

        if set(guessed_letters) == set(selected_word):
            print(
                f"Félicitations ! Vous avez deviné le mot '{selected_word}'. Vous avez gagné !"
            )
            break

    if errors == 5:
        print(f"Perdu. Le mot était '{selected_word}'.")


# Exécution du jeu
runGame()
