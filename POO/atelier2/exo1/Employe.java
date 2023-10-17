package POO.atelier2.exo1;

import java.util.GregorianCalendar;

public class Employe extends Personne {
    private double salaire;
    private GregorianCalendar dateEmbauche;

    protected Employe(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, double salaire) {
        super(nom, prenom, dateNaissance, adresse);
        this.salaire = salaire;
        this.dateEmbauche = new GregorianCalendar();
    }

    public GregorianCalendar getDateEmbauche() {
        return this.dateEmbauche;
    }

    public void setDateEmbauche(GregorianCalendar dateEmbauche) {
        this.dateEmbauche = dateEmbauche;
    }

    public double getSalaire() {
        return this.salaire;
    }

    public static Employe createEmploye(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse,
            int salaire) {
        Employe employe = new Employe(nom, prenom, dateNaissance, adresse, salaire);
        int ageEmploye = employe.calculAge();
        if (ageEmploye < 16 || ageEmploye > 65) {
            throw new IllegalArgumentException("L'employé doit avoir entre 16 et 65 ans");
        } else {
            return employe;
        }

    }

    public int calculAge() {
        GregorianCalendar today = new GregorianCalendar();
        int age = today.get(GregorianCalendar.YEAR) - this.getDateNaissance().get(GregorianCalendar.YEAR);
        if (today.get(GregorianCalendar.MONTH) < this.getDateNaissance().get(GregorianCalendar.MONTH)) {
            age--;
        } else if (today.get(GregorianCalendar.MONTH) == this.getDateNaissance().get(GregorianCalendar.MONTH)) {
            if (today.get(GregorianCalendar.DAY_OF_MONTH) < this.getDateNaissance()
                    .get(GregorianCalendar.DAY_OF_MONTH)) {
                age--;
            }
        }
        return age;
    }

    public void augmenterLeSalaire(double pourcentage) {
        if (pourcentage < 0) {
            throw new IllegalArgumentException("Le pourcentage doit être positif");
        }
        this.salaire = this.salaire + (this.salaire * pourcentage / 100);
    }

    public int calculAnnuite() {
        GregorianCalendar today = new GregorianCalendar();
        int annee = today.get(GregorianCalendar.YEAR) - this.getDateEmbauche().get(GregorianCalendar.YEAR);
        if (today.get(GregorianCalendar.MONTH) < this.getDateEmbauche().get(GregorianCalendar.MONTH)) {
            annee--;
        } else if (today.get(GregorianCalendar.MONTH) == this.getDateEmbauche().get(GregorianCalendar.MONTH)) {
            if (today.get(GregorianCalendar.DAY_OF_MONTH) < this.getDateEmbauche()
                    .get(GregorianCalendar.DAY_OF_MONTH)) {
                annee--;
            }
        }
        return annee;
    }

    public boolean equals(Object o) {
        if (o instanceof Employe) {
            Employe e = (Employe) o;
            return super.equals(e) && this.salaire == e.salaire
                    && this.dateEmbauche.equals(e.dateEmbauche);
        } else {
            return false;
        }
    }

    public String toString() {
        return super.toString() + "\nSalaire : " + this.salaire + " Euros\nDate d'embauche : "
                + this.dateEmbauche.get(GregorianCalendar.DAY_OF_MONTH) + "-"
                + this.dateEmbauche.get(GregorianCalendar.MONTH) + "-"
                + this.dateEmbauche.get(GregorianCalendar.YEAR);
    }
}
