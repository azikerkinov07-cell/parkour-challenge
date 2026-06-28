# player.py
import pygame

class Player(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 60)
        self.vel_y = 0
        self.on_ground = False
        self.start_x = x
        self.start_y = y
        self.flight_end_time = 0
        self.last_flight_use = 0
        self.is_flying = False

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vel_y = 0
        self.is_flying = False