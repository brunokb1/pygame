import pygame
import random
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
from assets import PLAYER_IMG, BACKGROUND


class Player:

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

class GameScreen:
    def __init__(self, manager):
        self.manager = manager
        self.assets = manager.assets
        # carrega fonte (caso precise escrever algo, recomendado ser feito nas referencias)
        try:
            self.font = self.assets['game_font']
        except:
            self.font = pygame.font.SysFont(None, 24)
        # fundo (imagem da rua)
        self.background = self.assets[BACKGROUND]
        self.bg_y = 0 
        # cria o player
        self.player = Player(manager)
        # listas para armazenar entidades do jogo
        self.obstaculos = []   
        self.boosts = []       
        self.moedas = []       
        # controle de spawn
        self.spawn_timer = 0
        self.spawn_interval = 1200  
        # controle de boost
        self.boost_ativo = False
        self.boost_timer = 0
        self.boost_duracao = 1500  
        # contador de moedas
        self.coin_count = 0
        # velocidade base do scroll
        self.scroll_speed = 200 
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
            # Fecha o jogo com segurança
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player.update(dt, keys)

    def draw(self):
        #desenha a tela
        screen = self.manager.screen
        # desenha o fundo
        screen.blit(self.background, (0, 0))
        # desenha o carro
        self.player.draw(screen)
        # texto de instrução
        text = self.font.render("Use ← → para mover | ESC volta", True, (255, 255, 255))
        screen.blit(text, (20, 20))

