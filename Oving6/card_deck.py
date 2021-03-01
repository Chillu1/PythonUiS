from card import Card
import random


class CardDeck:
    cards: list

    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            self.cards.append(Card("Club", i))
            self.cards.append(Card("Diamond", i))
            self.cards.append(Card("Heart", i))
            self.cards.append(Card("Spade", i))

    def shuffle(self):
        random.shuffle(self.cards)

    def take(self):
        card = self.cards[-1]
        del self.cards[-1]
        return card

    def __str__(self):
        text = "Carddeck \n"
        for card in self.cards:
            text += str(card) + "\n"
        return text

    def __len__(self):
        return len(self.cards)
