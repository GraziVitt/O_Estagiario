import pygame


class Boss:

    def __init__(self):

        self.x = 734
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

        # tamanho
        self.normal = pygame.transform.scale(
            self.normal,
            (60,120)
        )

        self.happy = pygame.transform.scale(
            self.happy,
            (60,120)
        )

        self.angry = pygame.transform.scale(
            self.angry,
            (60,120)
        )

        self.current_sprite = self.normal

        # mensagem
        self.message = ""
        self.message_timer = 0

        self.font = pygame.font.SysFont("Arial",24,True)

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

    def draw(self, window, request):

        window.blit(

            self.current_sprite,

            (self.x, self.y)

        )

        pedido = self.font.render(

            request.current_request,

            True,

            (255,255,255)

        )

        window.blit(

            pedido,

            (self.x-10, self.y-30)

        )

        if self.message:

            texto = self.font.render(

                self.message,

                True,

                (255,255,0)

            )

            window.blit(

                texto,

                (self.x-30, self.y-60)

            )

    # ----------------------------------

    def get_rect(self):

        return pygame.Rect(
            self.x - 40,
            self.y + 40,
            150,
            140
        )