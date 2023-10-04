/**
 * La classe TestEntier est utilisée pour tester les fonctionnalités des classes Entier et EntierFou.
 * Elle crée des instances de ces classes, effectue des opérations sur les entiers et affiche les résultats.
 */
package POO.atelier1.exo2;

public class TestEntier {
    public static void main(String[] args) {
        // Création d'entiers avec différentes configurations
        Entier entier1 = new Entier(1, 7);
        Entier entier2 = new Entier(1, 7, 3);
        EntierFou entierFou1 = new EntierFou(1, 10000, 3, 7);
        Entier entierErreur1 = new Entier(3, 1); // Les bornes sont inversées, une erreur sera affichée.
        Entier entierErreur2 = new Entier(1, 7, 8); // La valeur est en dehors des bornes, une erreur sera affichée.

        // Affichage des entiers créés
        System.out.println(entier1);
        System.out.println(entier2);

        // Affichage des entiers avec des configurations erronées (erreurs affichées)
        System.out.println(entierErreur1);
        System.out.println(entierErreur2);

        System.out.println("entierFou1 avant incrémentation");
        System.out.println(entierFou1);

        // Incrémentation de l'entier fou et affichage des résultats
        entierFou1.incrementeValue();
        System.out.println("entierFou1 après incrémentation");
        System.out.println(entierFou1);

        // Incrémentation de l'entier fou jusqu'à ce qu'il atteigne sa borne maximale
        while (entierFou1.getValue() < entierFou1.getBorneMaxi() - 1) {
            entierFou1.incrementeValue();
            System.out.println(entierFou1);
        }
    }
}
