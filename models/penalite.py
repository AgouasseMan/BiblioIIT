class Penalite:
    TARIF_PAR_JOUR = 100  # FCFA

    @classmethod
    def calculer(cls, jours_retard):
        return max(0, int(jours_retard)) * cls.TARIF_PAR_JOUR
