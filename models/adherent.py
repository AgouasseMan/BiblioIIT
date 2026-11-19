class Adherent:
    def __init__(self, nom, prenom, telephone="", email=""):
        self.nom = nom.strip()
        self.prenom = prenom.strip()
        self.telephone = telephone.strip()
        self.email = email.strip()