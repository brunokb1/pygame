
import pygame
from config import WIDTH, HEIGHT, FPS
from assets import load_assets
from game import GameScreen

def main():
    pygame.init()
    # cria janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Velozes e Furiosos")
    # carrega assets (imagens e sons)
    assets = load_assets()
    # mostra tela inicial (corrigido por ia)
    tela_ini = assets.get('tela_inicial_img')
    if tela_ini:
        screen.blit(tela_ini, (0,0))
        pygame.display.flip()
        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        waiting = False 
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
    # clock para FPS
    clock = pygame.time.Clock()
    # cria tela do jogo
    manager = type("Manager", (), {})()  
    manager.screen = screen
    manager.assets = assets
    # cria GameScreen
    game_screen = GameScreen(manager)
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game_screen.handle_event(event)
        # lógica e renderização
        game_screen.update(dt)
        game_screen.draw()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

