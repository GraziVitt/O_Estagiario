import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Game import Game
from code.Victory import Victory
from code.Defeat import Defeat


pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Estagiário em Pânico")

menu = Menu(window)
victory_screen = Victory(window)
defeat_screen = Defeat(window)

state = "MENU"

while True:

    if state == "MENU":

        menu.run()  # mostra o menu até o jogador clicar em "Jogar"

        state = "GAME"

    elif state == "GAME":

        game = Game(window)  # novo jogo: zera tempo, itens e pedidos

        result = game.run()  # "WIN" ou "LOSE"

        state = "WIN" if result == "WIN" else "LOSE"

    elif state == "WIN":

        choice = victory_screen.run()  # "RESTART" ou "MENU"

        state = "GAME" if choice == "RESTART" else "MENU"

    elif state == "LOSE":

        choice = defeat_screen.run()  # "RESTART" ou "MENU"

        state = "GAME" if choice == "RESTART" else "MENU"