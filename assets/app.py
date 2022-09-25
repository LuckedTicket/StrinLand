import pygame
import player as pl
import world as wr
import interface.inventory as inv
from interface.interface import *
from utils.settings import *
from utils.until import *

pygame.init()
loaddict = LoadLatest()

win = pygame.display.set_mode((geometry[0], geometry[1]))
win.convert_alpha()
win.convert()
pygame.display.set_caption(title)

fps = pygame.time.Clock()

player = pl.Player(win)
player.x, player.y = loaddict['player.pos'][0], loaddict['player.pos'][1]
world = wr.World(win)
world.world = loaddict['player.world']
inventoryUI = inv.Inventory(win)
inteface = InterFace(win)

bgui = pygame.image.load('./assets/data/include/interface/background.png').convert_alpha()


isPause = False
run = True
while run:
    win.fill((0, 0, 0))
    fps.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        inventoryUI.moveSlot()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and not isPause: isPause = True
        elif keys[pygame.K_ESCAPE] and isPause: isPause = False

    world.render()
    if not isPause:
        world.build(inventoryUI.inventory[inventoryUI.selectId])
        player.movement()
    player.render(inventoryUI.inventory[inventoryUI.selectId])
    
    inventoryUI.inventoryRender()
    inteface.mouseRender()

    if isPause:
        win.blit(bgui, (0, 0))
    pygame.display.update()
SaveLatest({
    "app.version": title,
    "player.pos": [
        player.x,
        player.y
    ],
    "player.world": world.world
})
pygame.quit()