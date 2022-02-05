"""
    classe, instance, objet, constructeur, Héritage, méthode(fonction)
    mieux structurer, organiser notre code
    modulaire et évolutif
    Reduire les dépendances (parties de code indépendantes, facilement réutilisable)
"""

#-Difference programmation imperative/ objet

def afficher_infos_personne(nom, age):
    print(f"le nom de la personne est {nom}, son age est {age} ans")

"""def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom?: ")
    return nom
"""
"""#afficher_infos_personne(nom="Bakary",age=2)

nom1 = demander_nom()
age1 = 34
afficher_infos_personne(nom1,age1)"""

# Personne (entité) ---> class
# Donnees: nom, age
# Actions: methodes
#   Se presenter
#   Demander nom (input)


#---Definition

class EtreVivant: #classe parent
    ESPECE = "être vivant non identifie"
    def AfficherInfosEtreVivant(self):
        print("infos être vivant: " + Personne.ESPECE)

class Personne(EtreVivant): # classe enfant
    ESPECE = "espece mammifère" #variable de classe
    def __init__(self, name: str = "", age: int = 0):
        self.name = name    # variable d'une instance: name
        self.age = age
        if name == "":
            self.DemanderNom()
        #print("Bonjour, je m'appelle " + self.name)

    def SePresenter(self):
        info_personne = "Bonjour je m'appelle " + self.name
        if self.age != 0:
            info_personne += " ,j'ai " + str(self.age) + " ans"

        print(info_personne)


        if self.age != 0:
            if self.EstMajeur():
                print(self.name, "est", "majeur")
            else:
                print(self.name, "est", "mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        name = ""
        while self.name == "" or self.name.isdigit():
            self.name = input("Quel est votre nom: ")
        return name

#--- Utilisation
#personne1 = Personne("Bakary",23) # je crée une personne(objet)
personne2 = Personne("Bakary",23)
personne3 = Personne("Pierre",4)

#personne1.SePresenter()  # methode d'instance
list_personnes = ((personne2),(personne3))
for personne in list_personnes:
    personne.SePresenter()
    personne.AfficherInfosEtreVivant()
#print(personne2.EstMajeur())

#Personne.AutreFonction() #methode de classe

# Heritage

class Chat(EtreVivant): #classe enfant
    ESPECE = "Chat mammifère felin"

class Etudiant(Personne):
    def __init__(self, name: str, age: int, etudes: str):
        #self.name = name
        #self.age = age
        super().__init__(name,age)
        self.etudes = etudes

    def SePresenter(self): # surchargé la méthode SePresenter
        super().SePresenter()
        print("Je suis etudiant en: " + self.etudes)



Etudiant("Bakary", 34, "Master").SePresenter()
Etudiant("Bakary", 34, "Master").AfficherInfosEtreVivant()