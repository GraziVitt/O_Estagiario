import pygame


class Boss:

    # Caminho dos ícones dos itens (mesmas imagens usadas em Game.py),
    # usados para deixar o balão de pedido mais claro e bonito.
    ITEM_ICONS = {
        "cafe": "assets/itens/cafe.png",
        "caneta": "assets/itens/caneta.png",
        "documentos": "assets/itens/documentos.png",
        "copo": "assets/itens/copo.png",
        "grampeador": "assets/itens/grampeador.png",
        "pasta": "assets/itens/pasta.png",
    }

    ITEM_LABELS = {
        "cafe": "Café",
        "caneta": "Caneta",
        "documentos": "Documentos",
        "copo": "Copo",
        "grampeador": "Grampeador",
        "pasta": "Pasta",
    }

    def __init__(self):

        self.x = 739
        self.y = 77

        self.width = 55
        self.height = 50

        # ----------------------------
        # Sprites
        # ----------------------------

        self.normal = pygame.image.load(
            "assets/boss/chefe_normal.png"
        ).convert_alpha()

        self.happy = pygame.image.load(
            "assets/boss/chefe_feliz.png"
        ).convert_alpha()

        self.angry = pygame.image.load(
            "assets/boss/chefe_bravo.png"
        ).convert_alpha()

        # ----------------------------
        # Tamanho
        # ----------------------------

        self.normal = pygame.transform.scale(
            self.normal,
            (50, 110)
        )

        self.happy = pygame.transform.scale(
            self.happy,
            (50, 110)
        )

        self.angry = pygame.transform.scale(
            self.angry,
            (50, 110)
        )

        self.current_sprite = self.normal

        # ----------------------------
        # Ícones dos itens (para o balão de pedido)
        # ----------------------------

        self.icons = {}
        for name, path in self.ITEM_ICONS.items():
            try:
                icon = pygame.image.load(path).convert_alpha()
                icon = pygame.transform.smoothscale(icon, (36, 36))
                self.icons[name] = icon
            except pygame.error:
                self.icons[name] = None

        # ----------------------------
        # Mensagem
        # ----------------------------

        self.message = ""
        self.message_timer = 0

        self.font = pygame.font.SysFont("Arial", 24, True)
        self.label_font = pygame.font.SysFont("Arial", 16, True)

    # ----------------------------------

    def show_message(self, text):

        self.message = text

        self.message_timer = pygame.time.get_ticks()

        if text == "Boa!":
            self.current_sprite = self.happy
        else:
            self.current_sprite = self.angry

    # ----------------------------------

    def update(self):

        if self.message:

            if pygame.time.get_ticks() - self.message_timer > 1500:

                self.message = ""

                self.current_sprite = self.normal

    # ----------------------------------
    # DESENHA APENAS O SPRITE
    # ----------------------------------

    def draw_sprite(self, window):

        window.blit(

            self.current_sprite,

            (self.x, self.y)

        )

    # ----------------------------------
    # Balão de fala estilo "comic", com cantos arredondados e rabicho
    # ----------------------------------

    def _draw_bubble(self, window, rect, tail_pos, bg_color=(255, 255, 255), border_color=(40, 40, 40)):
        # sombra leve (superfície separada com alpha, pois a janela não suporta alpha direto)
        shadow_surf = pygame.Surface((rect.width + 6, rect.height + 6), pygame.SRCALPHA)
        pygame.draw.rect(
            shadow_surf, (0, 0, 0, 70),
            (3, 3, rect.width, rect.height), border_radius=14
        )
        window.blit(shadow_surf, (rect.x + 2, rect.y + 2))

        # corpo do balão
        pygame.draw.rect(window, bg_color, rect, border_radius=14)
        pygame.draw.rect(window, border_color, rect, width=2, border_radius=14)

        # rabicho (triângulo apontando para o chefe)
        tx, ty = tail_pos
        points = [
            (tx - 8, ty),
            (tx + 10, ty),
            (tx, ty + 14),
        ]
        pygame.draw.polygon(window, bg_color, points)
        pygame.draw.polygon(window, border_color, points, width=2)

    # ----------------------------------
    # DESENHA APENAS TEXTOS / BALÃO DE PEDIDO
    # ----------------------------------

    def draw(self, window, request):

        # --------- Balão de pedido (com ícone do item) ---------
        if request.current_request:
            icon = self.icons.get(request.current_request)
            label = self.ITEM_LABELS.get(request.current_request, request.current_request)

            bubble_w, bubble_h = 150, 60
            bubble_rect = pygame.Rect(0, 0, bubble_w, bubble_h)
            bubble_rect.midbottom = (self.x + self.width // 2, self.y - 14)

            self._draw_bubble(
                window,
                bubble_rect,
                tail_pos=(bubble_rect.centerx, bubble_rect.bottom - 2),
            )

            content_x = bubble_rect.x + 12

            if icon:
                icon_rect = icon.get_rect()
                icon_rect.midleft = (content_x, bubble_rect.centery)
                window.blit(icon, icon_rect)
                text_x = icon_rect.right + 10
            else:
                text_x = content_x

            label_surf = self.label_font.render(label, True, (30, 30, 30))
            label_rect = label_surf.get_rect()
            label_rect.midleft = (text_x, bubble_rect.centery)
            window.blit(label_surf, label_rect)

        # --------- Balão de reação (acertou / errou) ---------
        if self.message:
            if self.message == "Boa!":
                bg_color = (210, 250, 210)
                border_color = (40, 140, 60)
                text_color = (20, 90, 30)
            else:
                bg_color = (255, 220, 220)
                border_color = (170, 40, 40)
                text_color = (140, 20, 20)

            msg_surf = self.font.render(self.message, True, text_color)

            padding_x, padding_y = 16, 10
            msg_rect = pygame.Rect(
                0, 0,
                msg_surf.get_width() + padding_x * 2,
                msg_surf.get_height() + padding_y * 2,
            )
            msg_rect.midbottom = (self.x + self.width // 2, self.y - 80)

            self._draw_bubble(
                window,
                msg_rect,
                tail_pos=(msg_rect.centerx, msg_rect.bottom - 2),
                bg_color=bg_color,
                border_color=border_color,
            )

            text_rect = msg_surf.get_rect(center=msg_rect.center)
            window.blit(msg_surf, text_rect)

    # ----------------------------------

    def get_rect(self):

        return pygame.Rect(

            self.x - 40,

            self.y + 40,

            150,

            140

        )