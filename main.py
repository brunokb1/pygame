
import pygame
from config import WIDTH, HEIGHT, FPS
from assets import load_assets
from game import GameScreen

def main():
    pygame.init()
    # cria janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Veloses e Furiosos")
    # carrega assets (imagens e sons)
    assets = load_assets()
    # clock para FPS
    clock = pygame.time.Clock()
    # cria tela do jogo
    manager = type("Manager", (), {})()  # cria um objeto vazio para segurar 'screen' e 'assets'
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

