import time
from exo4 import extract_elements_list
from exo1 import gen_list_random_int
import random
import matplotlib.pyplot as plt
import numpy as np


def perf_extract(
    extract_elements_list: callable, sample: callable, duree_list: list, nbr_exec: int
) -> tuple:
    """
    Mesure les performances des fonctions extract_elements_list et sample sur des listes de différentes longueurs.

    Args:
        extract_elements_list (callable): Une fonction pour extraire un nombre donné d'éléments d'une liste.
        sample (callable): Une fonction pour échantillonner un nombre donné d'éléments d'une liste.
        duree_list (list): Une liste des longueurs des listes à tester.
        nbr_exec (int): Le nombre d'exécutions à effectuer pour chaque longueur de liste.

    Returns:
        tuple: Un tuple contenant deux listes de temps d'exécution moyen pour extract_elements_list et sample respectivement.
    """
    tps_exec_extract_elements_list = (
        []
    )  # Crée une liste pour stocker les temps d'exécution moyen de extract_elements_list.
    tps_exec_sample = (
        []
    )  # Crée une liste pour stocker les temps d'exécution moyen de sample.

    for i in duree_list:
        tps_extract_elements_list = (
            0  # Initialise le temps d'exécution pour extract_elements_list.
        )
        tps_sample = 0  # Initialise le temps d'exécution pour sample.

        list_test = gen_list_random_int(
            i, 0, i
        )  # Génère une liste aléatoire de longueur i.

        for _ in range(nbr_exec):
            int_nbr_of_element_to_extract = random.randint(0, len(list_test) - 1)
            start_pc = time.perf_counter()

            # Exécute extract_elements_list sur la liste de test et mesure le temps d'exécution.
            extract_elements_list(list_test, int_nbr_of_element_to_extract)

            end_pc = time.perf_counter()
            tps_extract_elements_list += end_pc - start_pc

            start_pc = time.perf_counter()

            # Exécute sample sur la liste de test et mesure le temps d'exécution.
            sample(list_test, int_nbr_of_element_to_extract)

            end_pc = time.perf_counter()
            tps_sample += end_pc - start_pc

        # Calcule le temps d'exécution moyen pour extract_elements_list et sample et les ajoute aux listes correspondantes.
        tps_exec_extract_elements_list.append(tps_extract_elements_list / nbr_exec)
        tps_exec_sample.append(tps_sample / nbr_exec)

    return (tps_exec_extract_elements_list, tps_exec_sample)


list_exec = [10, 500, 5000, 50000, 100000]
resultat_perf = perf_extract(extract_elements_list, random.sample, list_exec, 100)
print(resultat_perf)

# Création d'une liste d'abscisses pour le graphique.
x_axis_list = np.arange(0, 5.5, 0.5)
fig, ax = plt.subplots()

# Tracez les performances de extract_elements_list et sample.
ax.plot(list_exec, resultat_perf[0], "bo-", label="extract_elements_list")
ax.plot(list_exec, resultat_perf[1], "r*-", label="sample")
ax.set(
    xlabel="Taille de la liste",  # Nom de l'axe des abscisses.
    ylabel="Temps d'exécution (s)",  # Nom de l'axe des ordonnées.
    title="Comparaison des performances de extract_elements_list et sample",  # Titre du graphique.
)
ax.legend(
    loc="upper center", shadow=True, fontsize="x-large"
)  # Légende pour les courbes.
plt.show()  # Affiche le graphique.
