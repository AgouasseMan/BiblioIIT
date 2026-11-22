from database.connexion import creer_connexion, initialiser_base
from views.menu import lancer_menu

def main():
    connexion = creer_connexion()
    initialiser_base(connexion)
    try:
        lancer_menu(connexion)
    finally:
        connexion.close()

if __name__ == "__main__":
    main()
