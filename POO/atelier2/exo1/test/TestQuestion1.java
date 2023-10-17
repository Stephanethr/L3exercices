package POO.atelier2.exo1.test;

import java.util.GregorianCalendar;

import POO.atelier2.exo1.Adresse;
import POO.atelier2.exo1.Personne;
import POO.atelier2.exo1.Employe;

public class TestQuestion1 {
    /**
     * @param args
     */
    public static void main(String[] args) {
        System.out.println("TestQuestion1");
        GregorianCalendar dateNaissanceE1 = new GregorianCalendar(1998, 4, 8);
        GregorianCalendar dateNaissance2 = new GregorianCalendar(2000, 4, 8);
        GregorianCalendar dateNaissance3 = new GregorianCalendar(2003, 4, 8);

        // Test de la classe Adresse
        System.out.println("Test de la classe Adresse");
        Adresse a1 = new Adresse(1, "mont thabor", "20000", "Ajaccio");
        Adresse a2 = new Adresse(2, "bonaparte", "20000", "Ajaccio");
        System.out.println("a1 = " + a1);
        System.out.println("a2 = " + a2);

        // Test de la classe Personne
        System.out.println("Test de la classe Personne");
        Personne p1 = new Personne("Dupont", "Jean", dateNaissanceE1, a1);
        Personne p2 = new Personne("Dupont", "Jean", dateNaissance3, a1);
        Personne p3 = new Personne("Dupont", "Jean", dateNaissance2, a2);
        System.out.println("p1 = " + p1);
        System.out.println("p2 = " + p2);

        System.out.println("p1 plus agée que p2 ? " + p1.plusAgeeQue(p2));
        System.out.println("p2 plus agée que p1 ? " + p2.plusAgeeQue(p1));

        System.out.println("p1 plus agée que p2 (méthode statique) ? " + Personne.plusAgee(p1, p2));
        System.out.println("p2 plus agée que p1 (méthode statique) ? " + Personne.plusAgee(p2, p1));
        System.out.println("nombre de personnes créées : " + Personne.nbPersonnes);
        System.out.println("Test égalité entre deux instances de Personne p1 et p2 : " + p1.equals(p2));
        System.out.println("Test égalité entre deux instances de Personne p2 et p3 : " + p2.equals(p3));

        // Test de la classe Employe
        System.out.println("Test de la classe Employe");
        Employe e1 = Employe.createEmploye("Thiry", "Stéphane", dateNaissanceE1, a1, 3000);

        System.out.println("e1 = " + e1);

        e1.augmenterLeSalaire(20);
        System.out.println("Test de la méthode augmenterLeSalaire avec une augmentation de 20 %" + e1);

        GregorianCalendar dateEmbauche = new GregorianCalendar(2010, 4, 25);
        e1.setDateEmbauche(dateEmbauche);
        System.out.println("test setDateEmbauche : " + e1);
        System.out.println("test calculAnnuite : " + e1.calculAnnuite());

        // Test de la classe Manager
        System.out.println("Test de la classe Manager");

    }
}
