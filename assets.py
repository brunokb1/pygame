# assets.py
import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, WIDTH, HEIGHT
from config import PLAYER_WIDTH, PLAYER_HEIGHT, COIN_SIZE, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, BOOST_SIZE

# chaves dos assets
# imagens
BACKGROUND = 'background'
PLAYER_IMG = 'player_img'
MOEDA_IMG = 'moeda_img'
OBSTACULO_IMG = 'obstaculo_img'
CONE_IMG = 'cone_img'
BOOST_IMG = 'boost_img'
LINHA_DE_CHEGADA_IMG = 'linha_de_chegada_img'
TELA_INICIAL_IMG = 'tela_inicial_img'
GAME_OVER_IMG = 'game_over_img'

# sons
MOEDA_SOUND = 'moeda_sound'
CARRO_SOUND = 'boost_sound'
FINISH_SOUND = 'finish_sound'
CRASH_SOUND = 'crash_sound'

# fonte
GAME_FONT = 'game_font'

def load_assets():
    assets = {}

    # Imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'rua_background.png')).convert()
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'car_player.png')).convert_alpha()
    assets[MOEDA_IMG]  = pygame.image.load(os.path.join(IMG_DIR, 'moeda.png')).convert_alpha()
    assets[OBSTACULO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo.png')).convert_alpha()
    assets[CONE_IMG]   = pygame.image.load(os.path.join(IMG_DIR, 'cone.png')).convert_alpha()
    assets[BOOST_IMG]  = pygame.image.load(os.path.join(IMG_DIR, 'boost.png')).convert_alpha()
    assets[LINHA_DE_CHEGADA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'finish_line.png')).convert_alpha()
    assets[TELA_INICIAL_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'tela_inicial.png')).convert_alpha()
    assets[GAME_OVER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'game_over.png')).convert_alpha()

    # Escala 
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[PLAYER_IMG] = pygame.transform.scale(assets[PLAYER_IMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[MOEDA_IMG]  = pygame.transform.scale(assets[MOEDA_IMG], (COIN_SIZE, COIN_SIZE))
    assets[OBSTACULO_IMG] = pygame.transform.scale(assets[OBSTACULO_IMG], (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    assets[CONE_IMG]   = pygame.transform.scale(assets[CONE_IMG], (int(OBSTACLE_WIDTH * 0.75), int(OBSTACLE_HEIGHT * 0.75)))
    assets[BOOST_IMG]  = pygame.transform.scale(assets[BOOST_IMG], (BOOST_SIZE, BOOST_SIZE))
    assets[LINHA_DE_CHEGADA_IMG] = pygame.transform.scale(assets[LINHA_DE_CHEGADA_IMG], (WIDTH, 80))
    assets[TELA_INICIAL_IMG] = pygame.transform.scale(assets[TELA_INICIAL_IMG], (WIDTH, HEIGHT))
    assets[GAME_OVER_IMG] = pygame.transform.scale(assets[GAME_OVER_IMG], (WIDTH, HEIGHT))

    
    # Sons 
    assets[MOEDA_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'moeda.wav'))
    assets[CARRO_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'boost.wav'))
    assets[FINISH_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'finish.wav'))
    assets[CRASH_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'crash.wav'))

    # Fonte
    try:
        assets[GAME_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 20)
    except Exception:
        assets[GAME_FONT] = pygame.font.SysFont(None, 24)

    return assets
