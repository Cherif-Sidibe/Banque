from models.fonction import *
import re

def affichermenu():
    print("1- Faire un dépot")
    print("2- Faire un Retrait")
    print("3- Afficher le solde")
    print("4- Quittez")

def saisir_email():
    while True:
        email = input("Veuillez entrer votre email : ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Email invalide. Essayez encore.")

def depot():
    users = getclients()
    user_active = None
    while user_active == None:
        mail = saisir_email()
        user_active=getclientsbymail(users,mail)
    montant=0
    while montant<1:
        montant=int(input("Entrer le montant :"))
    user_active.solde += montant
    sauvegarderclient(user_active)
    print (f"Le solde de {user_active.prenom} {user_active.nom} est de {user_active.solde}")

def retrait():
    users = getclients()
    user_active = None
    while user_active == None:
        mail = saisir_email()
        user_active = getclientsbymail(users, mail)
    montant = 0
    while montant < 1:
        montant = int(input("Entrer le montant :"))
    user_active.solde -= montant
    sauvegarderclient(user_active)
    print(f"Le solde de {user_active.prenom} {user_active.nom} est de {user_active.solde}")

def consulter():
    users = getclients()
    user_active = None
    while user_active == None:
        mail = saisir_email()
        user_active = getclientsbymail(users, mail)
    print(f"Le solde de {user_active.prenom} {user_active.nom} est de {user_active.solde}")
  