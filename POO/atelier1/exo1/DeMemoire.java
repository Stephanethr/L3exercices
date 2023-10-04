/**
 * La classe DeMemoire est une sous-classe de la classe De, qui représente un dé avec mémoire.
 * Elle permet de lancer le dé de manière à éviter d'obtenir le même résultat deux fois consécutives.
 */
package POO.atelier1.exo1;

public class DeMemoire extends De {
    private int memoire; // Le résultat précédemment obtenu lors du lancer du dé.

    /**
     * Constructeur de la classe DeMemoire.
     *
     * @param nom     Le nom du dé.
     * @param nbFaces Le nombre de faces du dé.
     */
    public DeMemoire(String nom, int nbFaces) {
        super(nom, nbFaces); // Appelle le constructeur de la classe parente (De).
        this.memoire = 0; // Initialise la mémoire à 0.
    }

    /**
     * Obtient la valeur enregistrée dans la mémoire du dé.
     *
     * @return La valeur enregistrée dans la mémoire.
     */
    public int getMemoire() {
        return this.memoire;
    }

    /**
     * Lance le dé de manière à éviter d'obtenir le même résultat deux fois
     * consécutives.
     * Si le résultat est le même que celui enregistré en mémoire, relance le dé
     * jusqu'à obtenir un résultat différent.
     * Enregistre ensuite le résultat dans la mémoire avant de le retourner.
     *
     * @return Le résultat du lancer de dé avec mémoire.
     */
    public int lancer() {
        int res;
        do {
            res = super.lancer(); // Appelle la méthode lancer de la classe parente (De).
        } while (res == this.memoire); // Répète le lancer tant que le résultat est le même que celui enregistré en
                                       // mémoire.
        this.memoire = res; // Enregistre le résultat dans la mémoire.
        return res;
    }
}
