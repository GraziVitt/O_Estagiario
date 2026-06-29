import pygame
from code.Const import *
from code.SoundManager import SoundManager


class Menu:

    def __init__(self, window):
        self.window = window

        self.sound = SoundManager()
        self.sound.play_music("assets/sons/menu.mp3", volume=0.6)

        # Fundo (tela vazia do computador)
        self.background = pygame.image.load("assets/background/menu.png").convert()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))

        # Fonte pixel / monoespaçada
        self.font_title  = pygame.font.SysFont("Courier New", 30, bold=True)
        self.font_item   = pygame.font.SysFont("Courier New", 22, bold=True)
        self.font_cursor = pygame.font.SysFont("Courier New", 22, bold=True)

        # Opções do menu
        self.options = ["NOVO DIA", "PEDIR DEMISSÃO"]
        self.selected = 0

        # Melhor tempo registrado (recorde do jogador)
        self.best_score = self.load_best_score()
        self.font_score = pygame.font.SysFont("Courier New", 18, bold=True)

        # Legenda de comandos (exigência da faculdade: mostrar os controles no menu)
        self.font_controls = pygame.font.SysFont("Courier New", 16, bold=True)
        self.controls = [
            "W A S D - Mover",
            "ESPACO - Pegar / Entregar item",
        ]

        # Posição da área da tela do monitor na imagem (calibrado para 1024x559)
        # Centro horizontal da tela do monitor: ~525
        # Área útil (abaixo do título): Y 270 a 420
        self.screen_cx   = 515   # centro X da tela do monitor
        self.menu_top    = 240   # Y do primeiro botão
        self.menu_step   = 30    # espaçamento entre botões

        # Cores estilo fósforo verde
        self.COLOR_BG       = (10,  30,  10)   # fundo dos botões
        self.COLOR_TEXT     = (80, 200,  80)   # texto normal
        self.COLOR_SELECTED = (20,  20,  10)   # texto do item selecionado
        self.COLOR_HL_BG    = (90, 210,  80)   # fundo do item selecionado
        self.COLOR_BORDER   = (60, 160,  60)   # borda dos botões
        self.COLOR_CURSOR   = (160, 255, 120)  # cursor ►

        # Dimensões dos botões
        self.btn_w = 270
        self.btn_h = 25

        # Animação de piscar do cursor
        self.blink_timer = 0
        self.blink_on    = True

    # ----------------------------------------------------------

    def load_best_score(self):
        """Lê o melhor tempo salvo em disco (data/best_score.txt), se existir."""
        import os
        path = "data/best_score.txt"
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    return int(f.read().strip())
            except (ValueError, OSError):
                return None
        return None

    # ----------------------------------------------------------

    def _btn_rect(self, index):
        """Retorna o pygame.Rect do botão na posição index."""
        x = self.screen_cx - self.btn_w // 2
        y = self.menu_top + index * self.menu_step
        return pygame.Rect(x, y, self.btn_w, self.btn_h)

    # ----------------------------------------------------------

    def draw(self):
        # 1. Fundo (imagem do monitor vazio)
        self.window.blit(self.background, (0, 0))

        now = pygame.time.get_ticks()

        # Piscar a cada 500 ms
        if now - self.blink_timer > 500:
            self.blink_on    = not self.blink_on
            self.blink_timer = now

        # 2. Desenha cada opção
        for i, text in enumerate(self.options):
            rect = self._btn_rect(i)
            is_sel = (i == self.selected)

            # Fundo do botão
            if is_sel:
                pygame.draw.rect(self.window, self.COLOR_HL_BG, rect, border_radius=3)
            else:
                pygame.draw.rect(self.window, self.COLOR_BG, rect, border_radius=3)

            # Borda
            pygame.draw.rect(self.window, self.COLOR_BORDER, rect, width=1, border_radius=3)

            # Texto centralizado
            color = self.COLOR_SELECTED if is_sel else self.COLOR_TEXT
            surf  = self.font_item.render(text, True, color)
            tx    = rect.centerx - surf.get_width() // 2
            ty    = rect.centery - surf.get_height() // 2
            self.window.blit(surf, (tx, ty))

            # Cursor ► à esquerda do item selecionado (piscante)
            if is_sel and self.blink_on:
                cur = self.font_cursor.render("►", True, self.COLOR_CURSOR)
                self.window.blit(cur, (rect.x - cur.get_width() - 6,
                                       rect.centery - cur.get_height() // 2))

        # 3. Score: melhor tempo do jogador, exibido embaixo dos botões
        score_y = self.menu_top + len(self.options) * self.menu_step - 1
        if self.best_score is not None:
            score_text = f"MELHOR TEMPO: {self.best_score}s"
        else:
            score_text = "MELHOR TEMPO: --"

        score_surf = self.font_score.render(score_text, True, self.COLOR_CURSOR)
        score_x = self.screen_cx - score_surf.get_width() // 2
        self.window.blit(score_surf, (score_x, score_y))

        # 4. Legenda de comandos, dentro da tela do monitor, abaixo do score
        controls_y = score_y + score_surf.get_height() + 2
        for line in self.controls:
            line_surf = self.font_controls.render(line, True, self.COLOR_TEXT)
            line_x = self.screen_cx - line_surf.get_width() // 2
            self.window.blit(line_surf, (line_x, controls_y))
            controls_y += line_surf.get_height() + 4

        pygame.display.update()

    # ----------------------------------------------------------

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            mouse = pygame.mouse.get_pos()

            # Hover com mouse atualiza seleção
            for i in range(len(self.options)):
                if self._btn_rect(i).collidepoint(mouse):
                    self.selected = i

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Navegação pelo teclado
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.selected = (self.selected - 1) % len(self.options)
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.selected = (self.selected + 1) % len(self.options)
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        return self._confirm()

                # Clique com mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.options)):
                        if self._btn_rect(i).collidepoint(mouse):
                            self.selected = i
                            return self._confirm()

    # ----------------------------------------------------------

    def _confirm(self):
        """Processa a opção selecionada e retorna o resultado."""
        self.sound.stop_music()

        if self.selected == 0:   # NOVO DIA
            return "PLAY"
        elif self.selected == 1: # PEDIR DEMISSÃO
            pygame.quit()
            quit()