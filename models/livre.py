class Livre:
    def __init__(self, titre, quantite, isbn=None, auteur_id=None,
                 categorie_id=None, editeur=None, annee=None):
        self.titre = titre.strip()
        self.quantite = int(quantite)
        self.isbn = isbn or None
        self.auteur_id = auteur_id or None
        self.categorie_id = categorie_id or None
        self.editeur = editeur or None
        self.annee = annee or None
