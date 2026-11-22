from controllers.emprunt_controllers import EmpruntControllers
from controllers.retour_controllers import RetourControllers

def menu_emprunts(db):
    emprunts = EmpruntControllers(db)
    retours = RetourControllers(db)
    while True:
        print("\\n--- EMPRUNTS ET RETOURS ---")
        print("1. Enregistrer un emprunt  2. Voir les emprunts en cours")
        print("3. Enregistrer un retour  0. Retour")
        choix = input("Choix : ").strip()
        try:
            if choix == "1":
                adherent_id = int(input("ID adhérent : "))
                livre_id = int(input("ID livre : "))
                quantite = int(input("Quantité (défaut 1) : ") or "1")
                duree = int(input("Durée en jours (défaut 14) : ") or "14")
                identifiant = emprunts.enregistrer(adherent_id, livre_id, quantite, duree)
                print(f"Emprunt enregistré. Numéro : {identifiant}")
            elif choix == "2":
                lignes = emprunts.lister_en_cours()
                if not lignes:
                    print("Aucun emprunt en cours.")
                for e in lignes:
                    print(f'Emprunt {e["emprunt_id"]} / détail {e["detail_id"]} : '
                          f'{e["prenom"]} {e["nom"]} - {e["titre"]} x{e["quantite"]} '
                          f'| retour prévu : {e["date_retour_prevue"]}')
            elif choix == "3":
                detail_id = int(input("ID du détail d'emprunt à retourner : "))
                montant = retours.enregistrer(detail_id)
                print("Retour enregistré.")
                if montant:
                    print(f"Retard : pénalité de {montant:.0f} FCFA à régler.")
                else:
                    print("Aucune pénalité.")
            elif choix == "0":
                break
            else:
                print("Choix invalide.")
        except (ValueError, TypeError) as erreur:
            print(f"Erreur : {erreur}")
