import pygame as pyg

def main():
    pyg.init()
    tela = pyg.display.set_mode([500, 500])
    pyg.display.set_caption("Bleach Inicio")
    relogio = pyg.time.Clock()
    cor_branca = (255,255,255)
    cor_preta = (100,100,100)
    sup = pyg.Surface((100, 100))
    sup2 = pyg.Surface((50,50))
    sup2.fill(cor_preta)
    
    ret = pyg.Rect (10, 10, 45, 45)
    
    sair = False

    while sair != True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                sair = True
            #if event.type ==pyg.MOUSEBUTTONDOWN:
                
'''
Butões interação com o personagem
'''
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    ret.move_ip(-10,0)
                if event.key == pyg.K_RIGHT:
                    ret.move_ip(10,0)
                if event.key == pyg.K_UP:
                    ret.move_ip(0,-10)
                if event.key == pyg.K_DOWN:
                    ret.move_ip(0,10)
                #if event.key == pyg.K_w:
                    #ret.move_ip(0,10)
                #if event.key == pyg.K_a:
                    #ret.move_ip(0,10)
                #if event.key == pyg.K_d:
                    #ret.move_ip(0,10)
                #if event.key == pyg.K_s:
                    #ret.move_ip(0,10)
                #if event.key == pyg.K_j:
                    #ret.move_ip(0,10)
                #if event.key == pyg.K_i:
                    #ret.move_ip(0,10)
                #if event.key == pyg.K_l:
                    #ret.move_ip(0,10)
        relogio.tick(28)
        tela.fill(cor_branca)
        tela.blit(sup, (50, 50))
        tela.blit(sup2,[10, 10])
        pyg.draw.rect(tela, cor_preta, ret)
        pyg.display.update()
    pyg.quit()
main()
