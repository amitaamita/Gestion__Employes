from exceptions import SalaireNegatifError, AgeInvalideError

class Employe:
    def __init__(self, mat, nom, prenom, age, sexe, adresse, tel, poste, salaire, code_dept):
        self.matricule = mat
        self.nom = nom
        self.prenom = prenom
        
        # Validations requises par le main.py
        if age <= 0:
            raise AgeInvalideError()
        self.age = age
            
        self.sexe = sexe
        self.adresse = adresse
        self.tel = tel
        self.poste = poste
        
        if salaire < 0:
            raise SalaireNegatifError()
        self.salaire = salaire
            
        self.code_dept = code_dept

    def afficher(self) -> str:
        # ATTENTION : doit utiliser return et non print pour que le main.py puisse faire print(emp.afficher())
        return (f"Matricule : {self.matricule}\n"
                f"Nom : {self.nom} {self.prenom}\n"
                f"Âge : {self.age} | Sexe : {self.sexe}\n"
                f"Adresse : {self.adresse} | Tel : {self.tel}\n"
                f"Poste : {self.poste} | Salaire : {self.salaire} €\n"
                f"Département : {self.code_dept}")