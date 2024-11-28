class Colibri:
    def __init__(self, Longitud, Latitud, Edat, VelocitatMitjana, Pes):
        self.Longitud = Longitud
        self.Latitud = Latitud
        self.Edat = Edat
        self.VelocitatMitjana = VelocitatMitjana
        self.Pes = Pes

    def GetLongitud(self):
        return self.Longitud

    def GetLatitud(self):
        return self.Latitud

    def GetEdat(self):
        return self.Edat

    def GetVelocitatMitjana(self):
        return self.VelocitatMitjana

    def SetLongitud(self, Longitud):
        self.Longitud = Longitud

    def SetLatitud(self, Latitud):
        self.Latitud