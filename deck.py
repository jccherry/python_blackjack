from card import Card
from random import shuffle as list_shuffle

class Deck:

    cards = None

    def __init__(self,number_of_decks=1):
        self.cards = self.reset(number_of_decks)

    def reset(self, number_of_decks=1):
        suit_list = ['Spades','Clubs','Diamonds','Hearts']
        name_list = ['Ace', 'King','Queen','Jack','Ten','Nine','Eight','Seven','Six',
        'Five','Four','Three','Two']
        base_value_list = [11,10,10,10,10,9,8,7,6,5,4,3,2]
        char_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

        cards = []
        for deck_number in range(0,number_of_decks):
            for suit in suit_list:
                for i in range(0,len(name_list)):
                    is_ace = False
                    if char_list[i] == 'A':
                        is_ace = True
                    cards.append(Card(name_list[i] + ' of ' + suit,base_value_list[i],
                    suit, char_list[i],is_ace))
        return cards



    def get_card(self, index):
        if index < len(self.cards):
            return self.cards[index]
        else:
            print('Error: card index out of bounds')

    def print_deck(self):
        for card in self.cards:
            print(card.display_name(), end=" ", flush=True)

    def shuffle(self):
        list_shuffle(self.cards)
