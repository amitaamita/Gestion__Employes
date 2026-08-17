from personne import Personne
from exceptions import SalaireNegatifError, AgeInvalideError

class Employe(Personne):
    """Classe Employe qui hérite de Personne."""
    
    def __init__(self, matricule: str, nom: str, prenom: str, age: int, sexe: str, adresse: str, tel: str, poste: str, salaire: float, code_dept: str):
        # Appel du constructeur de la classe mère (Personne)
        super().__init__(nom, prenom, age, sexe, adresse, tel)
        
        self.__matricule = matricule
        self.__poste = poste
        self.__code_dept = code_dept
        
        if salaire < 0:
            raise SalaireNegatifError()
        self.__salaire = salaire

    # Getters et Setters pour Employe
    @property
    def matricule(self): return self.__matricule

    @property
    def poste(self): return self.__poste
    @poste.setter
    def poste(self, v): self.__poste = v

    @property
    def salaire(self): return self.__salaire
    @salaire.setter
    def salaire(self, v):
        if v < 0:
            raise SalaireNegatifError()
        self.__salaire = v

    @property
    def code_dept(self): return self.__code_dept
    @code_dept.setter
    def code_dept(self, v): self.__code_dept = v

    def afficher(self) -> str:
        """Redéfinition de la méthode afficher (Polymorphisme)."""
        info_base = super().afficher()
        return f"{info_base}\nPoste: {self.__poste} | Salaire: {self.__salaire} € | Dept: {self.__code_dept}"