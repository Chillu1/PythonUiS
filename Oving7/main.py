from tur import Tur

tur = Tur("First", 2, 3)
tur.add_posisjon_koordinater(2, 3, 2)
tur.add_posisjon_koordinater(20, 5, 20)
tur.add_posisjon_koordinater(18, 13, 22)
tur.add_posisjon_koordinater(2, 3, 2)

print(f"Hoydemeter: {tur.hoydemeter()}")
print(f"Rundetur: {tur.er_rundtur()}")

turTwo = Tur("Second", 2, 3)
turTwo.add_posisjon_koordinater(5, 3, 10)
turTwo.add_posisjon_koordinater(15, 5, 18)
turTwo.add_posisjon_koordinater(12, 15, 12)

print(f"Hoydemeter: {turTwo.hoydemeter()}")
print(f"Rundetur: {turTwo.er_rundtur()}")
