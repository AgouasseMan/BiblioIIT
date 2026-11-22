from datetime import date

class AdherentControllers:
    def __init__(self, db):
        self.db = db

    def ajouter(self, adherent):
        cur = self.db.execute("""
            INSERT INTO adherents(nom,prenom,telephone,email,date_inscription,statut)
            VALUES(?,?,?,?,?,'ACTIF')
        """, (adherent.nom, adherent.prenom, adherent.telephone,
              adherent.email, date.today().isoformat()))
        self.db.commit()
        return cur.lastrowid

    def lister(self):
        return self.db.execute("SELECT * FROM adherents ORDER BY nom, prenom").fetchall()

    def rechercher(self, terme):
        return self.db.execute("""
            SELECT * FROM adherents
            WHERE nom LIKE ? OR prenom LIKE ? OR telephone LIKE ?
            ORDER BY nom
        """, (f"%{terme}%", f"%{terme}%", f"%{terme}%")).fetchall()

    def changer_statut(self, adherent_id, statut):
        if statut not in ("ACTIF", "SUSPENDU"):
            raise ValueError("Statut invalide.")
        self.db.execute("UPDATE adherents SET statut=? WHERE id=?", (statut, adherent_id))
        self.db.commit()
