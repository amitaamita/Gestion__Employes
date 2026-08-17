class SalaireNegatifError(Exception):
    """Exception levée si un salaire négatif est fourni."""
    def __init__(self, message="Erreur : Le salaire ne peut pas être négatif."):
        self.message = message
        super().__init__(self.message)

class AgeInvalideError(Exception):
    """Exception levée si l'âge est invalide."""
    def __init__(self, message="Erreur : L'âge doit être un entier positif."):
        self.message = message
        super().__init__(self.message)

class MatriculeInexistantError(Exception):
    """Exception levée si le matricule n'existe pas."""
    def __init__(self, message="Erreur : Aucun employé trouvé avec ce matricule."):
        self.message = message
        super().__init__(self.message)

class DepartementIntrouvableError(Exception):
    """Exception levée si le département n'existe pas."""
    def __init__(self, message="Erreur : Le département demandé est introuvable."):
        self.message = message
        super().__init__(self.message)