package POO.atelier2.exo1;

import java.util.*;

public class Manager extends Employe {
    private Secretaire secretaire;

    public Manager(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, double salaire,
            Secretaire secretaire) {
        super(nom, prenom, dateNaissance, adresse, salaire);
        this.secretaire = secretaire;
    }

    public Secretaire getSecretaire() {
        return this.secretaire;
    }

    public void setSecretaire(Secretaire secretaire) {
        this.secretaire.deleteManager(this);
        this.secretaire = secretaire;
        secretaire.setManager(this);
    }

    public void augmenterLeSalaire(double pourcentage) {
        super.augmenterLeSalaire(pourcentage + (this.calculAnnuite() * 0.5));
    }
}
