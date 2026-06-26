import pygame


class Item:

    def __init__(self, nome):
        self.nome = nome
        self.collected = False

        self.width = 32
        self.height = 32

        # -------------------------
        # Imagem de cada item
        # -------------------------

        imagens = {

            "cafe": "assets/itens/cafe.png",

            "caneta": "assets/itens/caneta.png",

            "documentos": "assets/itens/documentos.png",

            "copo": "assets/itens/copo.png",

            "grampeador": "assets/itens/grampeador.png",

            "pasta": "assets/itens/pasta.png"

        }

        # -------------------------
        # Posição fixa dos itens
        # -------------------------

        posicoes = {

            "grampeador": (65, 70),

            "caneta": (45, 205),

            "cafe": (340, 210),

            "documentos": (470, 205),

            "copo": (595, 75),

            "pasta": (130, 445)

        }

        self.x, self.y = posicoes[nome]

        self.image = pygame.image.load(
            imagens[nome]
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (32, 32)
        )

    def draw(self, window):
        if not self.collected:
            window.blit(
                self.image,
                (self.x, self.y)
            )

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
