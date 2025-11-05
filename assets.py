import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, WIDTH

# keys dos assets
BACKGROUND = 'background'
PLAYER_IMG = 'player_img'
COIN_IMG = 'coin_img'
TIRE_IMG = 'tire_img'
CAR_OBS_IMG = 'car_obs_img'
CONE_IMG = 'cone_img'
BOOST_IMG = 'boost_img'
FINISH_IMG = 'finish_img'

# sons
COIN_SOUND = 'coin_sound'
BOOST_SOUND = 'boost_sound'
FINISH_SOUND = 'finish_sound'

# fonte
GAME_FONT = 'game_font'

def load_assets():

    assets = {}

    # Imagens 
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'road_background.png')).convert()
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'car_player.png')).convert_alpha()
    assets[COIN_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'coin.png')).convert_alpha()
    assets[TIRE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'tire.png')).convert_alpha()
    assets[CAR_OBS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'car_obstacle.png')).convert_alpha()
    assets[CONE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'cone.png')).convert_alpha()
    assets[BOOST_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'boost.png')).convert_alpha()
    assets[FINISH_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'finish_line.png')).convert_alpha()

    assets[PLAYER_IMG] = pygame.transform.scale(assets[PLAYER_IMG], (64, 128))
    assets[COIN_IMG] = pygame.transform.scale(assets[COIN_IMG], (32, 32))
    assets[TIRE_IMG] = pygame.transform.scale(assets[TIRE_IMG], (64, 64))
    assets[CAR_OBS_IMG] = pygame.transform.scale(assets[CAR_OBS_IMG], (64, 128))
    assets[CONE_IMG] = pygame.transform.scale(assets[CONE_IMG], (48, 64))
    assets[BOOST_IMG] = pygame.transform.scale(assets[BOOST_IMG], (48, 48))
    assets[FINISH_IMG] = pygame.transform.scale(assets[FINISH_IMG], (WIDTH, 80))

    # Sons 
    try:
        assets[COIN_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'coin.wav'))
    except:
        assets[COIN_SOUND] = None
    try:
        assets[BOOST_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'boost.wav'))
    except:
        assets[BOOST_SOUND] = None
    try:
        assets[FINISH_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'finish.wav'))
    except:
        assets[FINISH_SOUND] = None

    # Fonte 
    try:
        assets[GAME_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 20)
    except:
        assets[GAME_FONT] = pygame.font.SysFont(None, 24)

    return assets