class Departement:
    def __init__(self, code: str, nom: str):
        self.code = code
        self.nom = nom

    def afficher(self) -> str:
        return f"[{self.code}] - {self.nom}"