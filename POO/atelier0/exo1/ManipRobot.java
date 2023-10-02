package POO.atelier0.exo1;

public class ManipRobot {

    public static void main(String[] args) {

        Robot toto = new Robot("Toto", 0, 0, 3);
        Robot titi = new Robot("Titi");
        System.out.println("Création des robots");

        System.out.println(toto);
        System.out.println(titi);

        titi.deplacerRobot();
        toto.deplacerRobot();
        System.out.println("Après déplacement des robots");

        System.out.println(toto);
        System.out.println(titi);

        titi.setOrientation(Robot.SUD);
        toto.setOrientation(Robot.EST);

        System.out.println("Après changement orientation robot");
        System.out.println(toto);
        System.out.println(titi);

        toto.deplacerRobot();
        titi.deplacerRobot();

        System.out.println("Après déplacement des robots");
        System.out.println(toto);
        System.out.println(titi);

    }
}
