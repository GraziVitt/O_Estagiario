import pygame

from code.Menu import Menu

pygame.init()

window = pygame.display.set_mode(

    (1024, 576)

)

pygame.display.set_caption(

    "O Estagiário"

)

menu = Menu(window)

option = menu.run()
print(option)
