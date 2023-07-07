import random
from dataclasses import dataclass

@dataclass
class Card:
    value: str
    _reshuffle: bool
    _lost: bool
    _function: callable

    def __str__(self) -> str:
        return self.value


class Deck:
    def __init__(self) -> None:
        self._cards = []
        self._drawn_cards = []

        self._initialize()

    def _initialize(self) -> None:
        # Set up the deck from scratch
        self._cards.append(Card('Null', True, False, lambda x: x * 0))
        self._cards.append(Card('2x', True, False, lambda x: x * 2))

        self._cards.append(Card('-2', False, False))
        self._cards.append(Card('+2', False, False))

        for _ in range(5):
            self._cards.append(Card('-1', False, False))
            self._cards.append(Card('+1', False, False))

        self._cards.extend([Card('+0', False, False) for _ in range(6)])

        # Initially shuffle the cards
        self._reshuffle()

    def _reshuffle(self) -> None:
        # Add all drawn cards back
        self._cards.extend(self._drawn_cards)
        self._drawn_cards.clear()

        # Shuffle the cards
        random.shuffle(self._cards)

    def draw(self) -> Card:
        # Get the next card off the deck
        card = self._cards.pop(0)

        if not card._lost:
            self._drawn_cards.append(card)

        # Reshuffle if the card wants us to, or we are out of cards
        if card._reshuffle or not self._cards:
            self._reshuffle()

        return card
