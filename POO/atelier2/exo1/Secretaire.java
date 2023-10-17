package POO.atelier2.exo1;

import java.util.*;

public class Secretaire extends Employe {

    public ArrayList<Manager> listManager = new ArrayList<Manager>();

    public Secretaire(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, double salaire,
            ArrayList<Manager> listManager) {
        super(nom, prenom, dateNaissance, adresse, salaire);
        setManager(listManager);
    }

    public void setManager(Manager manager) {
        if (this.listManager.contains(manager)) {
            throw new IllegalArgumentException("Le manager est déjà dans la liste");
        } else if (this.listManager.size() > 5) {
            throw new IllegalArgumentException("Cette secrétaire a déjà 5 managers");
        } else {
            this.listManager.add(manager);
        }
    }

    public void setManager(ArrayList<Manager> newListManager) {
        if ((newListManager.size() + this.listManager.size()) > 5) {
            throw new IllegalArgumentException(
                    "Avec l'ajout de la nouvelle liste de manager la secrétaire aura plus de 5 managers, par conséquent aucun ne sera ajouté.");
        } else {
            for (Manager manager : newListManager) {
                setManager(manager);
            }
        }
    }

    public void deleteManager(Manager manager) {
        this.listManager.remove(manager);
    }

    public void augmenterLeSalaire(double pourcentage) {
        super.augmenterLeSalaire(pourcentage + (this.listManager.size() * 0.1));
    }
}
