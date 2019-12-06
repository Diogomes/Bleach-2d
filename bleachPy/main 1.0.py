import pygame
pygame.init()

win = pygame.display.set_mode((1000,600))
pygame.display.set_caption("First Game")

kenpachi_andando_direita  = [pygame.image.load('sprites/kenpachi/WALK_1.png'), 
                          pygame.image.load('sprites/kenpachi/WALK_2.png'), 
                          pygame.image.load('sprites/kenpachi/WALK_3.png'), 
                          pygame.image.load('sprites/kenpachi/WALK_4.png'), 
                          pygame.image.load('sprites/kenpachi/WALK_5.png'), 
                          pygame.image.load('sprites/kenpachi/WALK_6.png')]

kenpachi_andando_esquerda = [pygame.image.load('sprites/kenpachi/WALK_1.png'), 
                                 pygame.image.load('sprites/kenpachi/WALK_2.png'), 
                                 pygame.image.load('sprites/kenpachi/WALK_3.png'), 
                                 pygame.image.load('sprites/kenpachi/WALK_4.png'), 
                                 pygame.image.load('sprites/kenpachi/WALK_5.png'), 
                                 pygame.image.load('sprites/kenpachi/WALK_6.png')]

kenpachi_ataque_fraco = [pygame.image.load('sprites/kenpachi/WEAK_ATTACK_1.png'), 
                         pygame.image.load('sprites/kenpachi/WEAK_ATTACK_2.png'), 
                         pygame.image.load('sprites/kenpachi/WEAK_ATTACK_3.png'), 
                         pygame.image.load('sprites/kenpachi/WEAK_ATTACK_4.png'), 
                         pygame.image.load('sprites/kenpachi/WEAK_ATTACK_5.png')]

ichigo_andando_direita  = [pygame.image.load('sprites/ichigo/ichigowalk_19.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_20.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_21.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_22.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_23.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_24.png'),
                            pygame.image.load('sprites/ichigo/ichigowalk_25.png'),
                            pygame.image.load('sprites/ichigo/ichigowalk_26.png')]

ichigo_andando_esquerda  = [pygame.image.load('sprites/ichigo/ichigowalk_19.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_20.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_21.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_22.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_23.png'), 
                            pygame.image.load('sprites/ichigo/ichigowalk_24.png'),
                            pygame.image.load('sprites/ichigo/ichigowalk_25.png'),
                            pygame.image.load('sprites/ichigo/ichigowalk_26.png')]

ichigo_ataque_fraco      = [pygame.image.load('sprites/ichigo/ichigo_WeakAtack_1.png'),
                            pygame.image.load('sprites/ichigo/ichigo_WeakAtack_2.png'),
                            pygame.image.load('sprites/ichigo/ichigo_WeakAtack_3.png')]

bg = pygame.image.load('sprites/ichigo/Entrance.png')
kenpachiChar = pygame.image.load('sprites/kenpachi/STANCE_2.png')
ichigoChar   = pygame.image.load('sprites/ichigo/ichigo_stance_1.png')
id_controle_1 = pygame.image.load('sprites/ichigo/ichigo_stance_1.png')
id_controle_2 = pygame.image.load('sprites/ichigo/ichigo_stance_1.png')
clock = pygame.time.Clock()



class kenpachi(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isWeakAttack = False
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True
        self.attackCount = 15
        self.weakAttack = False

    def draw(self, win):
        if self.visible:    
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.left:
                win.blit(kenpachi_andando_esquerda[self.walkCount % 3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(kenpachi_andando_direita[self.walkCount % 3], (self.x,self.y))
                self.walkCount +=1
            elif self.weakAttack:
                win.blit(kenpachi_ataque_fraco[self.attackCount % 3], (self.x,self.y))
                self.attackCount +=1
            else:
                win.blit(kenpachiChar, (self.x,self.y))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            
class ichigo(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isWeakAttack = False
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True
        self.attackCount = 15
        self.weakAttack = False

    def draw(self, win):
        if self.visible:    
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.left:
                win.blit(ichigo_andando_esquerda[self.walkCount % 3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(ichigo_andando_direita[self.walkCount % 3], (self.x,self.y))
                self.walkCount +=1
            elif self.weakAttack:
                win.blit(ichigo_ataque_fraco[self.attackCount % 3], (self.x,self.y))
                self.attackCount +=1
            else:
                win.blit(ichigoChar, (self.x,self.y))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


def redrawGameWindow():
    win.blit(bg, (0,0))
    kenpachi.draw(win)
    ichigo.draw(win)
    pygame.display.update()


#mainloop
kenpachi = kenpachi(300, 475, 64,64)
ichigo   = ichigo(600, 475, 64,64)
run = True
while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and kenpachi.x > kenpachi.vel:
        kenpachi.x -= kenpachi.vel
        kenpachi.left = True
        kenpachi.right = False
    elif keys[pygame.K_d] and kenpachi.x < 1000 - kenpachi.width - kenpachi.vel:
        kenpachi.x += kenpachi.vel
        kenpachi.right = True
        kenpachi.left = False
    elif keys[pygame.K_j]:
        kenpachi.right = False
        kenpachi.left = False 
        kenpachi.weakAttack = True
        if kenpachi.hitbox[1] < ichigo.hitbox[1] + ichigo.hitbox[3] and kenpachi.hitbox[1] + kenpachi.hitbox[3] > ichigo.hitbox[1]:
            if kenpachi.hitbox[0] + kenpachi.hitbox[2] > ichigo.hitbox[0] and kenpachi.hitbox[0] < ichigo.hitbox[0] + ichigo.hitbox[2]:
                ichigo.hit()
    elif keys[pygame.K_LEFT] and ichigo.x > ichigo.vel:
        ichigo.x -= ichigo.vel
        ichigo.left = True
        ichigo.right = False
    elif keys[pygame.K_RIGHT] and ichigo.x < 1000 - ichigo.width - ichigo.vel:
        ichigo.x += ichigo.vel
        ichigo.right = True
        ichigo.left = False
    elif keys[pygame.K_KP1]:
        ichigo.right = False
        ichigo.left = False
        ichigo.weakAttack = True
        if ichigo.hitbox[1] < kenpachi.hitbox[1] + kenpachi.hitbox[3] and ichigo.hitbox[1] + ichigo.hitbox[3] > kenpachi.hitbox[1]:
            if ichigo.hitbox[0] + ichigo.hitbox[2] > kenpachi.hitbox[0] and ichigo.hitbox[0] < kenpachi.hitbox[0] + kenpachi.hitbox[2]:
                kenpachi.hit()
    elif keys[pygame.K_KP2]:
        ichigo.right = False
        ichigo.left = False
        ichigo.weakAttack = True
        if ichigo.hitbox[1] < kenpachi.hitbox[1] + kenpachi.hitbox[3] and ichigo.hitbox[1] + ichigo.hitbox[3] > kenpachi.hitbox[1]:
            if ichigo.hitbox[0] + ichigo.hitbox[2] > kenpachi.hitbox[0] and ichigo.hitbox[0] < kenpachi.hitbox[0] + kenpachi.hitbox[2]:
                kenpachi.hit()
    elif keys[pygame.K_KP3]:
        ichigo.right = False
        ichigo.left = False
        ichigo.weakAttack = True
        if ichigo.hitbox[1] < kenpachi.hitbox[1] + kenpachi.hitbox[3] and ichigo.hitbox[1] + ichigo.hitbox[3] > kenpachi.hitbox[1]:
            if ichigo.hitbox[0] + ichigo.hitbox[2] > kenpachi.hitbox[0] and ichigo.hitbox[0] < kenpachi.hitbox[0] + kenpachi.hitbox[2]:
                kenpachi.hit()
    else:
        ichigo.right = False
        ichigo.left = False
        ichigo.weakAttack = False
        ichigo.walkCount = 0
        ichigo.right = False
        ichigo.left = False
        ichigo.weakAttack = False
        ichigo.walkCount = 0    
    
    if not(kenpachi.isJump):
        if keys[pygame.K_SPACE]:
            kenpachi.isJump = True
            kenpachi.right = False
            kenpachi.left = False
            kenpachi.walkCount = 0
    else:
        if kenpachi.jumpCount >= -10:
            neg = 1
            if kenpachi.jumpCount < 0:
                neg = -1
            kenpachi.y -= (kenpachi.jumpCount ** 2) * 0.5 * neg
            kenpachi.jumpCount -= 1
        else:
            kenpachi.isJump = False
            kenpachi.jumpCount = 10
    if not(ichigo.isJump):
        if keys[pygame.K_UP]:
            ichigo.isJump = True
            ichigo.right = False
            ichigo.left = False
            ichigo.walkCount = 0
    else:
        if ichigo.jumpCount >= -10:
            neg = 1
            if ichigo.jumpCount < 0:
                neg = -1
            ichigo.y -= (ichigo.jumpCount ** 2) * 0.5 * neg
            ichigo.jumpCount -= 1
        else:
            ichigo.isJump = False
            ichigo.jumpCount = 10
                    
    redrawGameWindow()

pygame.quit()
