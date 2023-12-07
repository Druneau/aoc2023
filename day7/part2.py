from Hand import Hand
from functools import cmp_to_key

hands = []

with open('day7/input', 'r') as file:
    for line in file:
        hand, bid = line.strip().split()
        hands.append(Hand(hand, bid, joker='J'))


def compare(hand_one, hand_two):
    winner = Hand.get_winner(hand_one, hand_two)

    if winner == hand_one:
        return 1
    else:
        return -1


hands = sorted(hands, key=cmp_to_key(compare))

sum_bid_rank = 0
rank = 1
for h in hands:
    sum_bid_rank += h.bid*rank
    rank += 1

print(sum_bid_rank)
