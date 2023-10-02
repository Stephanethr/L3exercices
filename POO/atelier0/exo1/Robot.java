package POO.atelier0.exo1;

public class Robot {
    private String ref;
    private String name;
    private int x;
    private int y;
    private int orientation;
    public static int nbRobot = 0;
    public final static int NORD = 1;
    public final static int EST = 2;
    public final static int SUD = 3;
    public final static int OUEST = 4;

    public Robot(String nomRobot, int coordonneeX, int coordonneeY, int orientationInit) {
        nbRobot++;
        this.ref = "ROB" + nbRobot;
        this.name = nomRobot;
        this.x = coordonneeX;
        this.y = coordonneeY;
        this.orientation = orientationInit;
    }

    public Robot(String nomRobot) {
        this(nomRobot, 0, 0, Robot.NORD); // Appelle le constructeur précendent
    }

    public int setOrientation(int value) {
        return this.orientation = value;
    }

    public String getRef() {
        return this.ref;
    }

    public String getName() {
        return this.name;
    }

    public int getAbscisse() {
        return this.x;
    }

    public int getOrdonnee() {
        return this.y;
    }

    public int getOrientation() {
        return this.orientation;
    }

    public void deplacerRobot() {
        if (this.orientation == NORD) {
            this.y++;
        } else if (this.orientation == EST) {
            this.x++;
        } else if (this.orientation == SUD) {
            if (this.y > 0) {
                this.y--;
            }
        } else if (this.orientation == OUEST) {
            if (this.x > 0) {
                this.x--;
            }
        }
    }

    public String toString() {
        return "nom : " + this.getName() + "; référence : " + this.getRef() + "; abscisse : " + this.getAbscisse()
                + "; ordonnée : " + this.getOrdonnee() + "; orientation : " + this.getOrientation();

    }
}
