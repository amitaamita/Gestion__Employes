import json
import os

class Utils:
    """Classe utilitaire pour la manipulation des fichiers JSON."""

    @staticmethod
    def charger_donnees(nom_fichier: str) -> dict:
        """Charge les données depuis un fichier JSON avec gestion des erreurs."""
        donnees = {}
        try:
            if os.path.exists(nom_fichier):
                with open(nom_fichier, "r", encoding="utf-8") as f:
                    donnees = json.load(f)
        except json.JSONDecodeError:
            print(f"Erreur : Le fichier {nom_fichier} est corrompu.")
        except Exception as e:
            print(f"Erreur de lecture du fichier {nom_fichier} : {e}")
        finally:
            # Le bloc finally s'exécute toujours (demandé par le prof)
            pass
        return donnees

    @staticmethod
    def sauvegarder_donnees(nom_fichier: str, donnees: dict) -> bool:
        """Sauvegarde des données dans un fichier JSON avec gestion des erreurs."""
        succes = True
        try:
            with open(nom_fichier, "w", encoding="utf-8") as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur d'écriture dans le fichier {nom_fichier} : {e}")
            succes = False
        finally:
            pass
        return succes