from models.penalite import Penalite

class PenaliteControllers:
    def __init__(self, db):
        self.db = db

    def creer(self, detail_id, jours_retard):
        montant = Penalite.calculer(jours_retard)
        if montant > 0:
            self.db.execute("""
                INSERT OR IGNORE INTO penalites(detail_emprunt_id,montant)
                VALUES(?,?)
            """, (detail_id, montant))
        return montant

    def lister(self):
        return self.db.execute("""
            SELECT p.*, a.nom, a.prenom, l.titre
            FROM penalites p
            JOIN details_emprunts de ON de.id=p.detail_emprunt_id
            JOIN emprunts e ON e.id=de.emprunt_id
            JOIN adherents a ON a.id=e.adherent_id
            JOIN livres l ON l.id=de.livre_id
            ORDER BY p.id DESC
        """).fetchall()

    def payer(self, penalite_id):
        cur = self.db.execute("""
            UPDATE penalites SET statut='PAYEE'
            WHERE id=? AND statut='NON PAYEE'
        """, (penalite_id,))
        self.db.commit()
        if cur.rowcount == 0:
            raise ValueError("Pénalité introuvable ou déjà payée.")
