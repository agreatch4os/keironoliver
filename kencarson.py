#OLIVER OSTRAT IT22
class Sissekanne:
     def __init__(self, sissekande_tyyp, kuupaev, tundide_arv, hinne=None):
          self.sissekande_tyyp = sissekande_tyyp
          self.kuupaev = kuupaev
          self.tundide_arv = tundide_arv
          self.hinne = hinne
          self.maara_varv()

     def maara_varv(self):
          if self.sissekande_tyyp == "Praktiline töö":
                 self.sissekande_varv = "roheline"
          elif self.sissekande_tyyp == "Teooria":
              self.sissekande_varv = "valge"
          elif self.sissekande_tyyp == "Iseseisev töö":
              self.sissekande_varv = "kollane"

     def muuda_hinnet(self, hinne):
          self.hinne = hinne
     def muuda_tyyp(self, uus_tyyp):
          self.sissekande_tyyp = uus_tyyp
          self.maara_varv()

sissekande1 = Sissekanne("Praktiline töö", "12.02.24", 5, 4)
sissekande2 = Sissekanne("Teeoria", "15.02.2024", 3)

sissekande1.muuda_hinnet(5)
sissekande1.muuda_tyyp("Iseseisev töö")

sissekande2.muuda_hinnet(4)
sissekande2.muuda_tyyp("Praktiline töö")

print("Sissekanne 1:")
print("Tüüp:", sissekande1.sissekande_tyyp)
print("Kuupäev:", sissekande1.kuupaev)
print("Tundide arv:", sissekande1.tundide_arv)
print("Hinne:", sissekande1.hinne)
print("Värv:", sissekande1.sissekande_varv)
print("\nSissekanne 2:")
print("Tüüp:", sissekande2.sissekande_tyyp)
print("Kuupäev:", sissekande2.kuupaev)
print("Tundide arv:", sissekande2.tundide_arv)
print("Hinne:", sissekande2.hinne)
print("Värv:", sissekande2.sissekande_varv)