from card import Card


scratchCount = {}

with open('day4/input', 'r') as file:

    for line in file:
        card = Card(line)

        # we scratched the card
        if card.id in scratchCount:
            scratchCount[card.id] += 1
        else:
            scratchCount[card.id] = 1

        copies = scratchCount[card.id]

        # we need to add copies for winnings
        for c in card.cardsWon:
            if c in scratchCount:
                scratchCount[c] += copies
            else:
                scratchCount[c] = copies

        print(card.points)


print(sum(scratchCount.values()))
