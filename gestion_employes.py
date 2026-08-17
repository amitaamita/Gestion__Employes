from employe import Employe
from exceptions import MatriculeInexistantError, SalaireNegatifError
import json
import os

class GestionEmployes:
    def __init__(self):
        self.employes = {}  # Dictionnaire {matricule: objet Employe}
        # Optionnel mais bien : charger les données ici si le fichier existe

    def ajouter_employe(self, emp: Employe):
        self.employes[emp.matricule] = emp

    def modifier_employe(self, mat: str, nouvelles_donnees: dict):
        if mat not in self.employes:
            raise MatriculeInexistantError()
            
        emp = self.employes[mat]
        for cle, valeur in nouvelles_donnees.items():
            # Le main.py envoie "telephone" mais l'attribut est "tel", il faut gérer ça !
            if cle == "telephone":
                emp.tel = valeur
            elif hasattr(emp, cle):
                # Vérification du salaire si on le modifie (car le main.py catch SalaireNegatifError ici)
                if cle == "salaire" and valeur is not None and valeur < 0:
                    raise SalaireNegatifError()
                setattr(emp, cle, valeur)

    def supprimer_employe(self, mat: str):
        if mat not in self.employes:
            raise MatriculeInexistantError()
        del self.employes[mat]

    def rechercher_employe(self, mat: str) -> Employe:
        if mat not in self.employes:
            raise MatriculeInexistantError()
        return self.employes[mat]

    def afficher_tous(self):
        if not self.employes:
            print("Aucun employé enregistré.")
            return
        for emp in self.employes.values():
            print(emp.afficher())
            print("-" * 30)

    def get_statistiques(self) -> dict:
        total = len(self.employes)
        # Le main.py fait un "if stats['total'] > 0:" avant d'afficher le reste, 
        # donc on peut mettre des valeurs par défaut à 0 pour éviter les erreurs de division par zéro.
        stats = {
            'total': total,
            'min': 0,
            'max': 0,
            'moyenne': 0.0,
            'masse': 0.0,
            'par_dept': {}
        }

        if total > 0:
            salaires = [emp.salaire for emp in self.employes.values()]
            stats['min'] = min(salaires)
            stats['max'] = max(salaires)
            stats['masse'] = sum(salaires)
            stats['moyenne'] = stats['masse'] / total

            # Compter par département
            for emp in self.employes.values():
                code = emp.code_dept
                stats['par_dept'][code] = stats['par_dept'].get(code, 0) + 1

        return stats  # DOIT OBLIGATOIRERET RETOURNER UN DICT AVEC CES CLES EXACTES

    def sauvegarder(self):
        data = {}
        for mat, emp in self.employes.items():
            data[mat] = {
                "nom": emp.nom, "prenom": emp.prenom, "age": emp.age,
                "sexe": emp.sexe, "adresse": emp.adresse, "tel": emp.tel,
                "poste": emp.poste, "salaire": emp.salaire, "code_dept": emp.code_dept
            }
        with open("employes.json", "w") as f:
            json.dump(data, f, indent=4)