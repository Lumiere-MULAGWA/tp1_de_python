name=input("entrez le nom de l'invite ")
print(f"vous avez invite {name}")
count=1
reponse=input("voulez vous ajoutez un autre invite?:(oui/non): ").lower()

while reponse == "oui":
    name=input("entre le nom de l'invite: ")
    print(f"vous avez invitez {name} ")
    count=count+1
    reponse=input("voulez vous ajoutez un autre invite?:(oui/non): ").lower()
print(f"vous avez invitée {count} personne(s) ")


