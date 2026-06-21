import pygame

from code.Const import *


class Menu:

    def __init__(self, window):

        self.window = window

        # Fundo

        self.background = pygame.image.load(
            "assets/background/menu.jpeg"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        # Botão Jogar

        self.play = pygame.image.load(
            "assets/ui/jogar.png"
        ).convert_alpha()

        self.play = pygame.transform.scale(
            self.play,
            (300, 90)
        )

        # Botão Sair

        self.exit = pygame.image.load(
            "assets/ui/sair.png"
        ).convert_alpha()

        self.exit = pygame.transform.scale(
            self.exit,
            (300, 90)
        )

        # Retângulos dos botões

        self.play_rect = self.play.get_rect(
            center=(WIN_WIDTH // 2, 340)
        )

        self.exit_rect = self.exit.get_rect(
            center=(WIN_WIDTH // 2, 470)
        )

        # Música

        pygame.mixer.music.load(
            "assets/sons/menu.mp3"
        )

    def draw_text(self, text, size, color, x, y):

        font = pygame.font.SysFont(
            "Arial",
            size,
            bold=True
        )

        surf = font.render(
            text,
            True,
            color
        )

        rect = surf.get_rect(center=(x, y))

        self.window.blit(surf, rect)

    def run(self):

        pygame.mixer.music.play(-1)

        while True:

            mouse = pygame.mouse.get_pos()

            # Fundo

            self.window.blit(
                self.background,
                (0, 0)
            )

            # Botões

            self.window.blit(
                self.play,
                self.play_rect
            )

            self.window.blit(
                self.exit,
                self.exit_rect
            )

            # Melhor tempo

            self.draw_text(

                "Melhor Tempo: --",

                28,

                (255, 255, 255),

                WIN_WIDTH // 2,

                410

            )

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.play_rect.collidepoint(mouse):
                        pygame.mixer.music.stop()

                        return "PLAY"

                    if self.exit_rect.collidepoint(mouse):
                        pygame.quit()

                        quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()

                        return "PLAY"
