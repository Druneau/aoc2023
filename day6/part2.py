

class Race:
    def __init__(self, time, record) -> None:
        self.time = time
        self.record = record
        self.simulations = {}
        self.simulate()

    def simulate(self):
        for t in range(self.time + 1):
            dist = self.calc_distance(t)
            self.add_simulation(t, dist)

    def calc_distance(self, hold_time):
        speed = hold_time
        distance = (self.time - hold_time) * speed
        return distance

    def add_simulation(self, hold_time, distance):
        self.simulations[hold_time] = distance

    def get_wins_count(self):
        wins = 0
        for _, v in self.simulations.items():
            if self.record < v:
                wins += 1
        return wins


races = []

race = Race(45977295, 305106211101695)

combinations = race.get_wins_count()

print(combinations)
