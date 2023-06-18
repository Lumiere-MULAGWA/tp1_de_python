import time
def montee(niveauAscenseur,niveau_user):
    while(int(niveauAscenseur) <= int(niveau_user)):
        print("niveau : ",niveauAscenseur)
        niveauAscenseur=int(niveauAscenseur)+1
        time.sleep(1)
pass
def descente(niveauAscenseur,niveau_user):
    while(int(niveauAscenseur) >= int(niveau_user)):
        print("niveau : ",niveauAscenseur)
        niveauAscenseur=int(niveauAscenseur)-1
        time.sleep(1)
pass
niveauAscenseur=0
niveau_user=0
while True:
    print("="*30)
    niveau_user=input("Vous etes à quel niveau ? : ")
    if((int(niveauAscenseur) > 12 or int(niveau_user) > 12 or int(niveauAscenseur) < -4 or int(niveau_user) < -4)):
        break
    else:
         if(int(niveauAscenseur) > int(niveau_user)):
            descente(niveauAscenseur,niveau_user)
            print("On est au niveau",niveau_user)
         else:
            montee(niveauAscenseur,niveau_user)
            print("On est au niveau",niveau_user)
          
         niveauAscenseur=niveau_user  
         niveau_user=input("A quelle niveau voulez-vous allez ? : ")
         if((int(niveauAscenseur) > 12 or int(niveau_user) > 12 or int(niveauAscenseur) < -4 or int(niveau_user) < -4)):
            break
         if(int(niveauAscenseur) < int(niveau_user)):
            montee(niveauAscenseur,niveau_user)
            print("Vous etes arrivé au niveau",niveau_user)
         else:
            descente(niveauAscenseur,niveau_user)
            print("Vous etes arrivé au niveau",niveau_user)
            print("_"*30)
         niveauAscenseur=niveau_user
print("="*30)
print("Vous avez entrez un chiffre hors plage, Merci d'avoir utilisé nos service")