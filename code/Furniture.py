import pygame


class Furniture:
    def __init__(self, image_path, x, y, size=None, collision_margin=None):
        """
        Carrega uma imagem e a coloca na posição (x, y).
        - size: (largura, altura) para redimensionar.
        - collision_margin: int, tupla(2) ou tupla(4) para ajustar colisão.

        O parâmetro always_front foi removido. A ordem de desenho agora é
        controlada pelo depth sort (ordenação por Y) feito em Game.draw().
        """
        self.image_path = image_path
        self.image = pygame.image.load(image_path).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collision_margin = collision_margin

    # ------------------------------------------------------------------
    # Chave usada pelo depth sort: borda inferior do sprite
    # ------------------------------------------------------------------
    def sort_key(self):
        return self.rect.bottom

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