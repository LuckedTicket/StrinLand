import pygame
from utils.settings import *

class Player():
    def __init__(self, win:pygame.display.set_mode) -> None:
        self.x = 0
        self.y = 0
        self.speed = 5
        self.win = win
        self.facingRight = True
        self.playerTexture = pygame.image.load('./assets/data/include/player-texture.png')
        self.playerTexture=pygame.transform.scale(self.playerTexture, (scale, scale))
        self.playerTexture=self.playerTexture.convert_alpha()
        
    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y >= 0: self.y-=self.speed
        if keys[pygame.K_s] and self.y <= geometry[1]-scale: self.y+=self.speed
        if keys[pygame.K_a] and self.x >= 0: self.x-=self.speed; self.facingRight = False
        if keys[pygame.K_d] and self.x <= geometry[0]-scale: self.x+=self.speed; self.facingRight=True

    def render(self, hand:str) -> None:
        self.win.blit(self.playerTexture, (self.x, self.y))
        if self.facingRight:
            self.handblock = pygame.image.load(f'./assets/data/include/{hand}.png')
            self.handblock=pygame.transform.scale(self.handblock, (8, 8))
            self.handblock=self.handblock.convert_alpha()
            self.win.blit(self.handblock, (self.x+15, self.y+10))
        else:
            self.handblock = pygame.image.load(f'./assets/data/include/{hand}.png')
            self.handblock=pygame.transform.scale(self.handblock, (8, 8))
            self.handblock=self.handblock.convert_alpha()
            self.win.blit(self.handblock, (self.x-3, self.y+10))