from departement import Departement

class GestionDepartements:
    def __init__(self, gestion_emp):
        self.departements = {}  # Dictionnaire {code: objet Departement}
        self.gestion_emp = gestion_emp  # Utile si tu veux vérifier si des employés sont dans un dept avant de le supprimer

    def afficher_sous_menu(self):
        # C'EST ICI QUE TU CRÉES UN WHILE TRUE avec un menu (1. Ajouter dept, 2. Supprimer, 3. Afficher, 4. Retour)
        # Exemple :
        while True:
            print("\n--- GESTION DES DÉPARTEMENTS ---")
            print("1. Ajouter un département")
            print("2. Supprimer un département")
            print("3. Afficher tous les départements")
            print("4. Retour au menu principal")
            choix = input("Choix : ")

            if choix == '1':
                code = input("Code du département : ")
                nom = input("Nom du département : ")
                self.departements[code] = Departement(code, nom)
                print("Département ajouté !")
            elif choix == '2':
                code = input("Code du département à supprimer : ")
                if code in self.departements:
                    del self.departements[code]
                    print("Département supprimé !")
                else:
                    print("Département introuvable.")
            elif choix == '3':
                if not self.departements:
                    print("Aucun département.")
                for dept in self.departements.values():
                    print(dept.afficher())
            elif choix == '4':
                break

    def sauvegarder(self):
        import json
        # Transformer les objets en dictionnaires pour le JSON
        data = {code: {"nom": dept.nom} for code, dept in self.departements.items()}
        with open("departements.json", "w") as f:
            json.dump(data, f, indent=4)