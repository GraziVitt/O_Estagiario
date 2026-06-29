import pygame

class Furniture:
    def __init__(self, image_path, x, y, size=None, collision_margin=None, always_front=False):
        """
        Carrega uma imagem e a coloca na posição (x, y).
        - size: (largura, altura) para redimensionar.
        - collision_margin: int, tupla(2) ou tupla(4) para ajustar colisão.
        - always_front: se True, este móvel sempre será desenhado por cima do jogador.
        """
        self.image = pygame.image.load(image_path).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collision_margin = collision_margin
        self.always_front = always_front  # <--- NOVO

    def draw(self, window):
        window.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect

    def get_collision(self):
        if self.collision_margin is None:
            return self.rect

        col_rect = self.rect.copy()

        if isinstance(self.collision_margin, int):
            return col_rect.inflate(self.collision_margin, self.collision_margin)
        elif isinstance(self.collision_margin, (tuple, list)):
            if len(self.collision_margin) == 2:
                return col_rect.inflate(self.collision_margin[0], self.collision_margin[1])
            elif len(self.collision_margin) == 4:
                left, top, right, bottom = self.collision_margin
                col_rect.x += left
                col_rect.y += top
                col_rect.width -= (left + right)
                col_rect.height -= (top + bottom)
                return col_rect

        return self.rect