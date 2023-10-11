from .domino import *
import random
from collections import deque

class JeuDomino:
    def __init__(self, max : int):
        """Constructeur de la classe jeu domino

        Args:
            max (int): Valeur max d'un domino
        """

        self.max = max
        self.pioche = deque()
        self.selected = None
        self.gauche = 0
        self.droite = 0


    def nouveauJeu(self):
        """Nettoie les informations des anciens jeu (si il y'en a un) et prépare un nouveau jeu
        """

        # Nettoyage du jeu de domino
        self.pioche.clear()
        
        # Remplissage du jeu
        for i in range(self.max):
            for j in range(i+1):
                self.pioche.append(Domino(i, j))

        '''
        # Affichage du jeu de domino
        for i in range(len(self.pioche)):
            print(self.pioche[i].gauche, self.pioche[i].droite)
        '''

        random.shuffle(self.pioche) # Mélange des cartes

        # Choix au hasard du premier domino
        self.selected = self.pioche.popleft()
        self.gauche = self.selected.gauche
        self.droite = self.selected.droite
        
    def boucleJeu(self):
            game = True
            taille = len(self.pioche)
            tour = 0
            while (game):
                self.selected = self.pioche.popleft()

                # Affichage test
                print(f"\n|{self.gauche}|..|?|..|{self.droite}|")
                print(f"\n\t\t|{self.selected.gauche}|{self.selected.droite}| {tour}/{taille}")
                print("\n----------------------------------------------------------------------")

                if (tour < taille):
                    # Test si on peut le mettre dans les extrémités
                    if (self.selected.gauche == self.gauche):
                        self.gauche = self.selected.droite
                        tour = 0 
                    elif (self.selected.gauche == self.droite):
                        self.droite = self.selected.droite
                        tour = 0
                    elif (self.selected.droite == self.gauche):
                        self.gauche = self.selected.gauche
                        tour = 0
                    elif (self.selected.droite == self.droite):
                        self.droite = self.selected.gauche
                        tour = 0

                    else:
                        self.pioche.append(self.selected)
                        tour+=1
                else :
                    game = False
                     