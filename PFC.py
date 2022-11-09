
#on admet une fonction random qui retourne un chiffre aleatoire entre 0 et 2 compris
#on admet une fonction input qui recupere l'entree d'un joueur

#on definit une fonction PFC avec comme parametre nombreJoueur et turnWin

    #on determine un tableau avec comme valeur "pierre" , "feuille" et "ciseaux"
    #on determine noWin a true
    #on initialise pointJoueurA a 0
    #on initialise pointJoueurB a 0

    #on affiche "nom du joueur 1: "
    #on assigne a nomJoueurA le string du retour de l'execution de la fonction input
    #si il n'y a qu'un joueur
        #alors on determine nomJoueurB a "IA"
    #sinon 
        #on affiche "nom du joueur 2: "
        #on assigne a nomJoueurB le string du retour de l'execution de la fonction input

    #tant que noWin est egal a true
        #alors
        #on assigne a choixJoueurA le retour de l'execution de la fonction input
        #si il n'y a qu'un joueur
            #alors on assigne a choixJoueurB le retour de l'execution de la fonction random
        #sinon on assigne a choixJoueurB le retour de l'execution de la fonction input

        #si choixJoueurA est égal a 0
            #alors
            #si choixJoueurB est égal a 0
                #alors 
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "égalité"

            #si choixJoueurB est égal a 1
                #alors 
                #on incremente poinJoueurB de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurB
        
            #si choixJoueurB est égal a 2
                #alors 
                #on incremente poinJoueurA de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurA

        #sinon si choixJoueurA est égal a 1
            #alors
            #si choixJoueurB est égal a 1
                #alors 
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "égalité"

            #si choixJoueurB est égal a 2
                #alors 
                #on incremente poinJoueurB de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurB
        
            #si choixJoueurB est égal a 0
                #alors 
                #on incremente poinJoueurA de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurA
        
        #sinon
            #alors
            #si choixJoueurB est égal a 2
                #alors 
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "égalité"

            #si choixJoueurB est égal a 0
                #alors 
                #on incremente poinJoueurB de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurB
        
            #si choixJoueurB est égal a 1
                #alors 
                #on incremente poinJoueurA de 1
                #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
                #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
                #on affiche "le vainqueur de la manche est " et nomJoueurA
            

        #on affiche nomJoueurA et pointJoueurA
        #on affiche nomJoueurB et pointJoueurB
        #si pointJoueurA est egal a turnWin
            #alors
            #on passe noWIn a false
            #on determine vainqueur a nomJoueurA
        #si pointJoueurB est egal a turnWin
            #alors
            #on passe noWIn a false
            #on determine vainqueur a nomJoueurB

    #on affiche "le vainqueur est : " et vainqueur
#fin fonction

