/**
 * La classe EntierFou est une sous-classe de la classe Entier, qui représente un nombre entier
 * avec un niveau de folie associé.
 * Elle permet d'augmenter la valeur de manière aléatoire en fonction du niveau de folie.
 */
package POO.atelier1.exo2;

import java.util.Random;

public class EntierFou extends Entier {
    private int niveauDeFolie; // Le niveau de folie associé à l'entier.
    private static Random r = new Random(); // Générateur de nombres aléatoires.

    /**
     * Constructeur de la classe EntierFou avec bornes minimale, maximale, valeur
     * initiale et niveau de folie spécifiés.
     *
     * @param borneMini     La borne minimale de l'entier.
     * @param borneMaxi     La borne maximale de l'entier.
     * @param value         La valeur initiale de l'entier.
     * @param niveauDeFolie Le niveau de folie associé à l'entier.
     */
    public EntierFou(int borneMini, int borneMaxi, int value, int niveauDeFolie) {
        super(borneMini, borneMaxi, value); // Appelle le constructeur de la classe parente (Entier).
        this.niveauDeFolie = niveauDeFolie;
    }

    /**
     * Obtient le niveau de folie associé à l'entier.
     *
     * @return Le niveau de folie.
     */
    public int getNiveauDeFolie() {
        return this.niveauDeFolie;
    }

    /**
     * Incrémente la valeur de l'entier de manière aléatoire en fonction du niveau
     * de folie.
     * La valeur est augmentée d'un nombre aléatoire compris entre 0 et le niveau de
     * folie.
     */
    public void incrementeValue() {
        super.incrementeValue(r.nextInt(this.niveauDeFolie + 1));
    }
}
