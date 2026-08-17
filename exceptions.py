class SalaireNegatifError(Exception):
    def __init__(self, message="Erreur : Le salaire ne peut pas être négatif."):
        self.message = message
        super().__init__(self.message)

class AgeInvalideError(Exception):
    def __init__(self, message="Erreur : L'âge doit être un entier positif supérieur à 0."):
        self.message = message
        super().__init__(self.message)

class MatriculeInexistantError(Exception):
    def __init__(self, message="Erreur : Aucun employé trouvé avec ce matricule."):
        self.message = message
        super().__init__(self.message)