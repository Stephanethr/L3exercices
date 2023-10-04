/**
 * La classe DePipe est une sous-classe de la classe De, qui représente un dé avec une borne minimale.
 * Elle permet de lancer le dé de manière à obtenir un résultat supérieur ou égal à une borne minimale spécifiée.
 */
package POO.atelier1.exo1;

public class DePipe extends De {
    private int borneMinimale; // La borne minimale pour le résultat du lancer.

    /**
     * Constructeur de la classe DePipe.
     *
     * @param nom           Le nom du dé.
     * @param nbFaces       Le nombre de faces du dé.
     * @param borneMinimale La borne minimale pour le résultat du lancer.
     */
    public DePipe(String nom, int nbFaces, int borneMinimale) {
        super(nom, nbFaces); // Appelle le constructeur de la classe parente (De).
        this.borneMinimale = verifBorneMinimale(borneMinimale);
    }

    /**
     * Obtient la borne minimale pour le résultat du lancer.
     *
     * @return La borne minimale.
     */
    public int getBorneMinimale() {
        return this.borneMinimale;
    }

    /**
     * Vérifie que la borne minimale est comprise entre 0 et le nombre de faces
     * inclus.
     * Si la valeur est invalide, affiche un message d'erreur.
     *
     * @param valeur La valeur de la borne minimale à vérifier.
     * @return La valeur de la borne minimale validée ou -1 en cas d'erreur.
     */
    public int verifBorneMinimale(int valeur) {
        if (valeur >= 0 && valeur <= this.getNbFaces()) {
            return valeur;
        } else {
            System.err.println("La borne minimale du dé : " + this.getNom()
                    + " n'est pas comprise entre 0 et le nombre de faces du dé inclus.");
            return -1;
        }
    }

    /**
     * Lance le dé de manière à obtenir un résultat supérieur ou égal à la borne
     * minimale spécifiée.
     * Si le résultat est inférieur à la borne minimale, relance le dé jusqu'à
     * obtenir un résultat valide.
     *
     * @return Le résultat du lancer de dé avec la borne minimale.
     */
    public int lancer() {
        int res = 0;
        while (res < this.borneMinimale) {
            int valeurDe = super.lancer(); // Appelle la méthode lancer de la classe parente (De).
            if (valeurDe >= this.borneMinimale) {
                res = valeurDe;
            }
        }
        return res;
    }
}
