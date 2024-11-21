print("Introdueix nombres fins que encertis el rang correcte")

Nombre = 0

while (Nombre < 100 or Nombre > 400):
    Nombre = int(input())

    if (Nombre < 100 or Nombre > 400):
        print("Incorrecte.")

print("Has encertat!")