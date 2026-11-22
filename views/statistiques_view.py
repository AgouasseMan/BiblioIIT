def afficher_statistiques(db):
    livres = db.execute("SELECT COUNT(*) FROM livres").fetchone()[0]
    exemplaires = db.execute("SELECT COALESCE(SUM(quantite_totale),0) FROM livres").fetchone()[0]
    disponibles = db.execute("SELECT COALESCE(SUM(quantite_disponible),0) FROM livres").fetchone()[0]
    adherents = db.execute("SELECT COUNT(*) FROM adherents").fetchone()[0]
    emprunts = db.execute("SELECT COUNT(*) FROM emprunts WHERE statut='EN COURS'").fetchone()[0]
    retards = db.execute("""
        SELECT COUNT(*) FROM details_emprunts de
        JOIN emprunts e ON e.id=de.emprunt_id
        WHERE de.date_retour_reelle IS NULL AND e.date_retour_prevue < date('now')
    """).fetchone()[0]
    print("\\n--- STATISTIQUES ---")
    print(f"Titres enregistrés : {livres}")
    print(f"Exemplaires : {exemplaires} (disponibles : {disponibles})")
    print(f"Adhérents : {adherents}")
    print(f"Emprunts avec retour en attente : {emprunts}")
    print(f"Emprunts en retard : {retards}")
