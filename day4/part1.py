from card import Card

totalPoints = 0

with open('day4/input', 'r') as file:

    for line in file:
        card = Card(line)
        totalPoints += card.points

print(totalPoints)
