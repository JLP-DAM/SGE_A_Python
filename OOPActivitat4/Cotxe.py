class Cotxe:
    def __init__(self, Marca, Model, Preu, Kilometratge, Pes):
        self.Marca = Marca
        self.Model = Model
        self.Preu = Preu
        self.Kilometratge = Kilometratge
        self.Pes = Pes

    def GetMarca(self):
        return self.Marca

    def GetModel(self):
        return self.Model

    def GetPreu(self):
        return self.Preu

    def SetMarca(self, Marca):
        self.Marca = Marca

    def SetModel(self, Model):
        self.Model = Model