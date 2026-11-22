def afficher_livres(livres):
    if not livres:
        print("Aucun livre trouvé.")
        return
    print("\nID | TITRE | AUTEUR | CATÉGORIE | DISPONIBLE/TOTAL")
    print("-" * 78)
    for l in livres:
        print(f'{l["id"]} | {l["titre"]} | {l["auteur"] or "-"} | '
              f'{l["categorie"] or "-"} | {l["quantite_disponible"]}/{l["quantite_totale"]}')

def afficher_adherents(adherents):
    if not adherents:
        print("Aucun adhérent trouvé.")
        return
    print("\nID | NOM | PRÉNOM | TÉLÉPHONE | STATUT")
    print("-" * 65)
    for a in adherents:
        print(f'{a["id"]} | {a["nom"]} | {a["prenom"]} | {a["telephone"] or "-"} | {a["statut"]}')
