from collections import deque
from charm import Charm

NECKLACE_SIZE = 2


class Necklace(object):
    def __init__(self):
        self.charms = deque(
            [Charm() for _ in xrange(NECKLACE_SIZE)],
            maxlen=NECKLACE_SIZE)

    def __str__(self):
        return "\n".join([str(charm) for charm in self.charms])
