class Departement:
    """Classe représentant un département de l'entreprise."""
    
    def __init__(self, code: str, nom: str, description: str = ""):
        self.__code = code
        self.__nom = nom
        self.__description = description

    @property
    def code(self): return self.__code
    @property
    def nom(self): return self.__nom
    @property
    def description(self): return self.__description

    @nom.setter
    def nom(self, v): self.__nom = v
    @description.setter
    def description(self, v): self.__description = v

    def afficher(self) -> str:
        """Méthode polymorphe pour afficher le département."""
        return f"[{self.__code}] {self.__nom} - {self.__description}"