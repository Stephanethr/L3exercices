package POO.atelier0.exo3;

import java.util.Random;

public class TestAPI {
    public static void main(String[] args) {
        double pi = Math.PI;
        System.out.println("La valeur de PI est : " + pi);
        double randomValue = Math.random();
        System.out.println("Nombre aléatoire : " + randomValue);

        Random random = new Random();
        int rand = random.nextInt(3) + 1;
        System.out.println("Nombre aléatoire : " + rand);

        int x1 = 5;
        int x2 = 7;
        System.out.println("plus grande valeur : " + Math.max(x1, x2));

        String n1 = "abc";
        String n2 = "def";
        System.out.println("Comparaison string : " + n1.compareTo(n2));

    }
}
