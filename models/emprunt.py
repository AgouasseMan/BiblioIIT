from datetime import date, timedelta

class Emprunt:
    def __init__(self, adherent_id, duree_jours=14):
        self.adherent_id = int(adherent_id)
        self.duree_emprunt = date.today()
        self.date_retour_prevue = self.date_emprunt + timedelta(days=int(duree_jours))
                                                                