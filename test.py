def concatWithComma(chaineA, chaineB):
    #Je m'assure que chaineA soit bien de type str
    stringifiedChaineA = str(chaineA)
    #Je m'assure que chaineB soit bien de type str
    stringifiedChaineB = str(chaineB)
    #Retourner chaineA concatené avec un comma et chaineB
    return stringifiedChaineA + ", " + stringifiedChaineB

print(concatWithComma(5,"fruits"))

def indexTableau(tableau,index):
    #Initialser i a 0
    i = 0
    #Definir chaineResultat en tant que string vide
    chaineResultat = ""
    #on determine firstTurn a true
    firstTurn = True
    #Tant que i est inferieur a la longueur de tableau
    while i < len(tableau):
        #Alors si l'elt d'index i de tableau est egal a x
        if tableau[i] == index :
            #Alors
            #Si je suis au premier tour ( si firstTurn est vrai)
            if firstTurn :
                #Alors j'assigne str(i) a chaineResultat
                chaineResultat = str(i)
                #On passe firstTurn a False
                firstTurn = False
            #Sinon on assigne a chaineResultat le retour de concatWithComma(chaineResultat, i)
            else :
                chaineResultat = concatWithComma(chaineResultat, i) 
        #On incremente i de 1
        i = i + 1
    #retourner la chaineResultat
    return chaineResultat

tab = [0,1,1,1,0,1,1,0,1]
print(indexTableau(tab,0))
