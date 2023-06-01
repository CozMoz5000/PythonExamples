from Frosthaven.deck import Deck

deck = Deck()
for x in range(10):
    card = deck.draw()
    print(f'Card: {card}, Remaining: {[str(x) for x in deck._cards]}')
