import pygame

from code.Const import *


class Defeat:
    """
    Tela exibida quando o tempo acaba antes do jogador
    entregar todos os pedidos.
    """

    def __init__(self, window):

        self.window = window

        self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
        self.font = pygame.font.SysFont("Arial", 30)

        self.retry_rect = pygame.Rect(0, 0, 280, 70)
        self.retry_rect.center = (WIN_WIDTH // 2, 360)

        self.menu_rect = pygame.Rect(0, 0, 280, 70)
        self.menu_rect.center = (WIN_WIDTH // 2, 450)

    def draw_button(self, rect, text, mouse_pos):

        hovering = rect.collidepoint(mouse_pos)

        color = (255, 200, 0) if hovering else (255, 255, 255)

        pygame.draw.rect(self.window, color, rect, border_radius=12)
        pygame.draw.rect(self.window, BLACK, rect, 3, border_radius=12)

        text_surf = self.font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=rect.center)

        self.window.blit(text_surf, text_rect)

    def run(self):
        """
        Retorna "RESTART" ou "MENU"
        """

        while True:

            mouse = pygame.mouse.get_pos()

            self.window.fill((110, 20, 20))

            title_surf = self.title_font.render(
                "VOCE PERDEU!", True, WHITE
            )

            title_rect = title_surf.get_rect(
                center=(WIN_WIDTH // 2, 180)
            )

            self.window.blit(title_surf, title_rect)

            self.draw_button(self.retry_rect, "Jogar de novo", mouse)
            self.draw_button(self.menu_rect, "Voltar ao Menu", mouse)

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.retry_rect.collidepoint(mouse):
                        return "RESTART"

                    if self.menu_rect.collidepoint(mouse):
                        return "MENU"

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return "RESTART"

                    if event.key == pygame.K_ESCAPE:
                        return "MENU"