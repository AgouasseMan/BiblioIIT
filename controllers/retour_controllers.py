from datetime import date, datetime
from controllers.penalite_controllers import PenaliteControllers

class RetourControllers:
    def __init__(self, db):
        self.db = db
        self.penalites = PenaliteControllers(db)

    def enregistrer(self, detail_id):
        detail = self.db.execute("""
            SELECT de.*, e.date_retour_prevue
            FROM details_emprunts de
            JOIN emprunts e ON e.id=de.emprunt_id
            WHERE de.id=?
        """, (detail_id,)).fetchone()
        if not detail:
            raise ValueError("Emprunt introuvable.")
        if detail["date_retour_reelle"]:
            raise ValueError("Ce livre a déjà été retourné.")
        aujourd_hui = date.today()
        self.db.execute(
            "UPDATE details_emprunts SET date_retour_reelle=? WHERE id=?",
            (aujourd_hui.isoformat(), detail_id)
        )
        self.db.execute("""
            UPDATE livres SET quantite_disponible=quantite_disponible+?
            WHERE id=(SELECT livre_id FROM details_emprunts WHERE id=?)
        """, (detail["quantite"], detail_id))
        retard = (aujourd_hui - date.fromisoformat(detail["date_retour_prevue"])).days
        montant = self.penalites.creer(detail_id, retard)
        restant = self.db.execute("""
            SELECT COUNT(*) FROM details_emprunts
            WHERE emprunt_id=(SELECT emprunt_id FROM details_emprunts WHERE id=?)
              AND date_retour_reelle IS NULL
        """, (detail_id,)).fetchone()[0]
        if restant == 0:
            self.db.execute("""
                UPDATE emprunts SET statut='TERMINE'
                WHERE id=(SELECT emprunt_id FROM details_emprunts WHERE id=?)
            """, (detail_id,))
        self.db.commit()
        return montant
