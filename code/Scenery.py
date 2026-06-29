from code.Furniture import Furniture


class Scenery:

    def __init__(self):

        self.furniture = [

            # -------------------------------------------------
            # Mesa do estagiário - ajuste personalizado
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_estagiario.png",
                0, 140,
                size=(260, 212),
                collision_margin=(-80, 60, 60, 55)  # + esquerda, + topo, + direita, + baixo
            ),

            # -------------------------------------------------
            # Mesa do estagiário - Planta
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_estagiario.png",
                0, 140,
                size=(260, 212),
                collision_margin=(210, 110, 10, 55)  # + esquerda, + topo, + direita, + baixo
            ),

            # -------------------------------------------------
            # Cafeteira
            # -------------------------------------------------
            Furniture(
                "assets/furniture/cafeteira.png",
                300, 130,
                size=(140, 176),
                collision_margin=(8, 65, 8, 35)
            ),

            # -------------------------------------------------
            # Impressora
            # -------------------------------------------------
            Furniture(
                "assets/furniture/impressora.png",
                445, 135,
                size=(85, 170),
                collision_margin=(5, 65, 5, 35)
            ),

            # -------------------------------------------------
            # Mesa do chefe
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_chefe.png",
                695, 60,
                size=(160, 295),
                collision_margin=(5, 140, -3, 50)

            ),

            # -------------------------------------------------
            # Mesa do chefe cadeira
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_chefe.png",
                700, 60,
                size=(160, 295),
                collision_margin=(20, 8, -3, 170)


            ),

            # -------------------------------------------------
            # Mesas dos funcionários
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesas_funcionarios.png",
                20, 380,
                size=(380, 174),
                collision_margin=(5, 50, -3, 12)
            ),

            # -------------------------------------------------
            # Mesa de centro
            # -------------------------------------------------
            Furniture(
                "assets/furniture/mesa_centro.png",
                775, 380,
                size=(140, 106),
                collision_margin=(10, 15, 10, 8)
            ),

            # -------------------------------------------------
            # Pilha de papéis
            # -------------------------------------------------
            Furniture(
                "assets/furniture/papeis.png",
                700, 455,
                size=(50, 112),
                collision_margin=(5, 15, 5, 10)
            ),

            # -------------------------------------------------
            # Plantas
            # -------------------------------------------------

            Furniture(
                "assets/furniture/planta.png",
                565, 452,
                size=(50, 115),
                collision_margin=(-5, 30, 10, 15)
            ),

        ]

    def draw(self, window):
        for piece in self.furniture:
            piece.draw(window)