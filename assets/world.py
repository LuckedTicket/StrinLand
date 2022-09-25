import pygame
from utils.settings import *

class World():
    def __init__(self, win:pygame.display.set_mode) -> None:
        self.win = win
        self.world = []
        self.cellSize = scale
        self.worldWidth, self.worldHeight = geometry[0]//self.cellSize, geometry[1]//self.cellSize
        for row in range(self.worldHeight):
            line = []
            for col in range(self.worldWidth):
                line.append('water-block')
            self.world.append(line)
        
        self.grassblock = pygame.image.load('./assets/data/include/grass-block.png').convert()
        self.grassblock = pygame.transform.scale(self.grassblock, (scale, scale)).convert()
        self.grassblock.convert_alpha()

        self.waterblock = pygame.image.load('./assets/data/include/water-block.png').convert()
        self.waterblock = pygame.transform.scale(self.waterblock, (scale, scale)).convert()
        self.waterblock.convert_alpha()

        self.sandblock = pygame.image.load('./assets/data/include/sand-block.png').convert()
        self.sandblock = pygame.transform.scale(self.sandblock, (scale, scale)).convert()
        self.sandblock.convert_alpha()
    
    def render(self) -> None:
        for row in range(self.worldHeight):
            for col in range(self.worldWidth):
                x, y = col*self.cellSize, row*self.cellSize
                if self.world[row][col] == 'grass-block':
                    self.win.blit(self.grassblock, (x, y))
                elif self.world[row][col] == 'sand-block':
                    self.win.blit(self.sandblock, (x, y))
                elif self.world[row][col] == 'water-block':
                    self.win.blit(self.waterblock, (x, y))
                else:
                    self.win.blit(self.waterblock, (x, y))
    
    def build(self, block:str) -> None:
        if block!='None':
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseLeft, mouseCenter, mouseRight = pygame.mouse.get_pressed()
            mouseRow, mouseCol = mouseX//self.cellSize, mouseY//self.cellSize
            pygame.draw.rect(self.win, (0, 0, 0), (mouseRow*self.cellSize, mouseCol*self.cellSize, scale, scale), outline)
            if mouseLeft: 
                self.world[mouseCol][mouseRow] = block
            elif mouseRight: 
                self.world[mouseCol][mouseRow] = 'water-block'