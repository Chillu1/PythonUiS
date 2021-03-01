HORISONTAL = 0
VERTIKAL = 1


class Skip:
    def __init__(self, start_x, start_y, retning, lengde):
        self.start_x = start_x
        self.start_y = start_y
        self.retning = retning
        self.lengde = lengde
        self.antall_treff = 0

    def __str__(self):
        return f"Skip med startkooridinater ({self.start_x}, {self.start_y}) med " \
            f"lengde {self.lengde}, som har tatt {self.antall_treff} treff."

    def treff(self):
        self.antall_treff += 1

    def er_senket(self):
        if self.antall_treff >= self.lengde:
            return True
        else:
            return False


if __name__ == "__main__":
    s1 = Skip(1, 5, HORISONTAL, 4)
    s2 = Skip(4, 1, VERTIKAL, 2)
    print(s1)
    print(s2)
    print()
    while not s1.er_senket():
        s1.treff()
        print(s1)
    while not s2.er_senket():
        s2.treff()
        print(s2)
