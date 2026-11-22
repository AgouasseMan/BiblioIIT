from datetime import datetime

def texte_obligatoire(valeur, nom_champ):
    valeur = str(valeur).strip()
    if not valeur:
        raise ValueError(f"Le champ {nom_champ} est obligatoire.")
    return valeur

def entier_positif(valeur, nom_champ="valeur"):
    try:
        nombre = int(valeur)
    except (TypeError, ValueError):
        raise ValueError(f"{nom_champ} doit être un nombre entier.")
    if nombre <= 0:
        raise ValueError(f"{nom_champ} doit être supérieur à zéro.")
    return nombre

def date_valide(valeur):
    try:
        datetime.strptime(valeur, "%Y-%m-%d")
        return True
    except ValueError:
        return False
