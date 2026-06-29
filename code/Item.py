import pygame


class Item:

    def __init__(self, name, image_path, position, size=(32, 32)):

        self.name = name

        self.image = pygame.image.load(image_path).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            size
        )

        self.start_position = position

        self.x = position[0]
        self.y = position[1]

        self.width = size[0]
        self.height = size[1]

        self.collected = False

    def draw(self, window):

        if not self.collected:
            window.blit(self.image, (self.x, self.y))

    def get_rect(self):

        if self.name == "cafe":
            return pygame.Rect(
                self.x - 15,
                self.y - 40,
                self.width + 30,
                self.height + 80
            )

        elif self.name == "documentos":
            return pygame.Rect(
                self.x - 10,
                self.y - 20,
                self.width + 0,
                self.height + 70
            )

        elif self.name == "caneta":
            return pygame.Rect(
                self.x - 20,
                self.y - 20,
                self.width + 40,
                self.height + 40
            )

        elif self.name == "copo":
            return pygame.Rect(
                self.x - 20,
                self.y - 30,
                self.width + 40,
                self.height + 60
            )

        elif self.name == "grampeador":
            return pygame.Rect(
                self.x - 20,
                self.y - 20,
                self.width + 60,
                self.height + 60
            )

        elif self.name == "pasta":
            return pygame.Rect(
                self.x - 20,
                self.y - 25,
                self.width + 40,
                self.height + 50
            )

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def reset(self):

        self.collected = False

        self.x = self.start_position[0]
        self.y = self.start_position[1]

