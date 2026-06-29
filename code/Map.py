import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Map:
    """
    Camada 0 do cenário: o background vazio do escritório.

    Não contém lógica de jogo nem colisão — apenas carrega e
    desenha a imagem de fundo. Pensado para crescer no futuro
    (troca de cenário, parallax, etc.) sem precisar tocar no Game.
    """

    def __init__(self, image_path="assets/background/escritorio.png"):

        self.image = pygame.image.load(image_path).convert()

        self.image = pygame.transform.scale(
            self.image,
            (WIN_WIDTH, WIN_HEIGHT)
        )

    def draw(self, window):

        window.blit(self.image, (0, 0))