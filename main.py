
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))
pygame.display.set_caption("Veloses e Furiosos")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
