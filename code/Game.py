import pygame

from code.Const import *
from code.Player import Player
from code.Boss import Boss
from code.Item import Item
from code.Request import Request
from code.Collision import COLLIDERS, WALLS, FURNITURE
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

        self.background = pygame.image.load(
            "assets/background/escritorio.png"
        ).convert()
        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.items = [

            Item(
                "cafe",
                "assets/itens/cafe.png",
                (320, 200),
                (28, 36)
            ),

            Item(
                "caneta",
                "assets/itens/caneta.png",
                (359, 460),
                (34, 15)
            ),

            Item(
                "documentos",
                "assets/itens/documentos.png",
                (470, 205),
                (38, 28)
            ),

            Item(
                "copo",
                "assets/itens/copo.png",
                (587, 99),
                (20, 30)
            ),

            Item(
                "grampeador",
                "assets/itens/grampeador.png",
                (175, 235),
                (30, 18)
            ),

            Item(
                "pasta",
                "assets/itens/pasta.png",
                (120, 418),
                (36, 42)
            )

        ]

        self.scenery = Scenery()

    # ---------------------------------------------------------

    def remaining_time(self):
        elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
        return self.total_time - elapsed

    # ---------------------------------------------------------

    def reset_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.reset()
                break

    # ---------------------------------------------------------

    def draw_hud(self):
        time_left = self.remaining_time()
        color = WHITE
        if time_left <= 15:
            color = YELLOW
        if time_left <= 5:
            color = RED

        timer = self.font.render(f"Tempo: {time_left}", True, color)
        self.window.blit(timer, (20, 20))

        pedidos = self.font.render(
            f"Pedidos: {self.request.completed}/6",
            True,
            WHITE
        )
        self.window.blit(pedidos, (20, 60))

        if self.player.carrying_item:
            carregando = self.font.render(
                f"Item: {self.player.current_item}",
                True,
                YELLOW
            )
            self.window.blit(carregando, (20, 100))

    # ---------------------------------------------------------

    def draw(self):
        # 1. Fundo
        self.window.blit(self.background, (0, 0))

        # ------------------------------------------------------------------
        # Depth sort unificado — todos os elementos competem pelo mesmo Y.
        # mesa_chefe, chefe e tampo_mesa recebem Y fixos que garantem a
        # ordem correta entre si, mas o jogador pode ultrapassá-los quando
        # seu Y real for maior (mais abaixo na tela).
        #
        # Y fixos escolhidos:
        #   mesa_chefe  → 250  (base da mesa, atrás do chefe)
        #   chefe       → 260  (na frente da mesa, atrás do tampo)
        #   tampo_mesa  → 270  (frente da mesa, cobre o chefe)
        #
        # O jogador entra com seu Y real. Quando estiver acima da mesa
        # (Y < 270) fica atrás do tampo; quando estiver abaixo (Y > 270)
        # fica na frente — efeito correto de profundidade.
        # ------------------------------------------------------------------

        MESA_Y  = 250
        CHEFE_Y = 260
        TAMPO_Y = 270

        entities = []

        for piece in self.scenery.furniture:
            if "mesa_chefe.png" in piece.image_path:
                entities.append((MESA_Y, piece.draw))
            elif "tampo_mesa" in piece.image_path:
                entities.append((TAMPO_Y, piece.draw))
            else:
                entities.append((piece.sort_key(), piece.draw))

        # Jogador com Y real
        player_y = self.player.y + self.player.height
        entities.append((player_y, self.player.draw))

        # Chefe com Y fixo
        entities.append((CHEFE_Y, self.boss.draw_sprite))

        entities.sort(key=lambda e: e[0])
        for _, draw_fn in entities:
            draw_fn(self.window)

        # Itens sempre visíveis (acima de tudo)
        for item in self.items:
            if not item.collected:
                item.draw(self.window)

        # Balão + HUD
        self.boss.draw(self.window, self.request)
        self.draw_hud()

        pygame.display.flip()

    # ---------------------------------------------------------

    def run(self):
        running = True

        while running:
            self.clock.tick(FPS)

            self.player.move()
            player_rect = self.player.get_rect()

            # Colisão com paredes
            for wall in WALLS:
                if player_rect.colliderect(wall):
                    self.player.undo_move()
                    player_rect = self.player.get_rect()
                    break

            # Colisão com móveis do cenário (com sprites)
            for mob in self.scenery.furniture:
                if player_rect.colliderect(mob.get_collision()):
                    self.player.undo_move()
                    player_rect = self.player.get_rect()
                    break

            # Colisão com os móveis extras (FURNITURE da Collision.py)
            for furn in FURNITURE:
                if player_rect.colliderect(furn):
                    self.player.undo_move()
                    player_rect = self.player.get_rect()
                    break

            self.boss.update()

            time_left = self.remaining_time()
            if time_left <= 0:
                return "LOSE"
            if self.request.game_finished():
                return "WIN"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                    interaction_rect = self.player.get_interaction_rect()

                    if not self.player.carrying_item:
                        for item in self.items:
                            if item.collected:
                                continue
                            if interaction_rect.colliderect(item.get_rect()):
                                item.collected = True
                                self.player.pick_item(item)
                                break
                    else:
                        if interaction_rect.colliderect(self.boss.get_rect()):
                            if self.request.check_delivery(self.player.current_item):
                                self.boss.show_message("Boa!")
                            else:
                                self.boss.show_message("Eu nao pedi isso!")
                                self.start_time -= (self.time_penalty * 1000)
                                self.reset_item(self.player.current_item)
                            self.player.drop_item()

            self.draw()

        return "LOSE"