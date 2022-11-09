
#on admet une fonction random qui retourne un chiffre aleatoire entre 0 et 2 compris
#on admet une fonction input qui recupere l'entree d'un joueur

#on definit une fonction PFC avec comme parametre nombreJoueur et turnWin
    #on determine un tableau avec comme valeur "pierre" , "feuille" et "ciseaux"
    #on determine noWin a True
    #on initialise pointJoueurA a 0
    #on initialise pointJoueurB a 0

    #on affiche "nom du joueur 1: "
    #on determine nomJoueurA a le string de la fonction input
    #si il n'y a qu'un joueur
        #alors on determine nomJoueurB a "IA"
    #sinon 
        #on affiche "nom du joueur 2: "
        # on determine nomJoueurB a le string de la fonction input

    #tant que noWin est egal a true et que pointJoueurA est inferieur a turnWin et que pointJoueurB est inferieur a turnWin
        #alors
        #on initialise choixJoueurA a l'integer de la fonction input
        #si il n'y a qu'un joueur
            #alors on initialise choixJoueurA a l'integer de la fonction random
        #sinon on initialise choixJoueurB a l'integer de la fonction input
        #si choixJoueurA est égal a 0
            #alors
            #si choixJoueurB est égal a 1
                #alors 
                #on incremente poinJoueurA de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurA
            #on affiche nomJoueurA et pointJoueurA
            #on affiche nomJoueurB et pointJoueurB

