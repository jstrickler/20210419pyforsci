"""
Provide Card and CardDeck classes
"""
import random
from abc import ABCMeta, abstractmethod

# def bark():
#     print("Woof! Woof!")

class Card:
    """
    Represent one playing card.
    """
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """Card Rank"""
        return self._rank

    @property
    def suit(self):
        """Card suit -- one of Clubs, Diamonds, Hearts, Spades"""
        return self._suit

    @property
    def value(self):
        return 42


class DeckBase(metaclass=ABCMeta):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class CardDeck(DeckBase):
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer_name):
        self._dealer_name = None
        self.dealer_name = dealer_name
        self._make_cards()

    def _make_cards(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                # card = Card(rank, suit)
                self._cards.append(card)
    # instance method
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        """
        Draw one card from the deck.

        :return:
        """
        #TODO: handle empty deck
        return self._cards.pop()


    @property
    def dealer_name(self): # getter property
        # look up dealer id# and get string
        return self._dealer_name

    @dealer_name.setter # setter property
    def dealer_name(self, dealer_name):
        if isinstance(dealer_name, str):
            self._dealer_name = dealer_name
        else:
            wrong_type = type(dealer_name).__name__
            raise TypeError(f"Dealer must be a string, not {wrong_type}")

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, value):
        self._animal = value

    @staticmethod
    def bark():
        print("Woof! Woof!")

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        # programmer-friendly
        my_type = type(self)
        my_class_name = my_type.__name__
        return f"{my_class_name}({self.dealer_name}, {len(self)})"


    @classmethod
    def get_ranks(cls):
        return cls.RANKS


    @property
    def cards(self):
        return self._cards

