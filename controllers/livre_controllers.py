class LivreControllers:
    def __init__(self, db):
        self.db = db

    def ajouter(self, livre):
        cur = self.db.execute("""
            INSERT INTO livres(isbn,titre,auteur_id,categorie_id,editeur,annee,
                               quantite_totale,quantite_disponible)
            VALUES(?,?,?,?,?,?,?,?)
        """, (livre.isbn, livre.titre, livre.auteur_id, livre.categorie_id,
              livre.editeur, livre.annee, livre.quantite, livre.quantite))
        self.db.commit()
        return cur.lastrowid

    def lister(self):
        return self.db.execute("""
            SELECT l.*, a.nom AS auteur, c.nom AS categorie
            FROM livres l
            LEFT JOIN auteurs a ON a.id=l.auteur_id
            LEFT JOIN categories c ON c.id=l.categorie_id
            ORDER BY l.titre
        """).fetchall()

    def rechercher(self, terme):
        return self.db.execute("""
            SELECT l.*, a.nom AS auteur, c.nom AS categorie
            FROM livres l
            LEFT JOIN auteurs a ON a.id=l.auteur_id
            LEFT JOIN categories c ON c.id=l.categorie_id
            WHERE l.titre LIKE ? OR l.isbn LIKE ? OR a.nom LIKE ?
            ORDER BY l.titre
        """, (f"%{terme}%", f"%{terme}%", f"%{terme}%")).fetchall()

    def supprimer(self, livre_id):
        en_cours = self.db.execute("""
            SELECT COUNT(*) FROM details_emprunts
            WHERE livre_id=? AND date_retour_reelle IS NULL
        """, (livre_id,)).fetchone()[0]
        if en_cours:
            raise ValueError("Impossible : ce livre fait l'objet d'un emprunt en cours.")
        self.db.execute("DELETE FROM livres WHERE id=?", (livre_id,))
        self.db.commit()

    def modifier_quantite(self, livre_id, nouvelle_quantite):
        livre = self.db.execute("SELECT * FROM livres WHERE id=?", (livre_id,)).fetchone()
        if not livre:
            raise ValueError("Livre introuvable.")
        empruntes = livre["quantite_totale"] - livre["quantite_disponible"]
        if nouvelle_quantite < empruntes:
            raise ValueError("La quantité totale ne peut pas être inférieure aux exemplaires empruntés.")
        self.db.execute("""
            UPDATE livres SET quantite_totale=?, quantite_disponible=?
            WHERE id=?
        """, (nouvelle_quantite, nouvelle_quantite-empruntes, livre_id))
        self.db.commit()
