import time
from exo2 import mix_list
from exo1 import gen_list_random_int
import random
import matplotlib.pyplot as plt
import numpy as np


def perf_mix(
    mix_list: callable, shuffle: callable, duree_list: list, nbr_exec: int
) -> tuple:
    """
    Mesure les performances des fonctions mix_list et shuffle sur des listes de différentes longueurs.

    Args:
        mix_list (callable): Une fonction pour mélanger une liste.
        shuffle (callable): Une fonction pour mélanger une liste (par exemple, la fonction shuffle du module random).
        duree_list (list): Une liste des longueurs des listes à tester.
        nbr_exec (int): Le nombre d'exécutions à effectuer pour chaque longueur de liste.

    Returns:
        tuple: Un tuple contenant deux listes de temps d'exécution moyen pour mix_list et shuffle respectivement.
    """
    tps_exec_mix_list = (
        []
    )  # Crée une liste pour stocker les temps d'exécution moyen de mix_list.
    tps_exec_shuffle = (
        []
    )  # Crée une liste pour stocker les temps d'exécution moyen de shuffle.

    for i in duree_list:
        tps_mix_list = 0  # Initialise le temps d'exécution pour mix_list.
        tps_shuffle = 0  # Initialise le temps d'exécution pour shuffle.

        list_test = gen_list_random_int(
            i, 0, i
        )  # Génère une liste aléatoire de longueur i.

        for _ in range(nbr_exec):
            start_pc = time.perf_counter()

            # Exécute mix_list sur la liste de test et mesure le temps d'exécution.
            mix_list(list_test)

            end_pc = time.perf_counter()
            tps_mix_list += end_pc - start_pc

            start_pc = time.perf_counter()

            # Exécute shuffle sur la liste de test et mesure le temps d'exécution.
            shuffle(list_test)

            end_pc = time.perf_counter()
            tps_shuffle += end_pc - start_pc

        # Calcule le temps d'exécution moyen pour mix_list et shuffle et les ajoute aux listes correspondantes.
        tps_exec_mix_list.append(tps_mix_list / nbr_exec)
        tps_exec_shuffle.append(tps_shuffle / nbr_exec)

    return (tps_exec_mix_list, tps_exec_shuffle)


list_exec = [10, 500, 5000, 50000, 100000]
resultat_perf = perf_mix(mix_list, random.shuffle, list_exec, 100)
print(resultat_perf)

# Création d'une liste d'abscisses pour le graphique.
x_axis_list = np.arange(0, 5.5, 0.5)
fig, ax = plt.subplots()

# Tracez les performances de mix_list et shuffle.
ax.plot(list_exec, resultat_perf[0], "bo-", label="mix_list")
ax.plot(list_exec, resultat_perf[1], "r*-", label="shuffle")
ax.set(
    xlabel="Taille de la liste",  # Nom de l'axe des abscisses.
    ylabel="Temps d'exécution (s)",  # Nom de l'axe des ordonnées.
    title="Comparaison des performances de mix_list et shuffle",  # Titre du graphique.
)
ax.legend(
    loc="upper center", shadow=True, fontsize="x-large"
)  # Légende pour les courbes.
plt.show()  # Affiche le graphique.
