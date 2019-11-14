import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('sprites/ichigo/ichigoWalk_17.png'), pygame.image.load('sprites/ichigo/ichigoWalk_18.png'), pygame.image.load('sprites/ichigo/ichigoWalk_19.png'), pygame.image.load('sprites/ichigo/ichigoWalk_20.png'), pygame.image.load('sprites/ichigo/ichigoWalk_21.png'), pygame.image.load('sprites/ichigo/ichigoWalk_22.png'), pygame.image.load('sprites/ichigo/ichigoWalk_23.png'), pygame.image.load('sprites/ichigo/ichigoWalk_24.png'), pygame.image.load('sprites/ichigo/ichigoWalk_25.png')]
walkLeft  = [pygame.image.load('sprites/ichigo/ichigoWalk_17.png'), pygame.image.load('sprites/ichigo/ichigoWalk_18.png'), pygame.image.load('sprites/ichigo/ichigoWalk_19.png'), pygame.image.load('sprites/ichigo/ichigoWalk_20.png'), pygame.image.load('sprites/ichigo/ichigoWalk_21.png'), pygame.image.load('sprites/ichigo/ichigoWalk_22.png'), pygame.image.load('sprites/ichigo/ichigoWalk_23.png'), pygame.image.load('sprites/ichigo/ichigoWalk_24.png'), pygame.image.load('sprites/ichigo/ichigoWalk_25.png')]
jump      = [pygame.image.load('sprites/ichigo/ichigo_jump_47.png'), pygame.image.load('sprites/ichigo/ichigo_jump_48.png'), pygame.image.load('sprites/ichigo/ichigo_jump_49.png'), pygame.image.load('sprites/ichigo/ichigo_jump_50.png'), pygame.image.load('sprites/ichigo/ichigo_jump_51.png')]
ichigoStrongAtack = [pygame.image.load('sprites/ichigo/ichigo_StrongAtack_1.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_2.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_3.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_4.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_5.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_6.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_7.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_8.png'), pygame.image.load('sprites/ichigo/ichigo_StrongAtack_9.png')]
ichigo_WeakAtack = [pygame.image.load('sprites/ichigo/ichigo_WeakAtack_1.png'),pygame.image.load('sprites/ichigo/ichigo_WeakAtack_2.png'),pygame.image.load('sprites/ichigo/ichigo_WeakAtack_3.png')]
bg        = pygame.image.load('sprites/ichigo/bg.png')
char      = pygame.image.load('sprites/ichigo/ichigo_stance_1.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.ichigoStrongAtack = False
        self.ichigoWeakAtack = False
        self.walkCount = 0
        self.jumpCount = 10
        self.strongAtack = 9
        self.weakAtack = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        
        elif self.isJump:
            win.blit(jump[self.walkCount//3], (self.x,self.y))
        
        elif self.ichigoStrongAtack:
            win.blit(ichigoStrongAtack[self.strongAtack//3], (self.x,self.y))
        
        elif self.ichigoWeakAtack:
            win.blit(ichigo_WeakAtack[self.weakAtack//3], (self.x,self.y))
            
        else:
            win.blit(char, (self.x,self.y))
#---------------------------------------------------------------------------------------------            
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.ichigoWeakAtack = False
        man.ichigoStrongAtack = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.ichigoWeakAtack = False
        man.ichigoStrongAtack = False
    elif keys[pygame.K_q]:
        man.right = False
        man.left = False
        man.ichigoStrongAtack = True
        man.ichigoWeakAtack = False

    elif keys[pygame.K_w]:
        man.right = False
        man.left = False
        man.ichigoStrongAtack = False
        man.ichigoWeakAtack = True
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
