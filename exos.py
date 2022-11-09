from random import *

def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x,y):
    # si le diviseur est 0
    if y == 0 :
        # alors j'affiche une erreur
        print("erreur de division par 0")
        # je retourne
        return
    # sinon je retourne la division de x par y
    return x / y


def modulo(x,y):
    return x % y


def revenusParSec(salaireH,heureParJO,JOparAn):
    # Je calcule le salaire annuel
    salaireAnnuel = salaireH * heureParJO * JOparAn 
    # Je calcule le nombre de seconde par an
    nbSecondeParAn = 365 * 24 * 60 * 60 
    # Je divise mon salaire par le nombre de seconde dans une année
    return salaireAnnuel / nbSecondeParAn 


def withdrawFees(total, percent):
    #calcul du montant des taxes a retirer
    fees = total * (percent / 100)
    # je retourne mon total sans les taxes
    return total - fees

def calculSalaireNet(salaireBrut, public):
    # si j'occupe un poste de la fonction publique
    if public :
    # alors je retourne le salaire brut - 15 % de taxes
        return withdrawFees(salaireBrut, 15)
    # sinon, c'est que je suis un travailleur privé
    else :
    # alors je retourne le salaire_brut - 23 % de taxes
        return withdrawFees(salaireBrut, 23)


def jouerUnTour():
    return
tour = 0
# Tant que je ne suis pas au tour 5
while tour != 5 :
# Appeler la fonction JouerUnTour
    jouerUnTour()
# J'effectue l'action de passer un tour
    tour += 1


def minijeu(bonCaractere):
    # on definit une variable pour mon caractère aléatoire
    caractereAleatoire = input()
    # tant que input n'est pas le bon caractère
    while caractereAleatoire != bonCaractere :
        # alors on change aléatoirement le input
        caractereAleatoire = input()
    # on affiche un message 
    print("gagner")
    # on retourne le bon caractère
    return caractereAleatoire



#Exo 1
#faire une fonction qui concatene 2 chaines de caractere, les separants par une virgule
def conca(char1,char2):
    if char1 != "":
        charConca = char1 + ", " + char2
        return charConca
    return char2
#Definir  une fonction avec comme paramètres : chaineA et chaineB
#qui retourne la concatenation de chaineA, une comma et enfin chaineB
def concatWithComma(chaineA, chaineB):
    #Je m'assure que chaineA soit bien de type str
    stringifiedChaineA = str(chaineA)
    #Je m'assure que chaineB soit bien de type str
    stringifiedChaineB = str(chaineB)
    #Retourner chaineA concatené avec un comma et chaineB
    return stringifiedChaineA + ", " + stringifiedChaineB

#Exo 2
#faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere avec l'ensemble des occurations d'un chiffre
#pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0,4,7" n'hesitez pas a implementer la premiere fonction
tab = [0,1,1,1,0,1,1,0,1]

#definir une fonction qui prend une liste et une variable  x quelconque
def indexTableau(tableau,index):
    #Initialser i a 0
    i = 0
    #Definir chaineResultat en tant que string vide
    chaineResultat = ""
    #Tant que i est inferieur a la longueur de tableau
    while i < len(tableau):
        #Alors si l'elt d'index i de tableau est egal a x
        if tableau[i] == index :
            #Alors on assigne a chaineResultat le retour de concatWithComma(chaineResultat, i)
            chaineResultat = conca(chaineResultat, i) 
        #On incremente i de 1
        i = i + 1
    #retourner la chaineResultat
    return chaineResultat


print(conca("viande","frite"))
print(indexTableau(tab,0))

def affichage(ele):
    print(ele)

#tel que 
listeUtilisateur = {
    "Alexandre" : "motdepasse",
    "Michel" : "password",
    "Toto" : "12345",
    "JhonDoe" : "azerty"
}

def login(userName, password , listUser):
    if listUser[userName] == password :
        print("good combo")
        return
    else :
        print("bad combo")
        return

affichage(login("Alexandre", "motdepasse", listeUtilisateur))
