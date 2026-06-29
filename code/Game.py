import pygame

from code.Const import *
from code.Player import Player
from code.Boss import Boss
from code.Item import Item
from code.Request import Request
from code.Collision import COLLIDERS, WALLS
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
            Item("cafe", "assets/itens/cafe.png", (340, 210)),
            Item("caneta", "assets/itens/caneta.png", (45, 205)),
            Item("documentos", "assets/itens/documentos.png", (470, 205)),
            Item("copo", "assets/itens/copo.png", (595, 75)),
            Item("grampeador", "assets/itens/grampeador.png", (65, 70)),
            Item("pasta", "assets/itens/pasta.png", (130, 445))
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

        # 2. Itens
        for item in self.items:
            item.draw(self.window)

        # ==========================================
        # 3. Móveis normais (sem always_front) + jogador
        # ==========================================
        objetos_para_desenhar = []

        # Adiciona móveis que NÃO são always_front
        for mob in self.scenery.furniture:
            if not mob.always_front:
                objetos_para_desenhar.append(mob)

        # Adiciona o jogador
        objetos_para_desenhar.append(self.player)

        # Ordena pelo Y (profundidade)
        def get_bottom(obj):
            if hasattr(obj, 'get_rect'):
                return obj.get_rect().bottom
            else:
                return obj.rect.bottom

        objetos_para_desenhar.sort(key=get_bottom)

        # Desenha tudo (jogador + móveis normais)
        for obj in objetos_para_desenhar:
            obj.draw(self.window)

        # ==========================================
        # 4. Chefe (desenha antes da mesa, se quiser que fique atrás)
        # ==========================================
        self.boss.draw(self.window, self.request)

        # ==========================================
        # 5. Móvel com always_front (mesa do chefe) - DESENHADO POR ÚLTIMO
        # ==========================================
        for mob in self.scenery.furniture:
            if mob.always_front:
                mob.draw(self.window)
                # print("Desenhando móvel sempre_front: ", mob)  # pode remover depois

        # ==========================================
        # 6. HUD (sempre por cima de tudo)
        # ==========================================
        self.draw_hud()

        # ==========================================
        # 7. DEBUG (opcional)
        # ==========================================
        for wall in WALLS:
            pygame.draw.rect(self.window, (255, 0, 0), wall, 2)

        for mob in self.scenery.furniture:
            pygame.draw.rect(self.window, (0, 255, 0), mob.get_collision(), 2)

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

            # Colisão com móveis
            for mob in self.scenery.furniture:
                if player_rect.colliderect(mob.get_collision()):
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
                    player_rect = self.player.get_rect()

                    if not self.player.carrying_item:
                        for item in self.items:
                            if item.collected:
                                continue
                            if player_rect.colliderect(item.get_rect()):
                                item.collected = True
                                self.player.pick_item(item)
                                break
                    else:
                        if player_rect.colliderect(self.boss.get_rect()):
                            if self.request.check_delivery(self.player.current_item):
                                self.boss.show_message("Boa!")
                            else:
                                self.boss.show_message("Eu nao pedi isso!")
                                self.start_time -= (self.time_penalty * 1000)
                                self.reset_item(self.player.current_item)
                            self.player.drop_item()

            self.draw()

        return "LOSE"