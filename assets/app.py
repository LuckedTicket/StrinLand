import pygame
import player as pl
import world as wr
import interface.inventory as inv
from interface.interface import *
from utils.settings import *
from utils.until import *
from interface.debug import *

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
debug = DebugLayer(win)

bgui = pygame.image.load('./assets/data/include/interface/background.png').convert_alpha()

isDebug = False
run = True
while run:
    win.fill((0, 0, 0))
    fps.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if not inteface.isPause and not inventoryUI.isBigInventory:
            inventoryUI.moveSlotByNumbers()
            inventoryUI.moveSlot()
        if inventoryUI.isBigInventory: 
            inventoryUI.moveSlotByNumbers()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and not inventoryUI.isBigInventory and not inteface.isPause: inteface.isPause = True
        elif keys[pygame.K_ESCAPE] and inteface.isPause: inteface.isPause = False
        if keys[pygame.K_q] and not isDebug: isDebug = True
        elif keys[pygame.K_q] and isDebug: isDebug = False
        if keys[pygame.K_e] and not inventoryUI.isBigInventory and not inteface.isPause: inventoryUI.isBigInventory = True
        elif keys[pygame.K_e] and inventoryUI.isBigInventory: inventoryUI.isBigInventory = False
        inteface.moveButtons()
        inteface.selectEnter()
        if inventoryUI.isBigInventory:
            inventoryUI.moveInventroyBig()

    world.render()
    if not inteface.isPause:
        world.build(inventoryUI.inventory[inventoryUI.selectId])
        player.movement()
    player.render(inventoryUI.inventory[inventoryUI.selectId])

    if isDebug:
        debug.renderDebugText({
            'debug.engine.fps': int(fps.get_fps()),
            'debug.player.pos': [player.x//scale, player.y//scale],
            "debug.player.speed": player.speed
            })
    if inventoryUI.isBigInventory:
        inventoryUI.renderBigInventory()
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