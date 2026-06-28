import pygame


class Furniture:

    def __init__(self, image_path, x, y, collision):

        self.image = pygame.image.load(image_path).convert_alpha()

        self.x = x
        self.y = y

        self.rect = self.image.get_rect(topleft=(x, y))

        # collision = (offset_x, offset_y, largura, altura)

        self.collision = pygame.Rect(

            x + collision[0],
            y + collision[1],
            collision[2],
            collision[3]

        )

    def draw(self, window):

        window.blit(self.image, (self.x, self.y))

    def get_collision(self):

        return self.collision