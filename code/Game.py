import pygame


from code.Const import *
from code.Player import Player
from code.Boss import Boss
from code.Item import Item
from code.Request import Request
from code.Collision import COLLIDERS
from code.Map import Map
from code.Scenery import Scenery



class Game:

    def __init__(self, window):

        self.window = window

        self.clock = pygame.time.Clock()

        self.player = Player()

        self.boss = Boss()

        self.request = Request()

        self.total_time = 40

        self.time_penalty = 3

        self.start_time = pygame.time.get_ticks()

        self.font = pygame.font.SysFont("Arial", 28)

        self.big_font = pygame.font.SysFont("Arial", 42)

        self.map = Map("assets/background/escritorio.png")

        self.scenery = Scenery()

        self.items = [

            Item(
                "cafe",
                "assets/itens/cafe.png",
                (340,210)
            ),

            Item(
                "caneta",
                "assets/itens/caneta.png",
                (45,205)
            ),

            Item(
                "documentos",
                "assets/itens/documentos.png",
                (470,205)
            ),

            Item(
                "copo",
                "assets/itens/copo.png",
                (595,75)
            ),

            Item(
                "grampeador",
                "assets/itens/grampeador.png",
                (65,70)
            ),

            Item(
                "pasta",
                "assets/itens/pasta.png",
                (130,445)
            )

        ]

    # ----------------------------------------------------

    def remaining_time(self):

        elapsed = (

            pygame.time.get_ticks()

            - self.start_time

        ) // 1000

        return self.total_time - elapsed

    # ----------------------------------------------------

    def reset_item(self, item_name):

        for item in self.items:

            if item.name == item_name:

                item.reset()

                break

    # ----------------------------------------------------

    def draw_hud(self):

        time_left = self.remaining_time()

        color = WHITE

        if time_left <= 15:

            color = YELLOW

        if time_left <= 5:

            color = RED

        timer = self.font.render(

            f"Tempo: {time_left}",

            True,

            color

        )

        self.window.blit(timer, (20,20))

        pedidos = self.font.render(

            f"Pedidos: {self.request.completed}/6",

            True,

            WHITE

        )

        self.window.blit(

            pedidos,

            (20,60)

        )

        if self.player.carrying_item:

            carregando = self.font.render(

                f"Item: {self.player.current_item}",

                True,

                YELLOW

            )

            self.window.blit(

                carregando,

                (20,100)

            )

    # ----------------------------------------------------

    def draw(self):

        # Camada 0: background vazio
        self.map.draw(self.window)

        # Camada 1: itens espalhados pelo escritório
        for item in self.items:

            item.draw(self.window)

        # Camada 2: móveis
        self.scenery.draw(self.window)

        # Camada 3: jogador
        self.player.draw(self.window)

        # Camada 4: chefe
        self.boss.draw(

            self.window,

            self.request

        )

        # Camada 5: HUD
        self.draw_hud()

        # ==========================================
        # MOSTRAR COLISÕES
        # ==========================================

        for collider in COLLIDERS:
            pygame.draw.rect(
                self.window,
                (255, 0, 0),
                collider,
                2
            )

        pygame.display.flip()

    # ----------------------------------------------------

    def run(self):

        running = True

        while running:

            self.clock.tick(FPS)

            self.player.move()

            player_rect = self.player.get_rect()

            for wall in COLLIDERS:

                if player_rect.colliderect(wall):
                    self.player.undo_move()

                    break

            self.boss.update()

            time_left = self.remaining_time()

            if time_left <= 0:

                return "LOSE"

            if self.request.game_finished():

                return "WIN"

            # -----------------------------------------
            # Eventos (entrada do jogador)
            # -----------------------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        player_rect = self.player.get_rect()

                        # ===============================
                        # PEGAR ITEM
                        # ===============================

                        if not self.player.carrying_item:

                            for item in self.items:

                                if item.collected:
                                    continue

                                if player_rect.colliderect(item.get_rect()):
                                    item.collected = True

                                    self.player.pick_item(item)

                                    break

                        # ===============================
                        # ENTREGAR ITEM
                        # ===============================

                        else:

                            if player_rect.colliderect(
                                    self.boss.get_rect()
                            ):

                                # ITEM CERTO
                                if self.request.check_delivery(
                                        self.player.current_item
                                ):

                                    self.boss.show_message(
                                        "Boa!"
                                    )

                                # ITEM ERRADO
                                else:

                                    self.boss.show_message(
                                        "Eu nao pedi isso!"
                                    )

                                    self.start_time -= (
                                            self.time_penalty * 1000
                                    )

                                    self.reset_item(
                                        self.player.current_item
                                    )

                                self.player.drop_item()

            # -----------------------------------------
            # Desenha a cada frame (fora do loop de eventos!)
            # -----------------------------------------

            self.draw()

        return "LOSE"