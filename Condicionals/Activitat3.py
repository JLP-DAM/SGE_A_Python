print("Introdueix la nota de l'alumne.")
Nota = int(input())

if Nota < 5:
    print("L’alumne ha suspés.")
elif Nota >= 5 and Nota <= 6.5:
    print("L’alumne ha aprovat.")
elif Nota > 6.5 and Nota <= 8:
    print("L'alumne ha tret un notable!")
elif Nota > 8:
    print("L'alumne ha tret un excel·lent!")
