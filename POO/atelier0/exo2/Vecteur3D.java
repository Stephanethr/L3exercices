package POO.atelier0.exo2;

public class Vecteur3D {
    private float x;
    private float y;
    private float z;

    public Vecteur3D(float x, float y, float z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vecteur3D() {
        this(0, 0, 0);
    }

    public String toString() {
        return "<" + this.x + ", " + this.y + ", " + this.z + ">";
    }

    public float normeVecteur() {
        return (float) Math.sqrt(this.x * this.x + this.y * this.y + this.z + this.z);
    }

    public float produitScalaireI(Vecteur3D v2) {
        return this.x * v2.x + this.y * v2.y + this.z * v2.z;
    }

    public Vecteur3D sommeVecteurI(Vecteur3D v2) {
        return new Vecteur3D(this.x + v2.x, this.y + v2.y, this.z + v2.z);
    }

    public static float produitScalaireC(Vecteur3D v1, Vecteur3D v2) {
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
    }

    public static Vecteur3D sommeVecteurC(Vecteur3D v1, Vecteur3D v2) {
        return new Vecteur3D(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z);
    }
}
