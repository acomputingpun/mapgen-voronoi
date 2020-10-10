import math

def basicRand(seed):
    if seed < 0:
        return ((-seed) ** (1.9 - 1/seed)) % 1
    elif seed > 0:
        return (seed ** (1.1 + 1/seed)) % 1
    else:
        return 0

def rand(seed):
    return basicRand(((seed*seed)^seed) & 65535)

def randint(seed, smallest, largest):
    return smallest + math.floor(rand(seed) * (largest-smallest))
def uniform(self):
    return smallest + (rand(seed) * (largest-smallest))
def choice(seed, items):
    return items[randint(seed, 0, len(items))]

def shuffle(seed, items) :
    ilen = len(items);
    for k in range(ilen):
        j = randint(seed+k, 0, ilen);
        items[k], items[j] = items[j], items[k]


class Roller:
    def __init__(self, firstSeed) :
        self.seed = firstSeed;

    def rand(self):
        self.seed += 1
        return rand(self.seed);

    def randint(self, smallest, largest) :
        self.seed += 1
        return randint(self.seed, smallest, largest);

    def choice(self, items) :
        self.seed += 1
        return choice(self.seed, items);

    def shuffle(self, items) :
        self.seed += 1
        shuffle(self.seed, items);
