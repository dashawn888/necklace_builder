from collections import deque
from charm import Charm

NECKLACE_SIZE = 2


class Necklace(object):
    def __init__(self):
        self.charms = deque(maxlen=NECKLACE_SIZE)
        for _ in xrange(NECKLACE_SIZE):
            self.charms.append(Charm())


    def __str__(self):
        return "\n".join([str(charm) for charm in self.charms])
