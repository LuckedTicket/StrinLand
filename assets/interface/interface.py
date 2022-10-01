import pygame

class InterFace():
    def __init__(self, win) -> None:
        self.win = win
        self.mouse = pygame.image.load('./assets/data/include/interface/slot.png')
        self.mouse = pygame.transform.scale(self.mouse, (20, 20))
        self.mouse.convert_alpha()
        self.pauserButtons = ['Continue', 'Settings', 'MainMenu']
        self.button = pygame.image.load('./assets/data/include/interface/slot.png')
        self.button = pygame.transform.scale(self.button, (200, 40))
        self.button.convert_alpha()
        self.buttonActive = pygame.image.load('./assets/data/include/interface/slot-active.png')
        self.buttonActive = pygame.transform.scale(self.buttonActive, (200, 40))
        self.buttonActive.convert_alpha()
        self.font = pygame.font.Font('./assets/data/include/font/intro.otf', 16)
        self.buttonSelectId = 0
        self._circle_cache = {}
        self.isPause = False

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

    def mouseRender(self) -> None:
        pygame.mouse.set_visible(False)
        mouseX, mouseY = pygame.mouse.get_pos()
        self.win.blit(self.mouse, (mouseX-10, mouseY-10))

    def moveButtons(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if self.buttonSelectId >= len(self.pauserButtons) - 1:
                self.buttonSelectId = 0
            else:
                self.buttonSelectId += 1
        if keys[pygame.K_UP]:
            if self.buttonSelectId <= 0:
                self.buttonSelectId = len(self.pauserButtons) - 1
            else:
                self.buttonSelectId -= 1
    
    def selectEnter(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if self.pauserButtons[self.buttonSelectId] == 'Continue':
                self.isPause = False

    def renderButtons(self) -> None:
        posItem=100
        for index in range(len(self.pauserButtons)):
            if index == self.buttonSelectId:
                self.win.blit(self.buttonActive, (720//2-200//2, posItem+40))
            else:
                self.win.blit(self.button, (720//2-200//2, posItem+40))
            self.win.blit(self._render(self.pauserButtons[index], self.font), (720//2-200//2+40+11, posItem+40+11))
            posItem+=40+10