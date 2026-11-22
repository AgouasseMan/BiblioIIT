def menu_referentiels(db):
    while True:
        print("\\n--- AUTEURS ET CATÉGORIES ---")
        print("1. Ajouter un auteur  2. Lister les auteurs")
        print("3. Ajouter une catégorie  4. Lister les catégories  0. Retour")
        choix = input("Choix : ").strip()
        if choix == "1":
            nom = input("Nom de l'auteur : ").strip()
            if nom:
                db.execute("INSERT INTO auteurs(nom) VALUES(?)", (nom,))
                db.commit()
                print("Auteur ajouté.")
        elif choix == "2":
            for r in db.execute("SELECT * FROM auteurs ORDER BY nom"):
                print(f'{r["id"]} - {r["nom"]}')
        elif choix == "3":
            nom = input("Nom de la catégorie : ").strip()
            if nom:
                try:
                    db.execute("INSERT INTO categories(nom) VALUES(?)", (nom,))
                    db.commit()
                    print("Catégorie ajoutée.")
                except Exception as e:
                    print(f"Impossible d'ajouter : {e}")
        elif choix == "4":
            for r in db.execute("SELECT * FROM categories ORDER BY nom"):
                print(f'{r["id"]} - {r["nom"]}')
        elif choix == "0":
            break
        else:
            print("Choix invalide.")
