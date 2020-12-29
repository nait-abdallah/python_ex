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

#L'utilisateur donne un entier positif et le programme annonce combien de fois 
# de suite cet entier est divisible par 2.
def ex5():
    b = 0 #conteur de combien de fois il est divisible 
    while True:
        try:
            a = int (input("entrer un nombre positif : "))
            break
        except:
            print("ereur dans la saisi 'entrer un nombre ' !!!")
    print("le nombre ",a," est divisible par 2 : ")   
    while a != 0:
        if a%2==0:
            a /= 2
            b += 1
        else: break  
    print(b," fois .")       

#L'utilisateur donne un entier supérieur à 1 et le programme affiche, 
# s'il y en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. 
# S'il n'y en a pas, il indique qu'il est premier.
def ex6():
    # -*- coding : utf8 -*-
    """Diviseurs propres d'un entier."""

    # Programme principal =========================================================
    n = int(input("Entrez un entier strictement positif :"))
    while n < 1:
        n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

    i = 2 # plus petit diviseur possible de n
    cpt = 0 # initialise le compteur de divisions
    p = n/2 # calculé une fois dans la boucle

    print("Diviseurs propres sans répétition de", n, " :", end=' ')
    while i <= p :
        if n%i == 0:
            cpt += 1
            print(i, end=' ')
        i += 1

    if not cpt :
        print("aucun ! Il est premier.")
    else :
        print("(soit", cpt, "diviseurs propres)")
            
# Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…
# Écrire une procédure (donc sans return) hauteurParcourue qui reçoit deux paramètres, le nombre
#   de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
# Sélectionnez
# Pour x marches de y cm, il parcourt z.zz m par semaine.
# On n'oubliera pas :
# qu'une semaine comporte 7 jours ;
# qu'une fois en bas, le gardien doit remonter ;
# que le résultat est à exprimer en m
def ex7(Nb_de_marche,H_de_marche):
    res = Nb_de_marche*H_de_marche*2*5*7*(10**(-2))
    print("pour ",Nb_de_marche," de ",H_de_marche," cm, il parcourt ",res," m par semaine .")

