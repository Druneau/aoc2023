from enum import Enum
from random import random

from collections import Counter


class OrderedEnum(Enum):

    def __ge__(self, other):

        if self.__class__ is other.__class__:

            return self.value >= other.value

        return NotImplemented

    def __gt__(self, other):

        if self.__class__ is other.__class__:

            return self.value > other.value

        return NotImplemented

    def __le__(self, other):

        if self.__class__ is other.__class__:

            return self.value <= other.value

        return NotImplemented

    def __lt__(self, other):

        if self.__class__ is other.__class__:

            return self.value < other.value

        return NotImplemented


class HandType(OrderedEnum):
    FIVE_KIND = 7
    FOUR_KIND = 6
    FULL_HOUSE = 5
    THREE_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class CardType(OrderedEnum):
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10


class Hand:
    def __init__(self, cards, bid=0, joker=None) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.joker = joker
        self.type = self.get_type(cards)

    def get_type(self, cards):
        same_counts = Counter(cards)

        if self.joker is not None:
            if self.joker in self.cards:

                joker_count = same_counts[self.joker]

                if joker_count != 5:
                    same_counts.pop(self.joker, None)
                    max_card = max(same_counts, key=same_counts.get)
                    same_counts[max_card] += joker_count

        number_counts = len(same_counts)
        max_count = max(list(same_counts.values()))

        if number_counts == 1:
            return HandType.FIVE_KIND

        if number_counts == 2:
            if max_count == 4:
                return HandType.FOUR_KIND
            if max_count == 3:
                return HandType.FULL_HOUSE

        if number_counts == 3:
            if max_count == 2:
                return HandType.TWO_PAIR
            if max_count == 3:
                return HandType.THREE_KIND

        if number_counts == 4:
            return HandType.ONE_PAIR

        if number_counts == 5:
            return HandType.HIGH_CARD

    @staticmethod
    def get_winner(hand_one, hand_two):
        if hand_one.type > hand_two.type:
            return hand_one
        elif hand_one.type < hand_two.type:
            return hand_two
        if hand_one.type == hand_two.type:
            return Hand.get_hand_winner(hand_one, hand_two)

    @staticmethod
    def get_hand_winner(hand_one, hand_two):
        joker = hand_one.joker
        for c1, c2 in zip(hand_one.cards, hand_two.cards):
            if Hand.get_card_value(c1, joker) > Hand.get_card_value(c2, joker):
                return hand_one
            if Hand.get_card_value(c1, joker) < Hand.get_card_value(c2, joker):
                return hand_two

        raise ValueError('Identical hands... no winner!')

    @staticmethod
    def get_card_value(card, joker=None):

        if str.isdigit(card):
            value = card
        else:
            value = CardType[card].value

        if joker is not None:
            if card == joker:
                value = 1

        return int(value)
