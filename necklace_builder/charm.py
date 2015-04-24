VALID_COLORS = "blue green orange purple red yellow pink".split()
VALID_FLOWERS = "rose orchid daisy sunflower tulip lily daffodil poppy".split()


class ColorException(Exception):
    pass


class FlowerException(Exception):
    pass


class Charm(object):
    def __init__(self):
        self._color = None
        self._flower = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color not in VALID_COLORS:
            raise ColorException("Invalid color choice.")
        self._color = color

    @property
    def flower(self):
        return self._flower

    @flower.setter
    def flower(self, flower):
        if flower not in VALID_FLOWERS:
            raise FlowerException("Invalid flower choice.")
        self._flower = flower

    def __str__(self):
        return "%s %s" % (self.color, self.flower)
