from Cotxe import Cotxe
from Colibri import Colibri

Cotxe1 = Cotxe("Pedra", "A1", 30000, 0, 1500)
Cotxe2 = Cotxe("Paper", "B2", 15000, 10050, 500)
Cotxe3 = Cotxe("Tissores", "C3", 60000, 62015, 2000)
# 3 instàncies de Cotxe

Colibri1 = Colibri(-3.45714, -81.38784, 5, 30, 200)
Colibri2 = Colibri(-13.39443, 106.97962, 2, 15, 150)
Colibri3 = Colibri(45.97043, 70.58274, 10, 10, 300)
# 3 instàncies de Colibrí

print(Cotxe1.GetMarca())
print(Cotxe2.GetModel())
print(Cotxe3.GetPreu())
# 3 getters de Cotxe

print(Colibri1.GetLongitud())
print(Colibri2.GetLatitud())
print(Colibri3.GetEdat())
print(Colibri1.GetVelocitatMitjana())
# 4 getters de Colibrí

Cotxe1.SetMarca("Paper")
Cotxe2.SetModel("A1")
# 2 atributs de Cotxe modificats a través dels setters

print(Cotxe1.GetMarca())
print(Cotxe2.GetModel())
# Mostrant 2 atributs de Cotxe modificats a través dels setters

Colibri1.SetLongitud(-19.00094)
Colibri2.SetLatitud(48.03035)
# 2 atributs de Cotxe modificats a través dels setters

print(Colibri1.GetLongitud())
print(Colibri2.GetLatitud())
# Mostrant 2 atributs de Cotxe modificats a través dels setters