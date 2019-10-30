import pygame as pyg

def main():
    pyg.init()
    tela = pyg.display.set_mode([800, 800])
    pyg.display.set_caption("Bleach Inicio")
    relogio = pyg.time.Clock()
    cor_branca = (255,255,255)
    sup = pyg.Surface((100, 100))
    
    sair = False

    while sair != True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                sair = True
                
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    sup.move_ip(-10,0)
                if event.key == pyg.K_RIGHT:
                    sup.move_ip(10,0)
                if event.key == pyg.K_UP:
                    sup.move_ip(0,-10)
                if event.key == pyg.K_DOWN:
                    sup.move_ip(0,10)
        relogio.tick(28)
        tela.fill(cor_branca)
        tela.blit(sup, (50, 50))
        pyg.display.update()
    pyg.quit()
main()
