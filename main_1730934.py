from tictactoe_1730934 import Player, Board

def NouvellePartie():
    nvPartie = input("Voulez-vous jouer une autre partie?")
    if (nvPartie == "o") or (nvPartie == "oui"):
        board.clear_board()
        return True
    elif (nvPartie == "n") or (nvPartie == "non"):
        return False
        print("Fin de jeu")
    else:
        print("Incorrect! Veuillez entrer un de ces choix: o, n, oui, non")
        NouvellePartie()



def InfoGagnant():
    print(board)
    print("\n")
    print("Nombre de victoires:")
    print(f"{joueurUn.name}: {joueurUn.n_wins}")
    print(f"{joueurDeux.name}: {joueurDeux.n_wins}")


def Gagnant():
    charGagnant = board.get_winner()
    if charGagnant is not None:
        if joueurUn.char == charGagnant:
            joueurUn.n_wins += 1
            print(f"Gagnant(e): {joueurUn.name} ({joueurUn.char})!")
            InfoGagnant()
            return NouvellePartie()

        if joueurDeux.char == charGagnant:
            joueurDeux.n_wins += 1
            print(f"Gagnant(e): {joueurDeux.name} ({joueurDeux.char})!")
            InfoGagnant()
            return NouvellePartie()


def Position(char):
    print("Entrez la position où vous voulez jouer:")
    ligne = int(input("Ligne: ", ))
    colonne = int(input("Colonne: "))

    while (ligne > 2 or ligne < 0) or (colonne > 2 or colonne < 0):
        print("Le nombre doit être entre 0 et 2 inclusivement")
        print("Entrez la position où vous voulez jouer:")
        ligne = int(input("Ligne: "))
        colonne = int(input("Colonne: "))
    valeurPosition = board.get(ligne, colonne)
    while valeurPosition != "_":
        print("Vous ne pouvez pas jouer là!")
        print("\n")

        print(board)
        if char == joueurUn.char:
            print(joueurUn)
        else:
            print(joueurDeux)
        print("Entrez la position où vous voulez jouer:")
        ligne = int(input("Ligne: ", ))
        colonne = int(input("Colonne: "))
        while (ligne > 2 or ligne < 0) or (colonne > 2 or colonne < 0):
            print("Le nombre doit être entre 0 et 2 inclusivement")
            print("Entrez la position où vous voulez jouer:")
            ligne = int(input("Ligne: "))
            colonne = int(input("Colonne: "))
        valeurPosition = board.get(ligne, colonne)
    return ligne, colonne


nomJoueurUn = input("Quel est le nom du premier joueur?: ")
charJoueurUn = input("Quel caractère voulez-vous utiliser (X/O)?: ")
nomJoueurDeux = input("Quel est le nom du deuxième joueur?: ")
charJoueurDeux = input("Quel caractère voulez-vous utiliser (X/O)?: ")

board = Board()

joueurUn = Player(nomJoueurUn, charJoueurUn)
joueurDeux = Player(nomJoueurDeux, charJoueurDeux)
print("\n")
print(joueurUn)
print(joueurDeux)

partie = True
while partie != False:
    gagnant = None
    print(2 * "\n")
    print(board)
    print(joueurUn)
    pos = Position(joueurUn.char)
    board.set(pos[0], pos[1], joueurUn.char)
    if board.is_full():
        print("Égalité! Aucun(e) gagnant(e)!")
        partie = NouvellePartie()
    partie = Gagnant()
    if partie != False:
        print(board)
        print(joueurDeux)
        pos = Position(joueurDeux.char)
        board.set(pos[0], pos[1], joueurDeux.char)
        if board.is_full():
            print("Égalité! Aucun(e) gagnant(e)!")
            partie = NouvellePartie()
        partie = Gagnant()
