import pygame

class InterFace():
    def __init__(self, win) -> None:
        self.win = win
        self.mouse = pygame.image.load('./assets/data/include/interface/slot.png')
        self.mouse = pygame.transform.scale(self.mouse, (20, 20))
        self.mouse.convert_alpha()

    def mouseRender(self) -> None:
        pygame.mouse.set_visible(False)
        mouseX, mouseY = pygame.mouse.get_pos()
        self.win.blit(self.mouse, (mouseX-10, mouseY-10))