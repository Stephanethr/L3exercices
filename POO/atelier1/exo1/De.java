/**
 * La classe De représente un dé avec un nom et un nombre de faces.
 * Elle permet de lancer le dé pour obtenir un résultat aléatoire.
 */
package POO.atelier1.exo1;

import java.util.*;

public class De {
    private String nom; // Le nom du dé.
    private int nbFaces; // Le nombre de faces du dé.
    private static Random r = new Random();
    private final static int MAXFACE = 120;
    private final static int MINFACE = 3;
    public static int nbDe = 0; // Le nombre total de dés créés.
    public static ArrayList<De> listDe = new ArrayList<De>(); // Liste des dés créés.

    /**
     * Constructeur de la classe De.
     *
     * @param nom     Le nom du dé.
     * @param nbFaces Le nombre de faces du dé.
     */
    public De(String nom, int nbFaces) {
        nbDe++;
        this.nom = nom;
        this.nbFaces = verifNbFaces(nbFaces);
        listDe.add(this);
    }

    /**
     * Constructeur par défaut de la classe De.
     * Crée un dé avec un nom par défaut "De" suivi du nombre de dés créés,
     * et 6 faces par défaut.
     */
    public De() {
        this("De" + nbDe, 6);
    }

    /**
     * Constructeur de la classe De avec un nombre de faces spécifié.
     * Crée un dé avec un nom par défaut "De" suivi du nombre de dés créés,
     * et le nombre de faces spécifié.
     *
     * @param nbFaces Le nombre de faces du dé.
     */
    public De(int nbFaces) {
        this("De" + nbDe, nbFaces);
    }

    /**
     * Constructeur de la classe De avec un nom spécifié.
     * Crée un dé avec le nom spécifié et 6 faces par défaut.
     *
     * @param nom Le nom du dé.
     */
    public De(String nom) {
        this(nom, 6);
    }

    /**
     * Vérifie que le nombre de faces du dé est compris entre 3 et 120 inclus.
     * Si le nombre de faces est invalide, affiche un message d'erreur.
     *
     * @param nb Le nombre de faces à vérifier.
     * @return Le nombre de faces validé ou -1 en cas d'erreur.
     */
    public int verifNbFaces(int nb) {
        if (nb >= MINFACE && nb <= MAXFACE) {
            return nb;
        } else {
            System.err.println("Le nombre de faces du dé : " + this.nom + " n'est pas compris entre 3 et 120 inclus.");
            return -1;
        }
    }

    /**
     * Modifie le nombre de faces du dé.
     *
     * @param nb Le nouveau nombre de faces du dé.
     */
    public void setNbFaces(int nb) {
        this.nbFaces = verifNbFaces(nb);
    }

    /**
     * Obtient le nombre de faces du dé.
     *
     * @return Le nombre de faces du dé.
     */
    public int getNbFaces() {
        return this.nbFaces;
    }

    /**
     * Obtient le nom du dé.
     *
     * @return Le nom du dé.
     */
    public String getNom() {
        return this.nom;
    }

    /**
     * Lance le dé une fois et retourne un résultat aléatoire entre 1 et le nombre
     * de faces.
     *
     * @return Le résultat du lancer de dé.
     */
    public int lancer() {
        return 1 + r.nextInt(this.getNbFaces());
    }

    /**
     * Lance le dé un nombre spécifié de fois et retourne le plus grand résultat
     * obtenu.
     *
     * @param nb Le nombre de lancers de dé.
     * @return Le résultat du lancer de dé le plus élevé.
     */
    public int lancer(int nb) {
        int res = 0;
        int count = 0;
        while (count < nb) {
            int valeurDe = 1 + r.nextInt(this.getNbFaces());
            if (valeurDe > res) {
                res = valeurDe;
            }
            count++;
        }
        return res;
    }

    /**
     * Obtient une représentation sous forme de chaîne de caractères du dé.
     *
     * @return Une chaîne de caractères représentant le dé.
     */
    public String toString() {
        return "nom du dé : " + this.getNom() + "\nnombre de faces : " + this.getNbFaces();
    }

    /**
     * Compare deux dés pour déterminer s'ils sont égaux (même nom et même nombre de
     * faces).
     *
     * @param obj L'objet à comparer avec le dé.
     * @return true si les objets sont égaux, sinon false.
     */

    public boolean equals(Object obj) {
        boolean result = false;
        if ((obj != null) && (obj instanceof De)) {
            De de2 = (De) obj;
            result = (this.nom.equals(de2.nom)) && (this.nbFaces == de2.nbFaces);
        }
        return result;
    }

}
