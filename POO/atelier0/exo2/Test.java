package POO.atelier0.exo2;

import java.text.DecimalFormat;

public class Test {
    public static void main(String[] args) {
        Vecteur3D v1 = new Vecteur3D(1.0f, 2.0f, 3.0f);
        Vecteur3D v2 = new Vecteur3D(3.0f, 2.0f, 5.0f);

        System.out.println(v1);
        System.out.println(v2);

        System.out.println(v1.normeVecteur());
        DecimalFormat df = new DecimalFormat("#0.00");
        System.out.println(df.format(v1.normeVecteur()));

        System.out.println(v1.produitScalaireI(v2));

        System.out.println(Vecteur3D.produitScalaireC(v2, v1));

        System.out.println(v1.sommeVecteurI(v2));

        System.out.println(Vecteur3D.sommeVecteurC(v1, v2));

    }
}
