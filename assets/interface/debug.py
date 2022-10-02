import pygame
import interface.interface as inf

class DebugLayer():
    def __init__(self, win) -> None:
        self.win = win
        self.inteface = inf.InterFace(self.win)
        self.font = pygame.font.Font('./assets/data/include/font/intro.otf', 12)

    def renderDebugText(self, dict:dict) -> None:
        '''
        [debug.engine.fps], [debug.player.pos], [debug.player.speed]
        '''
        textDebugExemple = f'FPS: {dict["debug.engine.fps"]}\nX: {dict["debug.player.pos"][0]}, Y: {dict["debug.player.pos"][1]}'
        textDebugExemple1 = f'speed: {dict["debug.player.speed"]}'
        self.win.blit(self.inteface._render(textDebugExemple, self.font), (0+5, 5+30+5))
        self.win.blit(self.inteface._render(textDebugExemple1, self.font), (0+5, 5+30+5+15))