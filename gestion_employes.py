from employe import Employe
from utils import Utils
from exceptions import MatriculeInexistantError, SalaireNegatifError

class GestionEmployes:
    """Classe permettant de gérer l'ensemble des opérations liées aux employés."""

    def __init__(self):
        """Initialise le gestionnaire et charge automatiquement les données."""
        self.__employes = {}  # Dictionnaire {matricule: objet Employe}
        self.__charger_donnees()

    def __charger_donnees(self):
        """Charge les employés depuis le fichier JSON au démarrage."""
        donnees_json = Utils.charger_donnees("employes.json")
        for matricule, info in donnees_json.items():
            # Utilisation des getters (propriétés) si besoin, mais ici on passe au constructeur
            try:
                emp = Employe(
                    matricule=matricule,
                    nom=info.get("nom", ""),
                    prenom=info.get("prenom", ""),
                    age=info.get("age", 0),
                    sexe=info.get("sexe", ""),
                    adresse=info.get("adresse", ""),
                    tel=info.get("tel", ""),
                    poste=info.get("poste", ""),
                    salaire=info.get("salaire", 0.0),
                    code_dept=info.get("code_dept", "")
                )
                self.__employes[matricule] = emp
            except Exception as e:
                print(f"Erreur lors du chargement de l'employé {matricule} : {e}")

    def ajouter_employe(self, emp: Employe):
        """Ajoute un nouvel employé au dictionnaire."""
        self.__employes[emp.matricule] = emp

    def modifier_employe(self, mat: str, nouvelles_donnees: dict):
        """Modifie les informations d'un employé existant."""
        if mat not in self.__employes:
            raise MatriculeInexistantError()
            
        emp = self.__employes[mat]
        for cle, valeur in nouvelles_donnees.items():
            if cle == "telephone":
                emp.tel = valeur  # Utilisation du setter
            elif hasattr(emp, cle):
                if cle == "salaire" and valeur is not None:
                    if valeur < 0:
                        raise SalaireNegatifError()
                    emp.salaire = valeur  # Utilisation du setter
                elif valeur != "":
                    setattr(emp, cle, valeur) # Utilise les setters automatiquement

    def supprimer_employe(self, mat: str):
        """Supprime un employé du système."""
        if mat not in self.__employes:
            raise MatriculeInexistantError()
        del self.__employes[mat]

    def rechercher_employe(self, mat: str) -> Employe:
        """Recherche et retourne un employé par son matricule."""
        if mat not in self.__employes:
            raise MatriculeInexistantError()
        return self.__employes[mat]

    def afficher_tous(self):
        """Affiche la liste complète de tous les employés."""
        if not self.__employes:
            print("Aucun employé enregistré.")
            return
        for emp in self.__employes.values():
            print(emp.afficher())  # Polymorphisme
            print("-" * 30)

    def get_statistiques(self) -> dict:
        """Calcule et retourne les statistiques sur les employés sous forme de dictionnaire."""
        total = len(self.__employes)
        stats = {
            'total': total,
            'min': 0,
            'max': 0,
            'moyenne': 0.0,
            'masse': 0.0,
            'par_dept': {}
        }

        if total > 0:
            # On utilise le getter emp.salaire (pas __salaire)
            salaires = [emp.salaire for emp in self.__employes.values()]
            stats['min'] = min(salaires)
            stats['max'] = max(salaires)
            stats['masse'] = sum(salaires)
            stats['moyenne'] = stats['masse'] / total

            # On utilise le getter emp.code_dept
            for emp in self.__employes.values():
                code = emp.code_dept
                stats['par_dept'][code] = stats['par_dept'].get(code, 0) + 1

        return stats

    def sauvegarder(self):
        """Sauvegarde tous les employés dans le fichier JSON en utilisant Utils."""
        data = {}
        for mat, emp in self.__employes.items():
            # On utilise obligatoirement les GETTERS (propriétés publiques) pour sérialiser
            data[mat] = {
                "nom": emp.nom,
                "prenom": emp.prenom,
                "age": emp.age,
                "sexe": emp.sexe,
                "adresse": emp.adresse,
                "tel": emp.tel,
                "poste": emp.poste,
                "salaire": emp.salaire,
                "code_dept": emp.code_dept
            }
        
        # Utilisation du fichier utils.py avec try/except/finally
        Utils.sauvegarder_donnees("employes.json", data)