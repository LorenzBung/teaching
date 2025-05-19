class Fahrzeug():
	def __init__(self, geschwindigkeit):
		self.geschwindigkeit = geschwindigkeit
	def fahren(self):
		print("Das Fahrzeug fährt.")
class Auto(Fahrzeug):
	def __init__(self, geschwindigkeit, farbe):
		super().__init__(geschwindigkeit)
		self.farbe = farbe
	def hupen(self):
		print("Das Auto hupt.")
auto1 = Auto(100, "rot")
auto1.hupen()   #Ausgabe: Das Auto hupt.
auto1.fahren()  #Ausgabe: Das Fahrzeug fährt.
