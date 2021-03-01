from card import Card

class Player:
    name : str
    card : Card

    def __init__(self, name, card):
        self.name = name
        self.card = card
