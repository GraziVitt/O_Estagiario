import pygame

from code.Game import Game


pygame.init()

window = pygame.display.set_mode((1024,576))

pygame.display.set_caption("Estagiário em Pânico")

game = Game(window)

game.run()

pygame.quit()