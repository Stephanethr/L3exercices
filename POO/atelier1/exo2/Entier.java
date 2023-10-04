/**
 * La classe Entier représente un nombre entier compris entre une borne minimale et une borne maximale.
 * Elle permet de manipuler et de vérifier la valeur de cet entier dans les bornes spécifiées.
 */
package POO.atelier1.exo2;

public class Entier {
    private int borneMini; // La borne minimale de l'entier.
    private int borneMaxi; // La borne maximale de l'entier.
    private int value; // La valeur de l'entier.

    /**
     * Constructeur de la classe Entier avec bornes minimale, maximale et valeur
     * initiale spécifiées.
     *
     * @param borneMini La borne minimale de l'entier.
     * @param borneMaxi La borne maximale de l'entier.
     * @param value     La valeur initiale de l'entier.
     */
    public Entier(int borneMini, int borneMaxi, int value) {
        this.borneMini = borneMini;
        this.borneMaxi = borneMaxi > borneMini ? borneMaxi : borneMini + 2;
        this.value = verifValue(value) ? value : 0;
    }

    /**
     * Constructeur de la classe Entier avec bornes minimale et maximale spécifiées.
     * Initialise la valeur de l'entier à zéro.
     *
     * @param borneMini La borne minimale de l'entier.
     * @param borneMaxi La borne maximale de l'entier.
     */
    public Entier(int borneMini, int borneMaxi) {
        this.borneMini = borneMini;
        this.borneMaxi = borneMaxi;
        this.value = 0;
    }

    /**
     * Obtient la borne minimale de l'entier.
     *
     * @return La borne minimale.
     */
    public int getBorneMini() {
        return this.borneMini;
    }

    /**
     * Obtient la borne maximale de l'entier.
     *
     * @return La borne maximale.
     */
    public int getBorneMaxi() {
        return this.borneMaxi;
    }

    /**
     * Obtient la valeur de l'entier.
     *
     * @return La valeur de l'entier.
     */
    public int getValue() {
        return this.value;
    }

    /**
     * Modifie la valeur de l'entier si la nouvelle valeur est valide.
     *
     * @param value La nouvelle valeur de l'entier.
     */
    public void setValue(int value) {
        this.value = verifValue(value) ? value : this.value;
    }

    /**
     * Vérifie si une valeur est valide pour l'entier, c'est-à-dire si elle est
     * comprise entre les bornes minimale et maximale (excluses).
     *
     * @param value La valeur à vérifier.
     * @return true si la valeur est valide, sinon false.
     */
    public boolean verifValue(int value) {
        return value > this.borneMini && value < this.borneMaxi;
    }

    /**
     * Incrémente la valeur de l'entier d'une unité si la nouvelle valeur est
     * valide.
     */
    public void incrementeValue() {
        this.value = verifValue(this.value + 1) ? this.value + 1 : this.value;
    }

    /**
     * Incrémente la valeur de l'entier par un nombre spécifié si la nouvelle valeur
     * est valide.
     *
     * @param n Le nombre à ajouter à la valeur de l'entier.
     */
    public void incrementeValue(int n) {
        this.value = verifValue(this.value + n) ? this.value + n : this.value;
    }

    /**
     * Obtient une représentation sous forme de chaîne de caractères de l'entier.
     *
     * @return Une chaîne de caractères représentant l'entier.
     */
    public String toString() {
        return "Entier : " + this.value + " compris entre " + this.borneMini + " et " + this.borneMaxi;
    }

    /**
     * Compare deux entiers pour déterminer s'ils sont égaux (même bornes minimale,
     * maximale et valeur).
     *
     * @param obj L'objet à comparer avec l'entier.
     * @return true si les objets sont égaux, sinon false.
     */
    public boolean equals(Object obj) {
        boolean result = false;
        if ((obj != null) && (obj instanceof Entier)) {
            Entier entier = (Entier) obj;
            result = this.borneMini == entier.borneMini && this.borneMaxi == entier.borneMaxi
                    && this.value == entier.value;
        }
        return result;

    }
}