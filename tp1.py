#---------Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
def ex1():
    from math import pi
    r = float(input("saisir le rayon du cone droit : "))
    h = float(input("saisir la hauteur du cone droit : "))
    v = 1/3*pi*r**2*h
    print ("le volume du cone droit est : ",v)

#---------Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.
def ex2():
    a = None
    i = 0
    TTC = 0
    while a != 0 :
        a = float(input("entrer le prix HT"))
        TTC += a 
        i += 1
    TTC /= i-1
    print("TTC est : ",TTC)     

#------------Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls.
#------------Comptez combien il y avait de données et combien étaient supérieures à 100.
#------------Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.
def ex3():
    a = int (input("entrer un nonbre : "))
    sup = 0
    nb_donne = 0
    sum = 0
    while a > 0:
        nb_donne += 1
        if a> 100:
            sup += 1
        sum += a  
        a = int (input("entrer un nonbre : ")) 

    print("le somme des nombre saisi est : ",sum)
    print("tu as saisi ",nb_donne," nombre.")
    print("tu as saisi ",sup," nombre superieur a 100 ")

#-----------L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon.
def ex4():
    a = int (input("entrer un nombre :"))
    if a%2 == 0:
        return "pair"
    else :
        return "impair"     

#L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.
def ex5():
    a = None
    try:
        a = int(input("entrer un nombre entier : "))
    except:
        print("erreur de saisi !!! ")
        