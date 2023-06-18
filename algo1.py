def pgcd(a,b):
    if b ==0:
        return a
    else:
        return pgcd(b,a%b)
a=int(input("entrer nombre "))
b=int(input("entrer nombre "))
resultat=pgcd(a,b)
print(resultat)