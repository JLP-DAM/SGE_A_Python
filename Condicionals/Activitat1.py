print("Escriu dos nombres per comprar-los")
Nombre1 = input()
Nombre2 = input()

if Nombre1 > Nombre2:
    print(Nombre1 + " es mes petit que " + Nombre2)
elif Nombre2 > Nombre1:
    print(Nombre2 + " es mes gran que " + Nombre1)
else:
    print(Nombre2 + " es igual a " + Nombre1)