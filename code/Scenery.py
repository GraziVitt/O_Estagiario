from code.Furniture import Furniture


class Scenery:
    """
    Camada 1 do cenário (agrupada): centraliza a criação e o
    desenho de todos os móveis do escritório.

    O Game não precisa saber nomes de arquivo nem posições de
    móvel — ele só chama scenery.draw(window).

    Os PNGs de mobília foram exportados em resolução muito maior
    que a cena (de 3x a 6x). Por isso cada Furniture aqui usa o
    parâmetro 'size' para redimensionar a imagem, mantendo a
    proporção (altura/largura) original de cada arquivo.

    IMPORTANTE: x, y e size são um ponto de partida calculado a
    partir da imagem de referência do escritório completo. Ajuste
    olhando o jogo rodando, do mesmo jeito que você já fez com os
    retângulos do Collision.py.
    """

    def __init__(self):

        self.furniture = [

            # -------------------------------------------------
            # Mesa do estagiário (papéis + monitor + cadeira + planta)
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_estagiario.png",
                0, 140,
                size=(260, 212)
            ),

            # -------------------------------------------------
            # Estação de café
            # -------------------------------------------------
            Furniture(
                "assets/furniture/cafeteira.png",
                300, 130,
                size=(140, 176)
            ),

            # -------------------------------------------------
            # Impressora
            # -------------------------------------------------
            Furniture(
                "assets/furniture/impressora.png",
                445, 154,
                size=(90, 150)
            ),

            # -------------------------------------------------
            # Mesa do chefe (cadeira + laptop + papéis)
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_chefe.png",
                690, 74,
                size=(165, 270)
            ),

            # -------------------------------------------------
            # Mesas dos funcionários (fileira com 4 estações)
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesas_funcionarios.png",
                20, 380,
                size=(380, 174)
            ),

            # -------------------------------------------------
            # Mesa de centro (perto do sofá)
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_centro.png",
                775, 380,
                size=(125, 100)
            ),

            # -------------------------------------------------
            # Pilha de papéis (perto do sofá)
            # -------------------------------------------------
            Furniture(
                "assets/furniture/papeis.png",
                695, 455,
                size=(50, 112)
            ),

            # -------------------------------------------------
            # Planta
            # -------------------------------------------------

            Furniture(
                "assets/furniture/planta.png",
                565, 452,
                size=(50, 115)
            ),

        ]

    def draw(self, window):

        for piece in self.furniture:

            piece.draw(window)