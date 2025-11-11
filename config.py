from os import path

# Pastas de assets 
BASE_DIR = path.dirname(__file__)
IMG_DIR = path.join(BASE_DIR, 'assets', 'img')
SND_DIR = path.join(BASE_DIR, 'assets', 'snd')
FNT_DIR = path.join(BASE_DIR, 'assets', 'font')

# Tela
WIDTH = 480
HEIGHT = 700

# Jogo
FPS = 60
LANES = 3  
LANE_WIDTH = WIDTH // LANES

# Tamanhos 
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 128

COIN_SIZE = 50
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = 70
BOOST_SIZE = 60

# Scroll 
BASE_SCROLL_SPEED = 5  
BOOST_SPEED = 12       
BOOST_DURATION_MS = 1500

# Distância da corrida 
FINISH_DISTANCE = 5000  

# Cores
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)