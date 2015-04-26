import charmdialog

VALID_COLORS = "blue green orange purple red yellow pink".split()
VALID_FLOWERS = "rose orchid daisy sunflower tulip lily daffodil poppy".split()

class CharmException(Exception):
    pass


class Charm(object):
    def __init__(self):
        self.word = None
        self._color = None
        self._flower = None
        self._image = None

    @property
    def color(self):
        if not self._color:
            raise CharmException("No color set.")
        return self._color

    @color.setter
    def color(self, color):
        if color not in VALID_COLORS:
            raise CharmException("Invalid color choice.")
        self._color = color

    @property
    def flower(self):
        if not self._flower:
            raise CharmException("No flower set.")
        return self._flower

    @flower.setter
    def flower(self, flower):
        if flower not in VALID_FLOWERS:
            raise CharmException("Invalid flower choice.")
        self._flower = flower

    @property
    def image(self):
        if not self._image:
            self._image = pygame.image.load(
                os.path.join("images", self.flower, self.color))
        return self._image

    def on_click(self):
        self.color, self.flower = charmdialog.Dialog()

    def __str__(self):
        return "%s %s" % (self.color, self.flower)

    # Version 2
    def get_custom_charm(self):
        raise NotImplementedError