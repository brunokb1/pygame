import pygame
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
from assets import PLAYER_IMG, BACKGROUND


class Jogador:

    def __init__(self, manager):
        # guarda referência ao gerenciador (para acessar assets)
        self.manager = manager
        self.image = self.manager.assets[PLAYER_IMG]
        self.rect = self.image.get_rect()
        # posiciona o carro no centro da tela, um pouco acima da base
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 50
        # velocidade de movimento (px/s)
        self.speed = 300

    def update(self, dt, keys):
        #Atualiza posição horizontal do carro com base nas teclas.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed * dt
        # impede sair da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, surface):
        #desenha o carro
        surface.blit(self.image, self.rect)

