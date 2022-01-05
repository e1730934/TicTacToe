import numpy as np


class Player:
    """Classe représentant un joueur"""

    def __init__(self, name, char):
        self.name = name
        self.char = char[0]
        self.n_wins = 0

    def __str__(self):
        """Retourne une chaîne de caractères représentant un joueur. Elle devrait au minimum contenir le nom du
            joueur"""
        nl = '\n'
        return f"Joueur: {self.name} ({self.char}){nl}Nombre de victoire:{self.n_wins}"


class Board:
    """Classe représentant une grille de jeu"""

    def __init__(self):
        """Initialisation de la grille de format 3 par 3"""
        self.tailleGrille = 3
        self.grille = np.full((self.tailleGrille, self.tailleGrille), '_')

    def clear_board(self):
        """Remet la grille à 0 dans le but de démarrer une nouvelle partie en réutilisant la grille existante,
        sans recréer complètement une nouvelle grille (sans recréer un nouvel objet de type Board)"""
        for i in range(self.tailleGrille):
            for j in range(self.tailleGrille):
                self.grille[i, j] = '_'

    def get(self, x, y):
        """Retourne le caractère à la position (x, y). Devrait retourner "_", "X" ou "O" """
        if self.grille[x, y] == 'X':
            return 'X'
        elif self.grille[x, y] == 'O':
            return 'O'
        else:
            return '_'

    def set(self, x, y, char):
        """Place le caractère à la position (x, y)"""
        self.grille[x, y] = char

    def get_winner(self):
        """Retourne le gagnant "X" ou "O", s'il y en a un. Si aucun gagnant, retourne None """

        compteurLigneX = 0
        compteurLigneO = 0
        compteurColonneX = 0
        compteurColonneO = 0
        compteurDiagonalX = 0
        compteurDiagonalO = 0
        compteurAntiDiagonalX = 0
        compteurAntiDiagonalO = 0

        for i in range(self.tailleGrille):
            for j in range(self.tailleGrille):
                if self.grille[i, j] == 'X':
                    compteurLigneX += 1
                elif self.grille[i, j] == 'O':
                    compteurLigneO += 1
                if self.grille[j, i] == 'X':
                    compteurColonneX += 1
                elif self.grille[j, i] == 'O':
                    compteurColonneO += 1
                if self.grille[i, i] == 'X':
                    compteurDiagonalX += 1
                elif self.grille[i, i] == 'O':
                    compteurDiagonalO += 1
                if self.grille[i, self.tailleGrille - i - 1] == 'X':
                    compteurAntiDiagonalX += 1
                elif self.grille[i, self.tailleGrille - i - 1] == 'O':
                    compteurAntiDiagonalO += 1

            if (compteurLigneX == self.tailleGrille) or (compteurColonneX == self.tailleGrille):
                return "X"
            elif compteurLigneO == self.tailleGrille or (compteurColonneO == self.tailleGrille):
                return "O"
            else:
                compteurLigneX = 0
                compteurLigneO = 0
                compteurColonneX = 0
                compteurColonneO = 0
        if compteurDiagonalX == self.tailleGrille * 3:
            return 'X'
        elif compteurDiagonalO == self.tailleGrille * 3:
            return 'O'
        if compteurAntiDiagonalX == self.tailleGrille * 3 :
            return 'X'
        elif compteurAntiDiagonalO == self.tailleGrille * 3 :
            return 'O'
        else:
            return None

    def is_full(self):
        """Retourne True si la grille est pleine (aucun case libre) et False sinon (s'il reste de la place)"""
        for i in range(self.tailleGrille):
            for j in range(self.tailleGrille):
                if self.grille[i, j] == '_':
                    return False
        return True

    def __str__(self):
        """Retourne une chaîne de caractère représentant la grille de jeu. Utilisée directement dans la sortie du
            jeu, en faisant par exemple `print(board)`, où `board` contient une instance de `Board`"""
        return f"{self.grille}"
