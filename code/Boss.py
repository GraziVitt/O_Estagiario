import pygame


class Boss:

    def __init__(self):
        self.width = 60
        self.height = 80

        # Posição do chefe
        self.x = 620
        self.y = 240

        # Cor temporária (depois será substituída pelo sprite)
        self.color = (180, 50, 50)

        self.font = pygame.font.SysFont(None, 28)

    def draw(self, window, request):
        # Desenha o chefe
        pygame.draw.rect(
            window,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

        # Balão
        balloon = pygame.Rect(
            self.x - 60,
            self.y - 75,
            180,
            50
        )

        pygame.draw.rect(
            window,
            (255, 255, 255),
            balloon,
            border_radius=8
        )

        pygame.draw.rect(
            window,
            (0, 0, 0),
            balloon,
            2,
            border_radius=8
        )

        # Texto
        text = self.font.render(
            f"Quero: {request.current_request}",
            True,
            (0, 0, 0)
        )

        window.blit(
            text,
            (
                balloon.x + 10,
                balloon.y + 15
            )
        )

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
