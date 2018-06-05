import random


def make_deck(jokers=False):
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    numbers = [str(i) for i in range(1, 11)] + ['jack', 'queen', 'king', 'ace']
    cards = []
    for suit in suits:
        for num in numbers:
            card = ' of '.join((num, suit))
            cards.append(card)
    if jokers:
        cards = cards + ['joker', 'joker']
    random.shuffle(cards)
    return cards


class Hand(object):
    def __init__(self):
        self._card_list = []

    def __repr__(self):
        return str(self._card_list)

    def play(self, card_index):
        return self._card_list.pop(card_index)

    def add(self, card: str):
        self._card_list.append(card)

    def discard(self, card_index):
        self._card_list.pop(card_index)

    def show(self):
        return self._card_list


class Table(Hand):
    def __init__(self):
        super().__init__()


class Game(object):
    def __init__(self, num_players: int):
        self.players = [Hand() for i in range(num_players)]
        self.table = Table()
        self.deck = make_deck(jokers=True)

    def __repr__(self):
        return str(self.show())

    def show(self):
        return {
            'num_players': len(self.players),
            'player_hands': [player.show() for player in self.players],
            'num_player_cards': [len(player.show()) for player in self.players],
            'table': self.table.show(),
        }

    def deal(self, num_cards_each):
        for i in range(num_cards_each):
            for player in self.players:
                player.add(self.deck.pop())

    def table_cards(self, num_cards):
        for i in range(num_cards):
            self.table.add(self.deck.pop())

