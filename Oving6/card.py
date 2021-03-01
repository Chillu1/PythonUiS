class Card():
    """
    Base card class
    """
    type: str
    value: int

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        display = f"{self.type}\t\t"

        if 1 <= self.value <= 10:
            display += str(self.value)
        elif self.value == 11:
            display += "Jack"
        elif self.value == 12:
            display += "Queen"
        elif self.value == 13:
            display += "King"

        if display == f"{self.type} ":
            raise ValueError('Unidentfied card value/type')

        return display
