import pygame

# =====================================================
# TAMANHO DA TELA
# =====================================================

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 567


# =====================================================
# PAREDES
# =====================================================

WALLS = [

    # Superior
    pygame.Rect(0, 0, SCREEN_WIDTH, 40),

    # Esquerda
    pygame.Rect(0, 0, 10, SCREEN_HEIGHT),

    # Direita
    pygame.Rect(SCREEN_WIDTH - 8, 0, 8, SCREEN_HEIGHT),

    # Inferior
    pygame.Rect(0, SCREEN_HEIGHT - 15, SCREEN_WIDTH, 15),

    # Pilar central
    pygame.Rect(291, -60, 60, 215),

    # Parede divisória (parte de cima)
    pygame.Rect(607, -44, 19, 325),

    # Parede divisória (parte de baixo)
    pygame.Rect(618, 440, 19, 136),

]


# =====================================================
# MÓVEIS
# =====================================================

FURNITURE = [

    # -------------------------
    # Estante com binders (canto superior esquerdo)
    # -------------------------
    pygame.Rect(0, -30, 190, 130),

    # -------------------------
    # Estante de livros (verde)
    # -------------------------
    pygame.Rect(355, -30, 212, 130),

    # -------------------------
    # Bebedouro
    # -------------------------
    pygame.Rect(578, -30, 38, 130),

    # -------------------------
    # Planta (esquerda, depois da divisória)
    # -------------------------
    pygame.Rect(630, 4, 40, 120),

    # -------------------------
    # Quadro pequeno / mural colorido
    # -------------------------
    pygame.Rect(670, -6, 52, 110),

    # -------------------------
    # Planta (direita, antes do quadro grande)
    # -------------------------
    pygame.Rect(845, -7, 40, 120),

    # -------------------------
    # Quadro grande (gráfico)
    # -------------------------
    pygame.Rect(900, -60, 85, 160),

    # -------------------------
    # Armário/lixeira cinza (borda direita)
    # -------------------------
    pygame.Rect(985, 40, 39, 100),

    # -------------------------
    # Planta sob o armário (borda direita)
    # -------------------------
    pygame.Rect(985, 170, 39, 90),

    # -------------------------
    # Sofá maior (sala do chefe)
    # -------------------------
    pygame.Rect(740, 475, 220, 80),

    # -------------------------
    # Sofá menor
    # -------------------------
    pygame.Rect(932, 350, 95, 167),



]


# =====================================================
# LISTA GERAL
# =====================================================

COLLIDERS = WALLS + FURNITURE