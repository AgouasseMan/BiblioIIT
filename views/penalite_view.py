from controllers.penalite_controllers import PenaliteControllers

def menu_penalites(db):
    service = PenaliteControllers(db)
    while True:
        print("\\n--- GESTION DES PÉNALITÉS ---")
        print("1. Lister  2. Enregistrer un paiement  0. Retour")
        choix = input("Choix : ").strip()
        try:
            if choix == "1":
                penalites = service.lister()
                if not penalites:
                    print("Aucune pénalité.")
                for p in penalites:
                    print(f'ID {p["id"]} | {p["prenom"]} {p["nom"]} | {p["titre"]} | '
                          f'{p["montant"]:.0f} FCFA | {p["statut"]}')
            elif choix == "2":
                service.payer(int(input("ID de la pénalité : ")))
                print("Paiement enregistré.")
            elif choix == "0":
                break
            else:
                print("Choix invalide.")
        except (ValueError, TypeError) as erreur:
            print(f"Erreur : {erreur}")
