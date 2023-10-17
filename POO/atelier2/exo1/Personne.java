package POO.atelier2.exo1;

import java.util.*;

public class Personne {
	private static final Adresse ADRESSE_INCONNUE = null;
	private String nom;
	private String prenom;
	private final GregorianCalendar dateNaissance;
	private Adresse adresse = ADRESSE_INCONNUE;
	public static int nbPersonnes = 0;

	/**
	 * Constructeur de Personne
	 * 
	 * @param leNom    le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param laDate   la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom, String lePrenom, GregorianCalendar laDate, Adresse lAdresse) {
		nbPersonnes++;
		nom = leNom.toUpperCase();
		prenom = lePrenom;
		dateNaissance = laDate;
		adresse = lAdresse;
	}

	/**
	 * Constructeur de Personne
	 * 
	 * @param leNom       le nom de la personne
	 * @param lePrenom    le pr�nom de la personne
	 * @param j           le jour de naissance
	 * @param m           le mois de naissance
	 * @param a           l'ann�e de naissance
	 * @param numero      le n� de la rue
	 * @param rue         la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville       la ville ou la personne habite
	 */
	public Personne(String leNom, String lePrenom, int j, int m, int a, int numero, String rue, String code_postal,
			String ville) {
		this(leNom, lePrenom, new GregorianCalendar(a, m, j), new Adresse(numero, rue, code_postal, ville));
	}

	/**
	 * Accesseur
	 * 
	 * @return retourne le nom
	 */
	public String getNom() {
		return nom;
	}

	/**
	 * Accesseur
	 * 
	 * @return retourne le pr�nom
	 */
	public String getPrenom() {
		return prenom;
	}

	/**
	 * Accesseur
	 * 
	 * @return retourne la date de naissance
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}

	/**
	 * Accesseur
	 * 
	 * @return retourne l'adresse
	 */
	public Adresse getAdresse() {
		return adresse;
	}

	/**
	 * Modificateur
	 * 
	 * @param retourne l'adresse
	 */
	public void setAdresse(Adresse a) {
		adresse = a;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see java.lang.Object#toString()
	 */
	public String toString() {
		String result = "\nNom : " + nom + "\n"
				+ "Prénom : " + prenom + "\n" +
				"Né(e) le : " + dateNaissance.get(Calendar.DAY_OF_MONTH) +
				"-" + dateNaissance.get(Calendar.MONTH) +
				"-" + dateNaissance.get(Calendar.YEAR) + "\n" +
				"Adresse : " +
				adresse.toString();
		return result;
	}

	public static boolean plusAgee(Personne personne1, Personne personne2) {
		return personne1.dateNaissance.before(personne2.dateNaissance);
	}

	public boolean plusAgeeQue(Personne personne2) {
		return this.dateNaissance.before(personne2.dateNaissance);
	}

	public boolean equals(Object obj) {
		boolean result = false;
		if ((obj != null) && (obj instanceof Personne)) {
			Personne personne2 = (Personne) obj;
			result = this.nom.equals(personne2.nom) && this.prenom.equals(personne2.prenom)
					&& this.dateNaissance.equals(personne2.dateNaissance);
		}
		return result;
	}

}
