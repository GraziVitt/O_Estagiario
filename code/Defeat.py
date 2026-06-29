import pygame
from code.Const import *
from code.SoundManager import SoundManager


class Defeat:
    def __init__(self, window):
        self.window = window

        # Imagem de fundo
        self.background = pygame.image.load("assets/background/derrota.png").convert()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))

        # Som de derrota
        self.sound = SoundManager()
        self.sound.load_sound("derrota", "assets/sons/derrota.mp3")

        self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
        self.font = pygame.font.SysFont("Arial", 28, bold=True)

        self.retry_rect = pygame.Rect(0, 0, 300, 64)
        self.retry_rect.center = (WIN_WIDTH // 2, 380)
        self.menu_rect = pygame.Rect(0, 0, 300, 64)
        self.menu_rect.center = (WIN_WIDTH // 2, 460)

        # Paleta (tom avermelhado para a tela de derrota)
        self.base_color = (235, 90, 80)
        self.hover_color = (250, 120, 100)
        self.text_color = (255, 255, 255)
        self.border_color = (110, 25, 20)

    def draw_button(self, rect, text, mouse_pos):
        hovering = rect.collidepoint(mouse_pos)

        # Sombra (superfície separada com alpha)
        shadow_surf = pygame.Surface((rect.width + 4, rect.height + 4), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 90), shadow_surf.get_rect(), border_radius=16)
        self.window.blit(shadow_surf, (rect.x - 2, rect.y + 4))

        # Leve "lift" no hover
        draw_rect = rect.copy()
        if hovering:
            draw_rect.inflate_ip(8, 6)

        top_color = self.hover_color if hovering else self.base_color

        # Corpo do botão com leve gradiente vertical (duas faixas de cor)
        pygame.draw.rect(self.window, top_color, draw_rect, border_radius=16)
        highlight_rect = draw_rect.copy()
        highlight_rect.height = draw_rect.height // 2
        highlight_color = tuple(min(255, c + 25) for c in top_color)
        pygame.draw.rect(
            self.window, highlight_color,
            highlight_rect, border_top_left_radius=16, border_top_right_radius=16
        )

        # Borda
        pygame.draw.rect(self.window, self.border_color, draw_rect, 3, border_radius=16)

        # Texto com leve sombra para legibilidade
        shadow_surf = self.font.render(text, True, (0, 0, 0))
        text_surf = self.font.render(text, True, self.text_color)
        text_rect = text_surf.get_rect(center=draw_rect.center)
        self.window.blit(shadow_surf, (text_rect.x + 2, text_rect.y + 2))
        self.window.blit(text_surf, text_rect)

    def run(self):
        self.sound.play("derrota", volume=0.85)

        while True:
            mouse = pygame.mouse.get_pos()

            # Desenha fundo
            self.window.blit(self.background, (0, 0))

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