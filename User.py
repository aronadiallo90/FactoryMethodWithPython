
from FabriqueCrack import FabriqueCrack

login = input("Veillez entrer votre login : ")  
password = input("Veillez entrer votre mot de pass : ")   
choix = int( input("Veillez choisir 1 pour BruteForce  2 pour Attaque par dictionnaire : ")  )
FabriqueCrack.getInstance(choix).cracker(password)
print("Vous avez etez pirater ......")