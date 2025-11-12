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
PLAYER_WIDTH = max(48, LANE_WIDTH - 50)      
PLAYER_HEIGHT = int(PLAYER_WIDTH * 1.9)     

COIN_SIZE = int(LANE_WIDTH * 0.7)            
OBSTACLE_WIDTH = int(LANE_WIDTH * 0.6)        
OBSTACLE_HEIGHT = OBSTACLE_WIDTH
BOOST_SIZE = int(LANE_WIDTH * 0.45)

# velocidade Scroll 
BASE_SCROLL_SPEED = 200    
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
