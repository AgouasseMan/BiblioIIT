from datetime import date

class Retour:
    def __init__(self, detail_emprunt_id):
        self.detail_emprunt_id = int(detail_emprunt_id)
        self.date_retour = date.today()

