#controles player 1

controle_1 = #escolha 1 kenpachi(300, 475, 64,64)
controle_2  = #escolha 2 ichigo(600, 475, 64,64)
run = True
while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and controle_1.x > controle_1.vel:
        controle_1.x -= controle_1.vel
        controle_1.left = True
        controle_1.right = False
    elif keys[pygame.K_d] and controle_1.x < 1000 - controle_1.width - controle_1.vel:
        controle_1.x += controle_1.vel
        controle_1.right = True
        controle_1.left = False
    elif keys[pygame.K_s] and controle_1.x < 1000 - controle_1.width - controle_1.vel:
        controle_1.x += controle_1.vel
        controle_1.right = False
        controle_1.left = False
        controle_1.down = True
    elif keys[pygame.K_j]:
        controle_1.right = False
        controle_1.left = False 
        controle_1.weakAttack = True
        controle_1.strongAttack = False
        controle_1.normalAttack = True
        if controle_1.hitbox[1] < controle_2.hitbox[1] + controle_2.hitbox[3] and controle_1.hitbox[1] + controle_1.hitbox[3] > controle_2.hitbox[1]:
            if controle_1.hitbox[0] + controle_1.hitbox[2] > ichigo.hitbox[0] and controle_1.hitbox[0] < ichigo.hitbox[0] + controle_2.hitbox[2]:
                controle_2.hit()
    elif keys[pygame.K_l]:
        controle_1.right = False
        controle_1.left = False
        controle_1.weakAttack = False
        controle_1.strongAttack = False
        controle_1.normalAttack = True
        if controle_1.hitbox[1] < ichigo.hitbox[1] + ichigo.hitbox[3] and controle_1.hitbox[1] + controle_1.hitbox[3] > ichigo.hitbox[1]:
            if controle_1.hitbox[0] + controle_1.hitbox[2] > ichigo.hitbox[0] and controle_1.hitbox[0] < ichigo.hitbox[0] + ichigo.hitbox[2]:
                ichigo.hit()
    elif keys[pygame.K_l]:
        controle_1.right = False
        controle_1.left = False
        controle_1.weakAttack = False
        controle_1.strongAttack = True
        controle_1.normalAttack = False
        if controle_1.hitbox[1] < ichigo.hitbox[1] + ichigo.hitbox[3] and controle_1.hitbox[1] + controle_1.hitbox[3] > ichigo.hitbox[1]:
            if controle_1.hitbox[0] + controle_1.hitbox[2] > controle_2.hitbox[0] and controle_1.hitbox[0] < ichigo.hitbox[0] + ichigo.hitbox[2]:
                ichigo.hit()
    else:
        if controle_1.jumpCount >= -10:
            neg = 1
            if controle_1.jumpCount < 0:
                neg = -1
            controle_1.y -= (controle_1.jumpCount ** 2) * 0.5 * neg
            controle_1.jumpCount -= 1
        else:
            controle_1.isJump = False
            controle_1.jumpCount = 10
        if not(controle_1.isJump):
        if keys[pygame.K_SPACE]:
            controle_1.isJump = True
            controle_1.right = False
            controle_1.left = False
            controle_1.walkCount = 0
    #controle 2
     keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and controle_1.x > controle_1.vel:
        controle_1.x -= controle_1.vel
        controle_1.left = True
        controle_1.right = False
    elif keys[pygame.K_d] and controle_1.x < 1000 - controle_1.width - controle_1.vel:
        controle_1.x += controle_1.vel
        controle_1.right = True
        controle_1.left = False
    elif keys[pygame.K_s] and controle_1.x < 1000 - controle_1.width - controle_1.vel:
        controle_1.x += controle_1.vel
        controle_1.right = False
        controle_1.left = False
        controle_1.down = True
    elif keys[pygame.K_j]:
        controle_2.right = False
        controle_2.left = False 
        controle_2.weakAttack = True
        controle_2.strongAttack = False
        controle_2.normalAttack = True
        if controle_1.hitbox[1] < ichigo.hitbox[1] + ichigo.hitbox[3] and controle_1.hitbox[1] + controle_1.hitbox[3] > controle_1.hitbox[1]:
            if controle_1.hitbox[0] + controle_1.hitbox[2] > ichigo.hitbox[0] and controle_1.hitbox[0] < controle_1.hitbox[0] + controle_1.hitbox[2]:
                ichigo.hit()
    elif keys[pygame.K_l]:
        controle_2.right = False
        controle_2.left = False
        controle_2.weakAttack = False
        controle_2.strongAttack = False
        controle_2.normalAttack = True
        if controle_1.hitbox[1] < controle_1.hitbox[1] + controle_1.hitbox[3] and controle_1.hitbox[1] + controle_1.hitbox[3] > controle_1.hitbox[1]:
            if controle_1.hitbox[0] + controle_1.hitbox[2] > controle_1.hitbox[0] and controle_1.hitbox[0] < controle_1.hitbox[0] + controle_1.hitbox[2]:
                controle_1.hit()
    elif keys[pygame.K_l]:
        controle_2.right = False
        controle_2.left = False
        controle_2.weakAttack = False
        controle_2.strongAttack = True
        controle_2.normalAttack = False
        if controle_1.hitbox[1] < controle_1.hitbox[1] + controle_1.hitbox[3] and controle_1.hitbox[1] + controle_1.hitbox[3] > controle_1.hitbox[1]:
            if controle_1.hitbox[0] + controle_1.hitbox[2] > controle_1.hitbox[0] and controle_1.hitbox[0] < controle_1.hitbox[0] + controle_1.hitbox[2]:
                controle_1.hit()
    else:
        if controle_2.jumpCount >= -10:
            neg = 1
            if controle_2.jumpCount < 0:
                neg = -1
            controle_2.y -= (controle_2.jumpCount ** 2) * 0.5 * neg
            controle_2.jumpCount -= 1
        else:
            controle_2.isJump = False
            controle_2.jumpCount = 10
        if not(controle_2.isJump):
        if keys[pygame.K_SPACE]:
            controle_2.isJump = True
            controle_2.right = False
            controle_2.left = False
            controle_2.walkCount = 0

    elif keys[pygame.K_j] and controle_2.x > controle_2.vel:
        controle_2.x -= controle_2.vel
        controle_2.left = True
        controle_2.right = False
    elif keys[pygame.K_l] and controle_2.x < 1000 - controle_2.width - controle_2.vel:
        controle_2.x += controle_2.vel
        controle_2.right = True
        controle_2.left = False
    elif keys[pygame.K_w]:
        controle_2.right = False
        controle_2.left = False
        controle_2.weakAttack = True
    else:
        controle_1.right = False
        controle_1.left = False
        controle_1.weakAttack = False
        controle_1.walkCount = 0
        controle_2.right = False
        controle_2.left = False
        controle_2.weakAttack = False
        controle_2.walkCount = 0    
    
    
    else:
        if controle_1.jumpCount >= -10:
            neg = 1
            if controle_1.jumpCount < 0:
                neg = -1
            controle_1.y -= (controle_1.jumpCount ** 2) * 0.5 * neg
            controle_1.jumpCount -= 1
        else:
            controle_1.isJump = False
            controle_1.jumpCount = 10
                    
    redrawGameWindow()

pygame.quit()
