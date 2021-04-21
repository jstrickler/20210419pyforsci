from carddeck import CardDeck

class Game:
    def get_instructions(self):
        return "this is how to play..."


class JokerDeck(CardDeck, Game):

    def _make_cards(self):
        super()._make_cards()
        for _ in range(2):
            card = "Joker", 'Joker'
            self._cards.append(card)
