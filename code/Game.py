import pygame

from code.Const import *
from code.Player import Player
from code.Boss import Boss
from code.Item import Item
from code.Request import Request


class Game:

    def __init__(self, window):

        self.window = window

        self.clock = pygame.time.Clock()

        self.player = Player()
        self.boss = Boss()
        self.request = Request()

        self.items = [

            Item("cafe"),

            Item("caneta"),

            Item("documentos"),

            Item("copo"),

            Item("grampeador"),

            Item("pasta")

        ]

        self.delivered_items = 0

        self.start_time = pygame.time.get_ticks()

        self.background = pygame.image.load(
            "assets/background/escritorio.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.font = pygame.font.SysFont(None, 36)

    def run(self):

        running = True

        while running:

            self.clock.tick(FPS)

            elapsed = (
                              pygame.time.get_ticks()
                              - self.start_time
                      ) // 1000

            time_left = 40 - elapsed

            # DERROTA
            if time_left <= 0:
                print("DERROTA!")

                running = False

            # VITÓRIA
            if self.delivered_items >= 6:
                print("VITORIA!")

                running = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        player_rect = pygame.Rect(
                            self.player.x,
                            self.player.y,
                            self.player.width,
                            self.player.height
                        )

                        # PEGAR ITEM
                        if not self.player.carrying_item:

                            for item in self.items:

                                if not item.collected:

                                    if player_rect.colliderect(
                                            item.get_rect()):
                                        item.collected = True

                                        self.player.carrying_item = True

                                        self.player.current_item = item.nome

                                        print("Pegou:", item.nome)

                                        break

                        # ENTREGAR ITEM
                        else:

                            if player_rect.colliderect(
                                    self.boss.get_rect()):
                                print("Entregou:", self.player.current_item)

                                self.player.carrying_item = False

                                self.player.current_item = None

                                self.delivered_items += 1

                                print(
                                    "ITEM ENTREGUE:",
                                    self.delivered_items
                                )

            self.player.move()

            self.window.blit(
                self.background,
                (0, 0)
            )

            self.player.draw(
                self.window
            )

            self.boss.draw(
                self.window,
                self.request
            )

            for item in self.items:
                item.draw(
                    self.window
                )

            timer_text = self.font.render(
                f"Tempo: {time_left}",
                True,
                WHITE
            )

            self.window.blit(
                timer_text,
                (20, 20)
            )

            delivery_text = self.font.render(
                f"Entregues: {self.delivered_items}/6",
                True,
                WHITE
            )

            self.window.blit(
                delivery_text,
                (20, 60)
            )

            if self.player.carrying_item:
                carry_text = self.font.render(
                    "CARREGANDO ITEM",
                    True,
                    YELLOW
                )

                self.window.blit(
                    carry_text,
                    (20, 100)
                )

            pygame.display.flip()
