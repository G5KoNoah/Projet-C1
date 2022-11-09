def concatWithComma(chaineA, chaineB):
    #Je m'assure que chaineA soit bien de type str
    stringifiedChaineA = str(chaineA)
    #Je m'assure que chaineB soit bien de type str
    stringifiedChaineB = str(chaineB)
    #Retourner chaineA concatené avec un comma et chaineB
    return stringifiedChaineA + ", " + stringifiedChaineB

print(concatWithComma(5,"fruits"))