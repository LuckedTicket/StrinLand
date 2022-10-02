import pygame

class Inventory():
    def __init__(self, win) -> None:
        self.selectId = 0
        self.win = win
        self.inventory = ['grass-block', 'sand-block', 'None', 'None', 'None', 'None', 'None', 'None']
        self.slottexture = pygame.image.load('./assets/data/include/interface/slot.png')
        self.slottexture = pygame.transform.scale(self.slottexture, (30, 30))
        self.slottexture.convert_alpha()
        self.slottextureac = pygame.image.load('./assets/data/include/interface/slot-active.png')
        self.slottextureac = pygame.transform.scale(self.slottextureac, (30, 30))
        self.slottextureac.convert_alpha()
        self.font = pygame.font.Font('./assets/data/include/font/intro.otf', 12)

        self._circle_cache = {}

        self.inventoryIDbig = 0
        self.inv1 = pygame.image.load('./assets/data/include/interface/slot.png')
        self.inv1 = pygame.transform.scale(self.inv1, (30, 30))
        self.inv1.convert_alpha()
        self.inv2 = pygame.image.load('./assets/data/include/interface/slot-active.png')
        self.inv2 = pygame.transform.scale(self.inv2, (30, 30))
        self.inv2.convert_alpha()
        self.allBlocksList = ['water-block', 'sand-block', 'grass-block']
        self.isBigInventory = False

    def moveInventroyBig(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.isBigInventory = False
            self.inventory[self.selectId] = self.allBlocksList[self.inventoryIDbig]
        if keys[pygame.K_BACKSPACE]:
            self.isBigInventory = False
            self.inventory[self.selectId] = 'None'
        if keys[pygame.K_RIGHT]:
            if self.inventoryIDbig >= len(self.allBlocksList)-1:
                self.inventoryIDbig = 0
            else: self.inventoryIDbig += 1
        if keys[pygame.K_LEFT]:
            if self.inventoryIDbig <= 0:
                self.inventoryIDbig = len(self.allBlocksList)-1
            else: self.inventoryIDbig -= 1

    def renderBigInventory(self) -> None:
        posItem = 5+30+5+30+30+5+30+5
        for i in range(len(self.allBlocksList)):
            current = pygame.image.load(f'./assets/data/include/items/{self.allBlocksList[i]}.png')
            current = pygame.transform.scale(current, (20, 20))
            current.convert_alpha()
            if i == self.inventoryIDbig:
                self.win.blit(self.inv2, (posItem+5, 5+30+5))
            else:
                self.win.blit(self.inv1, (posItem+5, 5+30+5))
            self.win.blit(current, (posItem+10, 5+30+5+5))
            posItem+=35

    def _circlepoints(self, r):
        r = int(round(r))
        if r in self._circle_cache:
            return self._circle_cache[r]
        x, y, e = r, 0, 1 - r
        self._circle_cache[r] = points = []
        while x >= y:
            points.append((x, y))
            y += 1
            if e < 0:
                e += 2 * y - 1
            else:
                x -= 1
                e += 2 * (y - x) - 1
        points += [(y, x) for x, y in points if x > y]
        points += [(-x, y) for x, y in points if x]
        points += [(x, -y) for x, y in points if y]
        points.sort()
        return points

    def _render(self, text, font:pygame.font.Font, foregrounnd=pygame.Color('white'), outline=(0, 0, 0), opx=2):
        textsurface = font.render(text, False, foregrounnd).convert_alpha()
        w = textsurface.get_width() + 2 * opx
        h = font.get_height()
        osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
        osurf.fill((0, 0, 0, 0))
        surf = osurf.copy()
        osurf.blit(font.render(text, False, outline).convert_alpha(), (0, 0))
        for dx, dy in self._circlepoints(opx):surf.blit(osurf, (dx + opx, dy + opx))
        surf.blit(textsurface, (opx, opx))
        return surf

    def moveSlotByNumbers(self) -> None:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_1]: self.selectId=0
        elif keys[pygame.K_2]: self.selectId=1
        elif keys[pygame.K_3]: self.selectId=2
        elif keys[pygame.K_4]: self.selectId=3
        elif keys[pygame.K_5]: self.selectId=4
        elif keys[pygame.K_6]: self.selectId=5
        elif keys[pygame.K_7]: self.selectId=6
        elif keys[pygame.K_8]: self.selectId=7

    def moveSlot(self) -> None:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.selectId >= len(self.inventory)-1:
                self.selectId = 0
            else: self.selectId += 1
        if keys[pygame.K_LEFT]:
            if self.selectId <= 0:
                self.selectId = len(self.inventory)-1
            else: self.selectId -= 1
    
    def inventoryRender(self) -> None:
        posItem = 5
        for index in range(len(self.inventory)):
            current1 = pygame.image.load(f'./assets/data/include/items/{self.inventory[index]}.png')
            current1 = pygame.transform.scale(current1, (20, 20))
            if index == self.selectId:
                self.win.blit(self.slottextureac, (posItem, 5))
            else:
                self.win.blit(self.slottexture, (posItem, 5))
            self.win.blit(current1, (posItem+5, 10))
            self.win.blit(self._render(f'{index+1}', self.font), (posItem, 5))
            posItem+=30+5