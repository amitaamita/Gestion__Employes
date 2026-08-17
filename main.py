"""Point d'entrée principal de l'application."""
from employe import Employe
from departement import Departement
from gestion_employes import GestionEmployes
from gestion_departements import GestionDepartements
from exceptions import SalaireNegatifError, AgeInvalideError, MatriculeInexistantError


def afficher_menu():
    """Affiche le menu principal."""
    print("\n======================================")
    print("     GESTION DES EMPLOYÉS")
    print("======================================")
    print("1. Ajouter un employé")
    print("2. Modifier un employé")
    print("3. Supprimer un employé")
    print("4. Rechercher un employé")
    print("5. Afficher tous les employés")
    print("6. Gérer les départements")
    print("7. Statistiques")
    print("8. Sauvegarder les données")
    print("9. Quitter")
    print("======================================")


def main():
    """Fonction principale exécutant la boucle de l'application."""
    gestion_emp = GestionEmployes()
    gestion_dept = GestionDepartements(gestion_emp)

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == '1':
            try:
                print("\n--- Ajout d'un employé ---")
                mat = input("Matricule : ")
                nom = input("Nom : ")
                prenom = input("Prénom : ")
                age = int(input("Âge : "))
                sexe = input("Sexe : ")
                adresse = input("Adresse : ")
                tel = input("Téléphone : ")
                poste = input("Poste : ")
                salaire = float(input("Salaire : "))
                code_dept = input("Code département : ")
                
                emp = Employe(mat, nom, prenom, age, sexe, adresse, tel, poste, salaire, code_dept)
                gestion_emp.ajouter_employe(emp)
                print("Employé ajouté avec succès !")
            except ValueError:
                print("Erreur : Veuillez entrer des nombres valides pour l'âge et le salaire.")
            except (SalaireNegatifError, AgeInvalideError) as e:
                print(f"Erreur de saisie : {e}")

        elif choix == '2':
            try:
                mat = input("Matricule de l'employé à modifier : ")
                print("Laissez vide si vous ne voulez pas modifier le champ.")
                nouvelles_donnees = {
                    "poste": input("Nouveau poste : "),
                    "salaire": float(input("Nouveau salaire : ")) if input("Modifier salaire ? (o/n) : ").lower() == 'o' else None,
                    "adresse": input("Nouvelle adresse : "),
                    "telephone": input("Nouveau téléphone : "),
                    "code_dept": input("Nouveau code département : ")
                }
                # Nettoyage des None
                nouvelles_donnees = {k: v for k, v in nouvelles_donnees.items() if v is not None and v != ""}
                gestion_emp.modifier_employe(mat, nouvelles_donnees)
                print("Employé modifié avec succès !")
            except MatriculeInexistantError as e:
                print(e)
            except SalaireNegatifError as e:
                print(e)

        elif choix == '3':
            try:
                mat = input("Matricule de l'employé à supprimer : ")
                gestion_emp.supprimer_employe(mat)
                print("Employé supprimé avec succès !")
            except MatriculeInexistantError as e:
                print(e)

        elif choix == '4':
            try:
                mat = input("Matricule de l'employé à rechercher : ")
                emp = gestion_emp.rechercher_employe(mat)
                print(emp.afficher())
            except MatriculeInexistantError as e:
                print(e)

        elif choix == '5':
            gestion_emp.afficher_tous()

        elif choix == '6':
            gestion_dept.afficher_sous_menu()

        elif choix == '7':
            stats = gestion_emp.get_statistiques()
            print("\n--- STATISTIQUES ---")
            print(f"Nombre total d'employés : {stats['total']}")
            if stats['total'] > 0:
                print(f"Salaire minimum : {stats['min']} €")
                print(f"Salaire maximum : {stats['max']} €")
                print(f"Salaire moyen : {stats['moyenne']:.2f} €")
                print(f"Masse salariale : {stats['masse']} €")
                print("Nombre d'employés par département :")
                for code, nb in stats['par_dept'].items():
                    print(f"  - {code} : {nb} employé(s)")

        elif choix == '8':
            gestion_emp.sauvegarder()
            gestion_dept.sauvegarder()
            print("Données sauvegardées manuellement avec succès.")

        elif choix == '9':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()