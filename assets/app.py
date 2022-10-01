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
inventoryUI.inventory = loaddict['player.inventory']
inteface = InterFace(win)

bgui = pygame.image.load('./assets/data/include/interface/background.png').convert_alpha()

inventoryIDbig = 0
inv1 = pygame.image.load('./assets/data/include/interface/slot.png')
inv1 = pygame.transform.scale(inv1, (30, 30))
inv1.convert_alpha()
inv2 = pygame.image.load('./assets/data/include/interface/slot-active.png')
inv2 = pygame.transform.scale(inv2, (30, 30))
inv2.convert_alpha()
allBlocksList = ['water-block', 'sand-block', 'grass-block']
isBigInventory = False

run = True
while run:
    win.fill((0, 0, 0))
    fps.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if not inteface.isPause and not isBigInventory:
            inventoryUI.moveSlotByNumbers()
            inventoryUI.moveSlot()
        if isBigInventory: 
            inventoryUI.moveSlotByNumbers()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and not isBigInventory and not inteface.isPause: inteface.isPause = True
        elif keys[pygame.K_ESCAPE] and inteface.isPause: inteface.isPause = False
        if keys[pygame.K_LSHIFT] and not isBigInventory: isBigInventory = True
        elif keys[pygame.K_LSHIFT] and isBigInventory: isBigInventory = False
        inteface.moveButtons()
        inteface.selectEnter()
        if isBigInventory:
            if keys[pygame.K_RETURN]:
                inventoryUI.inventory[inventoryUI.selectId] = allBlocksList[inventoryIDbig]
            if keys[pygame.K_BACKSPACE]:
                inventoryUI.inventory[inventoryUI.selectId] = 'None'
            if keys[pygame.K_RIGHT]:
                if inventoryIDbig >= len(allBlocksList)-1:
                    inventoryIDbig = 0
                else: inventoryIDbig += 1
            if keys[pygame.K_LEFT]:
                if inventoryIDbig <= 0:
                    inventoryIDbig = len(allBlocksList)-1
                else: inventoryIDbig -= 1

    world.render()
    if not inteface.isPause:
        world.build(inventoryUI.inventory[inventoryUI.selectId])
        player.movement()
    player.render(inventoryUI.inventory[inventoryUI.selectId])

    posItem = 5+30+5+30
    if isBigInventory:
        win.blit(bgui, (0, 0))
        for i in range(len(allBlocksList)):
            current = pygame.image.load(f'./assets/data/include/{allBlocksList[i]}.png')
            current = pygame.transform.scale(current, (20, 20))
            current.convert_alpha()
            if i == inventoryIDbig:
                win.blit(inv2, (posItem+5, 5+30+5))
            else:
                win.blit(inv1, (posItem+5, 5+30+5))
            win.blit(current, (posItem+10, 5+30+5+5))
            posItem+=35
    inventoryUI.inventoryRender()
    if inteface.isPause:
        win.blit(bgui, (0, 0))
        inteface.renderButtons()

    inteface.mouseRender()
    pygame.display.update()
SaveLatest({
    "app.version": title,
    "player.pos": [
        player.x,
        player.y
    ],
    "player.inventory": inventoryUI.inventory,
    "player.world": world.world
})
pygame.quit()