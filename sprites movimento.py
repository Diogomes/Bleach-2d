#movendo sprites

class Player(pg.sprite.Sprite):
def __init__(self, game, x, y):
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = pg.Surface((tilesize, tilesize))
    self.image.fill(yellow)
    self.rect = self.image.get_rect()
    self.vx, self.vy = 0, 0
    self.x = x * tilesize
    self.y = y * tilesize

def get_keys(self):
    self.vx, self.vy = 0, 0
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        self.vx = -playerspeed
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        self.vx = playerspeed
    if keys[pg.K_UP] or keys[pg.K_w]:
        self.vy = -playerspeed
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        self.vy = playerspeed
    if self.vx != 0 and self.vy != 0:
        self.vx *= 0.7071
        self.vy *= 0.7071

def collide_with_walls(self, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.vx > 0:
                self.x = hits[0].rect.left - self.rect.width
            if self.vx < 0:
                self.x = hits[0].rect.right
            self.vx = 0
            self.rect.x = self.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.vy > 0:
                self.y = hits[0].rect.top - self.rect.height
            if self.vy < 0:
                self.y = hits[0].rect.bottom
            self.vy = 0
            self.rect.y = self.y

def update(self):
    self.get_keys()
    self.x += self.vx * self.game.dt
    self.y += self.vy * self.game.dt
    self.rect.x = self.x
    self.collide_with_walls('x')
    self.rect.y = self.y
    self.collide_with_walls('y')
