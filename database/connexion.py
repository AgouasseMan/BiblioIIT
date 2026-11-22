import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "bibliotheque.db"

def creer_connexion():
    connexion = sqlite3.connect(DATABASE_PATH)
    connexion.row_factory = sqlite3.Row
    connexion.execute("PRAGMA foreign_keys = ON")
    return connexion

def initialiser_base(connexion):
    connexion.executescript("""
    CREATE TABLE IF NOT EXISTS auteurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS livres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn TEXT UNIQUE,
        titre TEXT NOT NULL,
        auteur_id INTEGER,
        categorie_id INTEGER,
        editeur TEXT,
        annee INTEGER,
        quantite_totale INTEGER NOT NULL CHECK(quantite_totale >= 0),
        quantite_disponible INTEGER NOT NULL CHECK(
            quantite_disponible >= 0 AND quantite_disponible <= quantite_totale
        ),
        FOREIGN KEY(auteur_id) REFERENCES auteurs(id) ON DELETE SET NULL,
        FOREIGN KEY(categorie_id) REFERENCES categories(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS adherents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        telephone TEXT,
        email TEXT,
        date_inscription TEXT NOT NULL,
        statut TEXT NOT NULL DEFAULT 'ACTIF'
    );

    CREATE TABLE IF NOT EXISTS bibliothecaires (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        identifiant TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS emprunts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        adherent_id INTEGER NOT NULL,
        date_emprunt TEXT NOT NULL,
        date_retour_prevue TEXT NOT NULL,
        statut TEXT NOT NULL DEFAULT 'EN COURS',
        FOREIGN KEY(adherent_id) REFERENCES adherents(id)
    );

    CREATE TABLE IF NOT EXISTS details_emprunts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emprunt_id INTEGER NOT NULL,
        livre_id INTEGER NOT NULL,
        quantite INTEGER NOT NULL CHECK(quantite > 0),
        date_retour_reelle TEXT,
        FOREIGN KEY(emprunt_id) REFERENCES emprunts(id),
        FOREIGN KEY(livre_id) REFERENCES livres(id)
    );

    CREATE TABLE IF NOT EXISTS penalites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        detail_emprunt_id INTEGER NOT NULL UNIQUE,
        montant REAL NOT NULL,
        statut TEXT NOT NULL DEFAULT 'NON PAYEE',
        FOREIGN KEY(detail_emprunt_id) REFERENCES details_emprunts(id)
    );
    """)
    connexion.commit()
