class Card:
    #a Card

    is_ace = None
    base_value = None
    suit = None
    full_name = None
    char_symbol = None

    def __init__(self, full_name, base_value, suit, char_symbol, is_ace):
        self.base_value = base_value
        self.is_ace = is_ace
        self.suit = suit
        self.full_name = full_name
        self.char_symbol = char_symbol

    def get_value(self):
        if not self.is_ace:
            return self.base_value
        else:
            return '1 or 11'

    def get_suit(self):
        return self.suit

    def display_name(self):
        char = '♠'
        if self.suit == 'Spades':
            char = '♠'
        elif self.suit == 'Clubs':
            char = '♣'
        elif self.suit == 'Diamonds':
            char = '♦'
        elif self.suit == 'Hearts':
            char = '♥'
        return str(self.char_symbol + char)


#end Card
