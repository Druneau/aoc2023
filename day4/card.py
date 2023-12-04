class Card:
    def __init__(self, raw):
        raw = raw.strip()
        self.raw = raw
        id, numbers = raw.split(':')

        _, id = id.split()
        self.id = int(id)

        winners, picks = numbers.split('|')

        self.winners = winners.split()
        self.picks = picks.split()

        matches = set(self.picks).intersection(self.winners)
        self.winnings = 0
        if len(matches) > 0:
            self.winnings = pow(2, len(matches)-1)
