import random

class Card(object):
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])



class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort(self):
        self.cards.sort()

    def deal_hands(self, num_hands, num_cards):
        hands = []
        for i in range(num_hands):
            new_hand = Hand()
            self.move_cards(new_hand, num_cards)
            hands.append(new_hand)
        return hands

class Hand(Deck):
    
    def __init__(self, label = ''):
        self.cards = []
        self.label = label

deck = Deck()
deck.shuffle()
game = deck.deal_hands(13, 4)

print(game)