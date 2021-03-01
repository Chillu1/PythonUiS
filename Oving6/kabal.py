from card_deck import CardDeck
from card import Card


class Kabal:
    deck: CardDeck
    placed_cards: list

    def __init__(self):
        self.deck = CardDeck()
        self.deck.shuffle()
        self.placed_cards = []
        for _ in range(0, 9):
            card = self.deck.take()
            self.placed_cards.append(card)

    def write_status(self):
        return f"{self}\nCards left: {len(self.deck)}"

    def __str__(self):
        text = "Cards placed: \n"
        text += "Index\tCardType\tCardValue\n\n"
        index: int = 0
        for card in self.placed_cards:
            text += f"{str(index)}\t{str(card)}\n"
            index += 1
        return text

    def is_game_over(self):
        return len(self.deck) <= 0

    def place_two_cards(self, placement_index_one, placement_index_two):
        if not self.__check_cards_placement(placement_index_one, placement_index_two):
            return
        self.placed_cards[placement_index_one] = self.deck.take()
        self.placed_cards[placement_index_two] = self.deck.take()

    def place_three_cards(self, placement_index_one, placement_index_two, placement_index_three):
        if not self.__check_cards_placement(placement_index_one, placement_index_two, placement_index_three):
            return
        self.placed_cards[placement_index_one] = self.deck.take()
        self.placed_cards[placement_index_two] = self.deck.take()
        self.placed_cards[placement_index_three] = self.deck.take()

    @staticmethod
    def __check_two_cards(value_one, value_two):
        if value_one + value_two == 11:
            return True
        print("Cards don't equal 11, invalid configuration")
        return False

    @staticmethod
    def __check_three_cards(value_one, value_two, value_three):
        if value_one >= 11 and value_two >= 11 and value_three >= 11:
            return True
        print("Not all cards are image cards, invalid configuration")
        return False

    def __check_cards_placement(self, index_one, index_two, index_three=-1):
        if index_three != -1:
            return self.__check_three_cards(self.placed_cards[index_one].value, self.placed_cards[index_two].value,
                                            self.placed_cards[index_three].value)
        return self.__check_two_cards(self.placed_cards[index_one].value, self.placed_cards[index_two].value)
