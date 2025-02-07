import json
BD="models/bd.json"

class  Utilisateurs:
    def __init__(self,nom,prenom,email,pwd,solde):
        self.nom=nom
        self.prenom=prenom
        self.email=email
        self.pwd=pwd
        self.solde=solde
   

    
def chargerclients():
    with open(BD,"r") as f:
        bd =json.load(f) 
    return bd

def getallclients(bd):
    clients=[]
    for i in bd["clients"]:
        clients.append(i)
    return clients



def getclients():
    data=chargerclients()
    clients=getallclients(data)
    l=[]
    for i in clients:
        l.append(Utilisateurs(i["nom"],i["prenom"],i["email"],i["password"],i["solde"]))
    return l   

def getclientsbymail(users,mail):
    for i in users:
        if i.email == mail : 
            return i
    return None
    

def afficherclient(users):
    for i in users:
        print("Nom :",i.nom)
        print("Prenom :",i.prenom)
        print("Email :",i.email)
        print("Password :",i.pwd,"\n")

def sauvegarderclient(user):
    data = chargerclients()  
    clients = data["clients"]
    
    for i in range(len(clients)):
        if clients[i]["email"] == user.email:
            clients[i]["nom"] = user.nom
            clients[i]["prenom"] = user.prenom
            clients[i]["email"] = user.email
            clients[i]["password"] = user.pwd
            clients[i]["solde"] = user.solde
            break
    with open(BD, "w") as f:
        json.dump(data, f, indent=4)


