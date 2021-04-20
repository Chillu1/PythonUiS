class Player:
    next_id: int = 1        # Klasse-variabel, en for hele klassen heller enn en pr. instans
                        # Bruker denne for å lage ID-er for spillerne som automatisk teller
                        # opp.

    def __init__(self, name):
        self.id = Player.next_id      # Bruker klasse-variabelen gjennom navnet til klassen
        Player.next_id += 1
        self.name = name
        self.points = 0

    def __str__(self):
        return f"Player {self.id}: {self.name} who has {self.points} points"

    def info(self):
        return f"Player {self.id}: {self.name}"