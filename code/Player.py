import pygame

from code.Const import *


class Player:

    def __init__(self):

        self.width = 32
        self.height = 32

        self.x = 100
        self.y = 300

        self.speed = PLAYER_SPEED

        self.carrying_item = False
        self.current_item = None

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        if self.x < 0:
            self.x = 0

        if self.x > WIN_WIDTH - self.width:
            self.x = WIN_WIDTH - self.width

        if self.y < 0:
            self.y = 0

        if self.y > WIN_HEIGHT - self.height:
            self.y = WIN_HEIGHT - self.height

    def draw(self, window):

        pygame.draw.rect(
            window,
            BLUE,
            (self.x, self.y, self.width, self.height)
        )