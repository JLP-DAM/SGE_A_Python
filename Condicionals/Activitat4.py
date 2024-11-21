print("Introdueix el teu salari")
Salari = int(input())
IVA = 0

if Salari >= 15000 and Salari < 30000:
    IVA = 10
elif Salari >= 30000:
    IVA = 21

print("Has de pagar un iva de " + str(IVA) + "%, es a dir " + str(Salari * (IVA / 100)) + " €.")

# No he fet < 60000 perque no hi han altres IVAs que aplicar