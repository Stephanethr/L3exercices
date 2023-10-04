package POO.atelier2.exo1.test;

import POO.atelier2.exo1.Adresse;
import POO.atelier2.exo1.Personne;

public class TestQuestion1 {
    public static void main(String[] args) {
        System.out.println("TestQuestion1");

        // Test de la classe Adresse
        System.out.println("Test de la classe Adresse");
        Adresse a1 = new Adresse(1, "rue de la paix", "75000", "Paris");
        Adresse a2 = new Adresse(2, "rue de la paix", "75000", "Paris");
        System.out.println("a1 = " + a1);
        System.out.println("a2 = " + a2);

        // Test de la classe Personne
        System.out.println("Test de la classe Personne");
        Personne p1 = new Personne("Dupont", "Jean", 1, 1, 1998, 1, "rue de la paix", "75000", "Paris");
        Personne p2 = new Personne("Turcq", "Fred", 1, 1, 2003, 1, "agosta", "20160", "Porticcio");
        System.out.println("p1 = " + p1);
        System.out.println("p2 = " + p2);
    }
}
