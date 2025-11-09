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

