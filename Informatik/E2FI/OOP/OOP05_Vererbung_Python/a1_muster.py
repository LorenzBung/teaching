class Produkt():
    def __init__(self, produktnummer, bezeichnung, preis):
        self.produktnummer = produktnummer
        self.bezeichnung = bezeichnung
        self.preis = preis
    def verkaufen(self):
        print(f"Das Produkt mit der Nummer {self.produktnummer} wurde für {self.preis} verkauft.")

class Pflanze(Produkt):
    def __init__(self, produktnummer, bezeichnung, preis, gattung, hoehe):
        super().__init__(produktnummer, bezeichnung, preis)
        self.gattung = gattung
        self.hoehe = hoehe
    def einpflanzen(self):
        print(f"Die Pflanze mit der Produktnummer {self.produktnummer} wurde eingepflanzt.")

class Blumentopf(Produkt):
    def __init__(self, produktnummer, bezeichnung, preis, material, volumen):
        super().__init__(produktnummer, bezeichnung, preis)
        self.material = material
        self.volumen = volumen
    def befuellen(self):
        print(f"Der Topf mit der Nummer {self.produktnummer} wurde mit {self.volumen} Liter befüllt.")

class Werkzeug(Produkt):
    def __init__(self, produktnummer, bezeichnung, preis, istElektrisch):
        super().__init__(produktnummer, bezeichnung, preis)
        self.istElektrisch = istElektrisch
