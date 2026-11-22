# BiblioIIT

## Présentation
**BiblioIIT** est une application console de gestion de bibliothèque développée en Python. Elle utilise la programmation orientée objet (POO) et SQLite pour gérer les livres, les adhérents, les emprunts, les retours et les pénalités.

## Objectifs
- Centraliser les informations sur les livres et les adhérents.
- Suivre les emprunts et les retours.
- Contrôler la disponibilité des exemplaires.
- Gérer les retards et les pénalités.
- Organiser le code dans une architecture modulaire.

## Fonctionnalités
- **Livres :** ajout, affichage, recherche, suppression et modification des quantités.
- **Adhérents :** inscription, affichage, recherche, suspension et réactivation.
- **Emprunts :** enregistrement, vérification de la disponibilité et consultation des emprunts en cours.
- **Retours :** enregistrement du retour et mise à jour des quantités disponibles.
- **Pénalités :** calcul, consultation et enregistrement des paiements.
- **Référentiels :** gestion des auteurs et des catégories.
- **Statistiques :** aperçu des livres, exemplaires, adhérents et retards.

## Technologies
- Python 3.10 ou supérieur
- SQLite (`sqlite3`)
- SQL
- Programmation orientée objet
- Git et GitHub

Aucune dépendance externe n'est nécessaire pour la version actuelle.

## Architecture

```text
BiblioIIT/
│
├── main.py
│
├── models/
│   ├── livre.py
│   ├── auteur.py
│   ├── categorie.py
│   ├── adherent.py
│   ├── bibliothecaire.py
│   ├── emprunt.py
│   ├── retour.py
│   └── penalite.py
│
├── controllers/
│   ├── livre_controller.py
│   ├── adherent_controller.py
│   ├── emprunt_controller.py
│   ├── retour_controller.py
│   └── penalite_controller.py
│
├── database/
│   ├── connexion.py
│   └── bibliotheque.db
│
├── views/
│   ├── menu.py
│   ├── livre_view.py
│   ├── adherent_view.py
│   └── emprunt_view.py
│
└── utils/
    └── validations.py
```

**Rôle des composants :**

| Élément | Responsabilité |
|---|---|
| `main.py` | Initialise l'application et lance le menu principal. |
| `models/` | Définit les classes représentant les entités métier. |
| `controllers/` | Reçoit les actions des vues, coordonne les traitements et fait le lien entre vues, modèles et données. |
| `views/` | Affiche les menus, recueille les saisies et présente les résultats. |
| `database/` | Gère la connexion SQLite et le stockage des données. |
| `utils/` | Regroupe les fonctions utilitaires et validations réutilisables. |

## Installation et lancement

1. Installer Python 3.10 ou supérieur.
2. Cloner le dépôt puis ouvrir le dossier du projet :

```bash
git clone URL_DU_DEPOT
cd BiblioIIT
```

3. Lancer l'application :

```bash
python main.py
```

La base SQLite et les tables sont initialisées au démarrage si elles n'existent pas.

## Règles de gestion principales
1. Seul un adhérent actif peut emprunter.
2. Un emprunt est possible uniquement si le livre est disponible en quantité suffisante.
3. Le nombre d'exemplaires empruntés simultanément par un adhérent est limité par l'application.
4. La durée d'emprunt proposée par défaut est de 14 jours.
5. La quantité disponible diminue lors d'un emprunt et augmente lors du retour.
6. Un même détail d'emprunt ne peut pas être retourné deux fois.
7. Une pénalité peut être calculée en fonction du nombre de jours de retard. Le tarif journalier est configurable dans le code.

## Base de données
SQLite stocke notamment les données dans les tables suivantes :
- `auteurs`
- `categories`
- `livres`
- `adherents`
- `bibliothecaires`
- `emprunts`
- `details_emprunts`
- `penalites`

Le fichier de base de données est créé localement par l'application.

## Scénario de test conseillé
1. Ajouter un auteur et une catégorie.
2. Ajouter un livre.
3. Inscrire un adhérent.
4. Enregistrer un emprunt.
5. Consulter les emprunts en cours.
6. Enregistrer le retour du livre.
7. Consulter les pénalités éventuelles et enregistrer un paiement.

## Gestion de versions avec Git

```bash
git init
git add .
git commit -m "Initialisation de BiblioIIT"
```

Le fichier `.gitignore` doit exclure les fichiers temporaires Python, les environnements virtuels et, si elle reste locale, la base SQLite.



