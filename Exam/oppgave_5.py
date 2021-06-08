class Gjenstand:
    def __init__(self, navn, fra_aar, til_aar, sted):
        self.navn = navn
        self.fra_aar = fra_aar
        self.til_aar = til_aar
        self.sted = sted
        self.plassering = None

    def __str__(self):
        display_string: str = self.navn

        display_string += ", år: "
        if self.fra_aar == self.til_aar:
            display_string += str(self.fra_aar)
        else:
            display_string += str(self.fra_aar) + " til " + str(self.til_aar)

        display_string += ". Sted: " + self.sted
        if self.plassering is not None:
            display_string += ". Plassering: " + self.plassering

        return display_string


def find_gjenstand_from_year(gjenstand_liste, year: int):
    gjenstand_liste_from_year = list()
    for gjenstand in gjenstand_liste:
        if gjenstand.fra_aar <= year and gjenstand.til_aar >= year:
            gjenstand_liste_from_year.append(gjenstand)
            print(gjenstand)
    return gjenstand_liste_from_year


if __name__ == "__main__":
    gjenstand_liste = list()

    gjenstand = Gjenstand("Langsverd fra jernalder", 500, 1000, "Rogaland")
    gjenstand_liste.append(gjenstand)

    gjenstand = Gjenstand("Gullring fra middelalder", 1030, 1350, "Hordaland")
    gjenstand_liste.append(gjenstand)

    gjenstand = Gjenstand("Spydspiss fra rundt år 600", 550, 650, "Rogaland")
    gjenstand_liste.append(gjenstand)

    gjenstand = Gjenstand("Sykkel fra år 1923", 1923, 1923, "Agder")
    gjenstand_liste.append(gjenstand)

    gjenstand = Gjenstand("Kopp fra romertid", 0, 500, "Rogaland")
    gjenstand_liste.append(gjenstand)

    find_gjenstand_from_year(gjenstand_liste, 500)
