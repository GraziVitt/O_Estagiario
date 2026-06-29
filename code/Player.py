import pygame

from code.Const import *


class Player:

    def __init__(self):

        # -------------------------
        # Posição inicial
        # -------------------------

        self.x = 90
        self.y = 110

        self.old_x = self.x
        self.old_y = self.y

        self.speed = 4

        self.width = 40
        self.height = 55

        # -------------------------
        # Distância extra para pegar/entregar itens
        # -------------------------
        # Quanto maior esse número, mais "de longe" o jogador
        # consegue pegar um item ou entregar pro chefe — útil
        # quando o item está em cima de um móvel e a colisão
        # do móvel não deixa o player_rect chegar bem perto.
        self.pickup_range = 16

        # -------------------------
        # Sistema de itens
        # -------------------------

        self.carrying_item = False
        self.current_item = None

        # -------------------------
        # Direção
        # -------------------------

        self.direction = "frente"

        # -------------------------
        # Animação
        # -------------------------

        self.frame = 0
        self.animation_speed = 0.18
        self.moving = False

        # -------------------------
        # Carrega sprites
        # -------------------------

        self.sprites = {

            "frente": [

                pygame.image.load(
                    "assets/sprites/frente_0.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/frente_1.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/frente_2.png"
                ).convert_alpha()

            ],

            "costas": [

                pygame.image.load(
                    "assets/sprites/costas_0.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/costas_1.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/costas_2.png"
                ).convert_alpha()

            ],

            "esquerda": [

                pygame.image.load(
                    "assets/sprites/esquerda_0.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/esquerda_1.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/esquerda_2.png"
                ).convert_alpha()

            ],

            "direita": [

                pygame.image.load(
                    "assets/sprites/direita_0.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/direita_1.png"
                ).convert_alpha(),

                pygame.image.load(
                    "assets/sprites/direita_2.png"
                ).convert_alpha()

            ]

        }

        # -------------------------
        # Redimensiona
        # -------------------------

        self.scale = 60

        for direction in self.sprites:

            for i in range(len(self.sprites[direction])):

                self.sprites[direction][i] = pygame.transform.scale(

                    self.sprites[direction][i],

                    (self.scale, self.scale * 2)

                )

    # =======================================

    def move(self):

        self.old_x = self.x
        self.old_y = self.y

        keys = pygame.key.get_pressed()

        self.moving = False

        if keys[pygame.K_w]:

            self.y -= self.speed

            self.direction = "costas"

            self.moving = True

        elif keys[pygame.K_s]:

            self.y += self.speed

            self.direction = "frente"

            self.moving = True

        elif keys[pygame.K_a]:

            self.x -= self.speed

            self.direction = "esquerda"

            self.moving = True

        elif keys[pygame.K_d]:

            self.x += self.speed

            self.direction = "direita"

            self.moving = True

        if self.moving:

            self.frame += self.animation_speed

            if self.frame >= 3:

                self.frame = 0

        else:

            self.frame = 0

    # =======================================

    def draw(self, window):

        sprite = self.sprites[self.direction][int(self.frame)]

        window.blit(

            sprite,

            (

                self.x - 10,

                self.y - 45

            )

        )

    # =======================================

    def get_rect(self):

        area = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        area.inflate_ip(14, 10)  # aumenta 30 pixels para cada lado

        return area

    # =======================================

    def get_interaction_rect(self):
        """
        Rect maior que o de colisão, usado apenas para checar
        se o jogador está perto o suficiente de um item ou do
        chefe para pegar/entregar. Não interfere na colisão de
        movimento (paredes e móveis continuam usando get_rect()).
        """

        return self.get_rect().inflate(

            self.pickup_range,

            self.pickup_range

        )

    # =======================================

    def pick_item(self, item):

        self.carrying_item = True

        self.current_item = item.name

    # =======================================

    def drop_item(self):

        self.carrying_item = False

        self.current_item = None

    def undo_move(self):

        self.x = self.old_x
        self.y = self.old_y