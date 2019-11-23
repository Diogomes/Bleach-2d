import pygame as pyg
pyg.init()

win = pyg.display.set_mode((1200,900))

pyg.display.set_caption("Bleach Fight")

walkRight = [pyg.image.load('sprites/ichigo/ichigoWalk_17.png'), pyg.image.load('sprites/ichigo/ichigoWalk_18.png'), pyg.image.load('sprites/ichigo/ichigoWalk_19.png'),
             pyg.image.load('sprites/ichigo/ichigoWalk_20.png'), pyg.image.load('sprites/ichigo/ichigoWalk_21.png'), pyg.image.load('sprites/ichigo/ichigoWalk_22.png'),
             pyg.image.load('sprites/ichigo/ichigoWalk_23.png'), pyg.image.load('sprites/ichigo/ichigoWalk_24.png'), pyg.image.load('sprites/ichigo/ichigoWalk_25.png')]
Esquerda  = [pyg.image.load('sprites/ichigo/ichigoWalk_17.png'), pyg.image.load('sprites/ichigo/ichigoWalk_18.png'), pyg.image.load('sprites/ichigo/ichigoWalk_19.png'),
             pyg.image.load('sprites/ichigo/ichigoWalk_20.png'), pyg.image.load('sprites/ichigo/ichigoWalk_21.png'), pyg.image.load('sprites/ichigo/ichigoWalk_22.png'),
             pyg.image.load('sprites/ichigo/ichigoWalk_23.png'), pyg.image.load('sprites/ichigo/ichigoWalk_24.png'), pyg.image.load('sprites/ichigo/ichigoWalk_25.png')]
jump      = [pyg.image.load('sprites/ichigo/ichigo_jump_47.png'), pyg.image.load('sprites/ichigo/ichigo_jump_48.png'), pyg.image.load('sprites/ichigo/ichigo_jump_49.png'),
             pyg.image.load('sprites/ichigo/ichigo_jump_50.png'), pyg.image.load('sprites/ichigo/ichigo_jump_51.png')]
ichigoStrongAtack = [pyg.image.load('sprites/ichigo/ichigo_StrongAtack_1.png'), pyg.image.load('sprites/ichigo/ichigo_StrongAtack_2.png'),
                     pyg.image.load('sprites/ichigo/ichigo_StrongAtack_3.png'), pyg.image.load('sprites/ichigo/ichigo_StrongAtack_4.png'),
                     pyg.image.load('sprites/ichigo/ichigo_StrongAtack_5.png'), pyg.image.load('sprites/ichigo/ichigo_StrongAtack_6.png'),
                     pyg.image.load('sprites/ichigo/ichigo_StrongAtack_7.png'), pyg.image.load('sprites/ichigo/ichigo_StrongAtack_8.png'),
                     pyg.image.load('sprites/ichigo/ichigo_StrongAtack_9.png')]
ichigo_WeakAtack = [pyg.image.load('sprites/ichigo/ichigo_WeakAtack_1.png'),
                    pyg.image.load('sprites/ichigo/ichigo_WeakAtack_2.png'),
                    pyg.image.load('sprites/ichigo/ichigo_WeakAtack_3.png')]
ichigoRun = [pyg.image.load('sprites/ichigo/ichigoRun_18.png'), pyg.image.load('sprites/ichigo/ichigoRun_19.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_20.png'), pyg.image.load('sprites/ichigo/ichigoRun_21.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_22.png'), pyg.image.load('sprites/ichigo/ichigoRun_23.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_24.png'), pyg.image.load('sprites/ichigo/ichigoRun_25.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_26.png'), pyg.image.load('sprites/ichigo/ichigoRun_27.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_28.png'), pyg.image.load('sprites/ichigo/ichigoRun_29.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_30.png'), pyg.image.load('sprites/ichigo/ichigoRun_31.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_32.png'), pyg.image.load('sprites/ichigo/ichigoRun_33.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_34.png'), pyg.image.load('sprites/ichigo/ichigoRun_35.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_36.png'), pyg.image.load('sprites/ichigo/ichigoRun_37.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_38.png'), pyg.image.load('sprites/ichigo/ichigoRun_39.png'),
                    pyg.image.load('sprites/ichigo/ichigoRun_40.png')]
bg        = pyg.image.load('sprites/ichigo/Academy.png')
char      = pyg.image.load('sprites/ichigo/ichigo_stance_1.png')

clock = pyg.time.Clock()


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
        self.ichigoRun = 20
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
            
        elif self.ichigoRun:
            win.blit(ichigoRun[self.ichigoRun//3], (self.x,self.y))
            
        else:
            win.blit(char, (self.x,self.y))
#---------------------------------------------------------------------------------------------            
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    
    pyg.display.update()


#mainloop
man = player(50, 490, 70,0)
run = True
while run:
    clock.tick(27)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

    keys = pyg.key.get_pressed()


    if keys[pyg.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.ichigoWeakAtack = False
        man.ichigoStrongAtack = False
    elif keys[pyg.K_RIGHT] and man.x < 870 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.ichigoWeakAtack = False
        man.ichigoStrongAtack = False
    elif keys[pyg.K_q]:
        man.right = False
        man.left = False
        man.ichigoStrongAtack = True
        man.ichigoWeakAtack = False

    elif keys[pyg.K_e]:
        man.right = False
        man.left = False
        man.ichigoStrongAtack = False
        man.ichigoWeakAtack = True

    elif keys[pyg.K_w]:
        man.right = False
        man.left = False
        man.ichigoStrongAtack = False
        man.ichigoWeakAtack = True
        
    elif keys[pyg.K_DOWN and pyg.K_RIGHT]:
        man.right = False
        man.left = False
        man.ichigoStrongAtack = False
        man.ichigoWeakAtack = True
        man.ichigoRun = True
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pyg.K_SPACE]:
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

pyg.quit()
