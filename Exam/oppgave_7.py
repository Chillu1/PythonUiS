import random


class Terning:
    def __init__(self, antall_sider=6):
        self.__verdi = 1
        self.__sider = antall_sider

    @property
    def verdi(self):
        return self.__verdi

    @property
    def antall_sider(self):
        return self.__sider

    def kast(self):
        self.__verdi = random.randint(1, self.__sider)


class Spiller:
    neste_id = 1  # Klasse-variabel, en for hele klassen heller enn en pr. instans

    # Bruker denne for å lage ID-er for spillerne som automatisk teller
    # opp.
    def __init__(self, navn):
        self.id = Spiller.neste_id  # Bruker klasse-variabelen gjennom navnet til klassen
        Spiller.neste_id += 1
        self.navn = navn
        self.poengsum = 0
        self.staar_over_tur = False  # Innført for å kunne løse frivillig oppgave g)

    def __str__(self):
        return f"Spiller {self.id}: {self.navn} som har {self.poengsum} poeng"


LENGDEN_TIL_VEIEN = 20


# Løsningsforslag til øving 9 del 1
# Oppgave a)
class VanligRute:
    def __init__(self, min_posisjon):
        self.min_posisjon = min_posisjon

    def flytt_hit(self, spiller: Spiller):
        spiller.poengsum = self.min_posisjon
        return f"Spiller {spiller.navn} er flyttet til posisjon {self.min_posisjon}."


# Oppgave b)
class TilbakeTilStart:
    def __init__(self, min_posisjon):
        self.min_posisjon = min_posisjon

    def flytt_hit(self, spiller):
        spiller.poengsum = 0
        return f"Spiller {spiller.navn} prøvde å flytte til {self.min_posisjon} men må rykke tilbake til start"


# Oppgave c)
class Hinder:
    def __init__(self, min_posisjon):
        self.min_posisjon = min_posisjon

    def flytt_hit(self, spiller):
        return f"Spiller {spiller.navn} prøvde å flytte til {self.min_posisjon} men ble hindret"


# Frivillig oppgave g)
class StaaOverTur:
    def __init__(self, min_posisjon):
        self.min_posisjon = min_posisjon

    def flytt_hit(self, spiller):
        spiller.staar_over_tur = True
        return f"Spiller {spiller.navn} prøvde å flytte til {self.min_posisjon} men ble hindret og må stå over sin neste tur"


# Frivillig oppgave f)
class Ekstrakast:
    def __init__(self, min_posisjon, veien):
        self.min_posisjon = min_posisjon
        self.veien = veien
        self.terningen = Terning()

    def flytt_hit(self, spiller):
        resultat = f"Spiller {spiller.navn} flyttet til {self.min_posisjon} og får et ekstrakast \n"
        spiller.poengsum = self.min_posisjon
        self.terningen.kast()
        ny_posisjon = spiller.poengsum + self.terningen.verdi
        if ny_posisjon < len(self.veien):
            resultat += self.veien[ny_posisjon].flytt_hit(spiller)
        else:
            resultat += "Ekstrakastet tok deg utenfor veien!"
            spiller.poengsum = ny_posisjon
        return resultat


class FlyttSpiller:
    def __init__(self, min_posisjon, maal_posision):
        self.min_posisjon = min_posisjon
        self.maal_posision = maal_posision

    def flytt_hit(self, spiller):
        spiller.poengsum = self.maal_posision
        return f"Spilleren {spiller.navn} flytter til rute {self.min_posisjon}, så flyttes den igjen til {self.maal_posision}"


# Hjelpemetode for oppgave d) og e)
def lag_vei():
    veien = list()
    for i in range(LENGDEN_TIL_VEIEN):
        if (i + 1) % 3 == 0:
            if (i + 1) % 9 == 0:
                veien.append(TilbakeTilStart(i))
            elif (i + 1) == 6:
                veien.append(StaaOverTur(i))
            else:
                veien.append(Hinder(i))
        elif (i + 1) % 10 == 0:
            veien.append(Ekstrakast(i, veien))
        elif i + 1 == 5:  # We can hardcode both FlyttSpiller ruter because both of them are "VanligRuter"
            veien.append(FlyttSpiller(i, 12))# TODO FIX ME
        elif i + 1 == 13:
            veien.append(FlyttSpiller(i, 3))
        else:
            veien.append(VanligRute(i))
        #print(veien[i].__class__) # Debug to check if our ruter placements are correct
    return veien


# Oppgave d). Denne er ikke modifisert for de frivillige oppgavene.
def spill_en_spiller():
    spilleren = Spiller("Spilleren")
    terningen = Terning()
    veien = lag_vei()
    while spilleren.poengsum < LENGDEN_TIL_VEIEN:
        terningen.kast()
        verdi = terningen.verdi
        print(f"Spilleren {spilleren.navn} står på posisjon {spilleren.poengsum} og kastet {verdi}")
        if spilleren.poengsum + verdi >= LENGDEN_TIL_VEIEN:
            break
        beskjed = veien[spilleren.poengsum + verdi].flytt_hit(spilleren)
        if spilleren.poengsum >= LENGDEN_TIL_VEIEN:
            break
        print(beskjed)
        input("Trykk enter for å fortsette: ")


# Oppgave e), inkludert modifikasjoner for frivillig oppgave f) og g)
def spill_flere_spillere():
    antall_spillere = int(input("Antall spillere: "))
    spillerne = list()
    for i in range(antall_spillere):
        navn = input(f"Navn til spiller {i + 1}: ")
        spilleren = Spiller(navn)
        spillerne.append(spilleren)
    terningen = Terning()
    veien = lag_vei()
    fortsetter = True
    while fortsetter:
        for spiller in spillerne:
            if spiller.staar_over_tur:
                spiller.staar_over_tur = False
                continue
            terningen.kast()
            verdi = terningen.verdi
            print(f"Spilleren {spiller.navn} står på posisjon {spiller.poengsum} og kastet {verdi}")
            if spiller.poengsum + verdi >= LENGDEN_TIL_VEIEN:
                fortsetter = False
                print(f"Spilleren {spiller.navn} er ferdig med veien og har vunnet!")
                break
            beskjed = veien[spiller.poengsum + verdi].flytt_hit(spiller)
            print(beskjed)
            if spiller.poengsum >= LENGDEN_TIL_VEIEN:
                fortsetter = False
                print(f"Spilleren {spiller.navn} er ferdig med veien og har vunnet!")
                break
            input("Trykk enter for å fortsette: ")


if __name__ == "__main__":
    spill_flere_spillere()
