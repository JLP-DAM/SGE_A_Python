Nombres = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

print("Parells")
for Nombre in Nombres:
    if (Nombre % 2 == 1):
        continue

    print(Nombre)

print("\n\nImparells")
for Nombre in Nombres:
    if (Nombre % 2 == 0):
        continue

    print(Nombre)