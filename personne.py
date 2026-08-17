class Personne:
    """Classe mère représentant une personne générique."""
    
    def __init__(self, nom: str, prenom: str, age: int, sexe: str, adresse: str, tel: str):
        """Initialise une personne avec des attributs privés."""
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__sexe = sexe
        self.__adresse = adresse
        self.__tel = tel

    # --- GETTERS ET SETTERS (Encapsulation) ---
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, valeur: str):
        self.__nom = valeur

    @property
    def prenom(self) -> str:
        return self.__prenom

    @prenom.setter
    def prenom(self, valeur: str):
        self.__prenom = valeur

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, valeur: int):
        self.__age = valeur

    @property
    def sexe(self) -> str:
        return self.__sexe

    @sexe.setter
    def sexe(self, valeur: str):
        self.__sexe = valeur

    @property
    def adresse(self) -> str:
        return self.__adresse

    @adresse.setter
    def adresse(self, valeur: str):
        self.__adresse = valeur

    @property
    def tel(self) -> str:
        return self.__tel

    @tel.setter
    def tel(self, valeur: str):
        self.__tel = valeur

    def afficher(self) -> str:
        """Méthode polymorphe pour afficher les infos de base."""
        return f"{self.__nom} {self.__prenom} - Âge: {self.__age} | Sexe: {self.__sexe} | Tel: {self.__tel}"