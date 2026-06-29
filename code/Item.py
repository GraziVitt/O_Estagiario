import pygame


class Item:

    def __init__(self, name, image_path, position):

        self.name = name

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))

        self.start_position = position

        self.x = position[0]
        self.y = position[1]

        self.width = 32
        self.height = 32

        self.collected = False

    def draw(self, window):

        if not self.collected:
            window.blit(self.image, (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def reset(self):
        """Volta o item para o lugar de origem."""

        self.collected = False

        self.x = self.start_position[0]
        self.y = self.start_position[1]