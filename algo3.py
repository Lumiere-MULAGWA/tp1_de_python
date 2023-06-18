number=int(input("entrez un nombre entre 1 et 12 "))
i=1
while (number<1 ) or (number >13):
    number=int(input("entrer votre nombre entre 1 et 12 "))
    print("######################")
while i<=10:
    somme=number*i
    print(f"{number} x {i} = {somme}")
    i=i+1
print("fin du programme")
