class Rom:
    def __init__(self, beksrivelse, utgang):
        self.beskrivelse = beksrivelse
        self.utgang = utgang
        self.retninger = dict()

    def legg_til_retning(self, retning, rom):
        self.retninger[retning] = rom

    def gaa_i_retning(self, retning):
        if retning in self.retninger:
            return self.retninger[retning]
        else:
            print("Ugyldig rom!")
            return self

    def __str__(self):
        streng = "Rom:\n" + self.beskrivelse
        return streng


# Lager en testlabyrint og returnerer rommet du starter i
def lag_testlabyrint():
    rom1 = Rom("Du starter her. Det er ei lita fontene i dette rommet.", False)
    rom2 = Rom("Et digert tre står i senter av dette rommet. Det er en stige i treet", False)
    rom3 = Rom("Du er i ei hytte oppe i treet. Det er trapper ned og ei hengebro til et annet tre", False)
    rom4 = Rom("Du er på en platting i et stort tre. Det er trapper ned og ei hengebro til et annet tre", False)
    rom5 = Rom("Det er et lite tjern her.", False)
    rom6 = Rom("Det er en stor stein her.", False)
    rom7 = Rom("Gratulerer, du har funne utgangen.", True)

    rom1.legg_til_retning("Nord", rom5)
    rom1.legg_til_retning("Vest", rom2)

    rom2.legg_til_retning("Ost", rom1)
    rom2.legg_til_retning("Nord", rom6)
    rom2.legg_til_retning("Opp", rom3)

    rom3.legg_til_retning("Ned", rom2)
    rom3.legg_til_retning("Nord", rom4)

    rom4.legg_til_retning("Ned", rom7)
    rom4.legg_til_retning("Sor", rom3)

    rom5.legg_til_retning("Vest", rom6)
    rom5.legg_til_retning("Sor", rom1)

    rom6.legg_til_retning("Ost", rom5)
    rom6.legg_til_retning("Sor", rom2)

    # Not needed, but we might want to extend the program later on, so good to have in the first place
    rom7.legg_til_retning("Opp", rom4)

    return rom1


if __name__ == "__main__":
    rommet = lag_testlabyrint()
    while not rommet.utgang:
        print(rommet)
        retning = input("Skriv inn hvilken retning du vil gå: ")
        rommet = rommet.gaa_i_retning(retning)
    print(rommet)
    print("Gratulerer! Du er ute")
