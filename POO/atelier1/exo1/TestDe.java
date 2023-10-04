/**
 * La classe TestDe est utilisée pour tester les fonctionnalités des classes De, DePipe et DeMemoire.
 * Elle crée des instances de ces classes, effectue des lancers de dés et affiche les résultats.
 */
package POO.atelier1.exo1;

public class TestDe {

    /**
     * Méthode principale du programme de test.
     *
     * @param args Les arguments de la ligne de commande (non utilisés dans ce
     *             programme).
     */
    public static void main(String[] args) {
        // Création de différents dés avec leurs paramètres
        De de1 = new De("de24Faces", 24);
        De deEquals1 = new De("de24Faces", 24);
        De de2 = new De();
        De de3 = new De(8);
        De de3Erreur = new De(7);
        De de4 = new De("de6faces");

        System.out.println(de1 + " " + de2 + " " + de3 + " " + " " + de3Erreur + de4); // Affichage des dés créés

        // Affichage des résultats des lancers de dés
        for (De de : De.listDe) {
            System.out.println("Le lancé du dé : " + de.getNom() + " à " + de.getNbFaces()
                    + " faces a donné la valeur : " + de.lancer());
        }

        // Nombre de lancers à effectuer
        int nbLance = 10;

        // Affichage des meilleurs résultats sur un certain nombre de lancers
        for (De de : De.listDe) {
            System.out.println("Sur " + nbLance + " lancés, " + "Le meilleur lancé du dé : " + de.getNom() + " à "
                    + de.getNbFaces()
                    + " faces est : " + de.lancer(nbLance));
        }

        // Utilisation de la méthode toString et equals
        System.out.println("override toString : " + de1);
        System.out.println("override equals : " + de1.equals(deEquals1));

        // Création et utilisation d'un dé avec borne minimale
        DePipe dePipe = new DePipe("dePipé", 8, 4);
        System.out.println("La valeur de lancé du dé pipé dont la borne minimale est : " + dePipe.getBorneMinimale()
                + " est égale à : " + dePipe.lancer());

        // Création et utilisation d'un dé avec mémoire
        DeMemoire deMemoire = new DeMemoire("deMemoire", 6);
        int count = 0;
        int nbTest = 10;
        while (count <= nbTest) {
            System.out.println("lancé numéro " + count + " ; valeur = " + deMemoire.lancer());
            count++;
        }
    }
}
