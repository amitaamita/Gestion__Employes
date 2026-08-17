import json
from departement import Departement

class GestionDepartements:
    def __init__(self, gestion_emp):
        self.departements = {}  # Dictionnaire {code: objet Departement}
        self.gestion_emp = gestion_emp  # Au cas où tu veux vérifier si un dept a des employés avant de le supprimer

    def afficher_sous_menu(self):
        while True:
            print("\n--- GESTION DES DÉPARTEMENTS ---")
            print("1. Ajouter un département")
            print("2. Supprimer un département")
            print("3. Afficher tous les départements")
            print("4. Retour au menu principal")
            
            choix = input("Votre choix : ")

            if choix == '1':
                code = input("Code du département (ex: INFO) : ")
                if code in self.departements:
                    print("Erreur : Ce code de département existe déjà.")
                    continue
                nom = input("Nom du département (ex: Informatique) : ")
                self.departements[code] = Departement(code, nom)
                print(f"Département '{nom}' ajouté avec succès !")

            elif choix == '2':
                code = input("Code du département à supprimer : ")
                if code in self.departements:
                    del self.departements[code]
                    print("Département supprimé avec succès !")
                else:
                    print("Erreur : Département introuvable.")

            elif choix == '3':
                if not self.departements:
                    print("Aucun département enregistré.")
                else:
                    print("\nListe des départements :")
                    for dept in self.departements.values():
                        print(dept.afficher())

            elif choix == '4':
                print("Retour au menu principal...")
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    def sauvegarder(self):
        # On transforme les objets en dictionnaires simples pour le fichier JSON
        data = {code: {"nom": dept.nom} for code, dept in self.departements.items()}
        try:
            # encoding='utf-8' et ensure_ascii=False sont ajoutés pour ne pas avoir de problèmes avec les accents (é, è, etc.)
            with open("departements.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Une erreur est survenue lors de la sauvegarde des départements : {e}")