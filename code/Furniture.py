import pygame

class Furniture:
    def __init__(self, image_path, x, y, size=None):
        """
        Carrega uma imagem e a coloca na posição (x, y).
        Se 'size' for fornecido (tupla (largura, altura)), redimensiona a imagem.
        """
        self.image = pygame.image.load(image_path).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, window):
        """Desenha o móvel na tela."""
        window.blit(self.image, self.rect)

    def get_rect(self):
        """Retorna o retângulo do móvel (para colisão)."""
        return self.rect

    def get_collision(self):
        """Retorna o retângulo de colisão (pode ser o mesmo que o rect)."""
        return self.rect