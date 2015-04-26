import time
import pygame

class Canvas(object):
    def __init__(self):
        self.display = None
        self.game_exiting = False
        self.game_loop_running = False

    def __enter__(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Necklace Builder")
        pygame.display.update()
        return self

    def __exit__(self, _unused1, _unused2, _unused3):
        self.game_exiting = True
        while self.game_loop_running:
            time.sleep(.1)
        pygame.quit()

    def game_loop(self, event_callback):
        self.game_loop_running = True
        while not self.game_exiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exiting = True
                else:
                    event_callback(event)
        self.game_loop_running = False