from views.fonction import *

while True:
    affichermenu()
    choix=int(input("Entrer votre choix : "))
    if choix == 1 :
        depot()
    elif choix == 2 :
        retrait()
    elif choix == 3 :
        consulter()
    elif choix == 4 :
        print('Au revoir !')
        break
    else:
        print("ERREUR ! Choix indisponible ")
