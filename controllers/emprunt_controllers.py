from datetime import date, timedelta

class EmpruntControllers:
    LIMITE_EMPRUNTS = 3

    def __init__(self, db):
        self.db = db

    def enregistrer(self, adherent_id, livre_id, quantite=1, duree=14):
        quantite = int(quantite)
        if quantite <= 0:
            raise ValueError("La quantité doit être positive.")
        adherent = self.db.execute(
            "SELECT * FROM adherents WHERE id=?", (adherent_id,)
        ).fetchone()
        if not adherent or adherent["statut"] != "ACTIF":
            raise ValueError("Adhérent inexistant ou suspendu.")
        nombre = self.db.execute("""
            SELECT COALESCE(SUM(de.quantite),0)
            FROM details_emprunts de JOIN emprunts e ON e.id=de.emprunt_id
            WHERE e.adherent_id=? AND de.date_retour_reelle IS NULL
        """, (adherent_id,)).fetchone()[0]
        if nombre + quantite > self.LIMITE_EMPRUNTS:
            raise ValueError(f"L'adhérent ne peut pas dépasser {self.LIMITE_EMPRUNTS} livres empruntés.")
        livre = self.db.execute("SELECT * FROM livres WHERE id=?", (livre_id,)).fetchone()
        if not livre:
            raise ValueError("Livre introuvable.")
        if livre["quantite_disponible"] < quantite:
            raise ValueError("Quantité disponible insuffisante.")
        aujourd_hui = date.today()
        retour = aujourd_hui + timedelta(days=int(duree))
        cur = self.db.execute("""
            INSERT INTO emprunts(adherent_id,date_emprunt,date_retour_prevue)
            VALUES(?,?,?)
        """, (adherent_id, aujourd_hui.isoformat(), retour.isoformat()))
        emprunt_id = cur.lastrowid
        self.db.execute("""
            INSERT INTO details_emprunts(emprunt_id,livre_id,quantite)
            VALUES(?,?,?)
        """, (emprunt_id, livre_id, quantite))
        self.db.execute("""
            UPDATE livres SET quantite_disponible=quantite_disponible-?
            WHERE id=?
        """, (quantite, livre_id))
        self.db.commit()
        return emprunt_id

    def lister_en_cours(self):
        return self.db.execute("""
            SELECT de.id AS detail_id, e.id AS emprunt_id, a.nom, a.prenom,
                   l.titre, de.quantite, e.date_emprunt, e.date_retour_prevue
            FROM details_emprunts de
            JOIN emprunts e ON e.id=de.emprunt_id
            JOIN adherents a ON a.id=e.adherent_id
            JOIN livres l ON l.id=de.livre_id
            WHERE de.date_retour_reelle IS NULL
            ORDER BY e.date_emprunt
        """).fetchall()
