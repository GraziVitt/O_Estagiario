import pygame

from code.Const import *

class Boss:

    def __init__(self):

        self.x = 730
        self.y = 120

        self.width = 64
        self.height = 64

        sprite_sheet = pygame.image.load(
            "assets/sprites/chefe.png"
        ).convert_alpha()

        # usa o chefe do meio (expressão neutra)
        self.image = sprite_sheet.subsurface(
            (64, 0, 64, 64)
        )

        self.message = ""
        self.message_timer = 0

        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, window, request):

        window.blit(
            self.image,
            (self.x, self.y)
        )

        pedido = self.font.render(
            request.current_request.upper(),
            True,
            WHITE
        )

        window.blit(
            pedido,
            (620, 80)
        )

        if self.message_timer > 0:

            texto = self.font.render(
                self.message,
                True,
                YELLOW
            )

            window.blit(
                texto,
                (620, 50)
            )

    def update(self):

        if self.message_timer > 0:
            self.message_timer -= 1

    def show_message(self, message):

        self.message = message
        self.message_timer = 90

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )