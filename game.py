import pygame
import random
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, LANES, LANE_WIDTH, FINISH_DISTANCE
from assets import PLAYER_IMG, BACKGROUND, MOEDA_IMG, BOOST_IMG, OBSTACULO_IMG, CONE_IMG, LINHA_DE_CHEGADA_IMG, GAME_OVER_IMG, VITORIA_IMG

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
        self.spawn_interval =450
        # controle de boost
        self.boost_ativo = False
        self.boost_timer = 0
        self.boost_duracao = 2100 
        self.coin_multiplier = 1
        # contador de moedas
        self.coin_count = 0
        # velocidade base do scroll
        self.scroll_speed = 200 
        # distância percorrida 
        self.distance_travelled = 0
        # posiciona a linha de chegada no mapa 
        finish_img = self.assets.get(LINHA_DE_CHEGADA_IMG)
        if finish_img:
            finish_rect = finish_img.get_rect(topleft=(0, -FINISH_DISTANCE))
            self.finish = {'img': finish_img, 'rect': finish_rect}
        else:
            self.finish = None
        # estado do jogo
        self.game_over = False  
        self.won = False
        # se a linha de chegada já aparece na tela
        self.finish_visible = False
        # limpa os objetos quando a linha aparecer
        self.finish_cleared = False


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Fecha o jogo com segurança
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        # corrigido por ia
        if self.game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.__init__(self.manager)

    #função corrigida pela ia para aumentar a probabilidade de moedas e diminuir a de boosts
    def _spawn_objetos(self):
        choices = ["moeda", "obstaculo", "cone", "boost", None]
        weights = [0.4, 0.2, 0.2, 0.06, 0.14] 
        tipo = random.choices(choices, weights=weights, k=1)[0]

        lane = random.randrange(0, LANES)
        x_center = lane * LANE_WIDTH + LANE_WIDTH // 2
        y = -100

        if tipo == "moeda":
            img = self.assets.get(MOEDA_IMG)
            if img:
                rect = img.get_rect(center=(x_center, y))
                self.moedas.append({"img": img, "rect": rect})

        elif tipo == "boost":
            img = self.assets.get(BOOST_IMG)
            if img:
                rect = img.get_rect(center=(x_center, y))
                self.boosts.append({"img": img, "rect": rect})

        elif tipo == "obstaculo":
            img = self.assets.get(OBSTACULO_IMG)
            if img:
                rect = img.get_rect(center=(x_center, y))
                self.obstaculos.append({"img": img, "rect": rect})

        elif tipo == "cone":
            img = self.assets.get(CONE_IMG)
            if img:
                rect = img.get_rect(center=(x_center, y))
                self.obstaculos.append({"img": img, "rect": rect})
        
    def _ativar_boost(self):
        #UTILIZAÇÃO try dada por ia 
        self.boost_ativo = True
        self.coin_multiplier = 2
        self.boost_timer = pygame.time.get_ticks()
        try:
            som = self.assets.get("boost_sound") or self.assets.get("carro_sound")
            if som:
                som.play()
        except Exception:
            pass

    def _end_game(self, won=False):
        # finaliza a execução do jogo (exibe tela de resultado)
        self.game_over = True
        self.won = won
        # tocar som final 
        if won:
            s = self.assets.get('finish_sound')
        else:
            s = self.assets.get('crash_sound')
        if s:
            s.play()

    def update(self, dt):
        # se o jogo acabou não atualiza mais
        if self.game_over:
            return
        keys = pygame.key.get_pressed()
        self.player.update(dt, keys)
        # movimenta o fundo (scroll)
        self.bg_y += self.scroll_speed * dt
        if self.bg_y >= HEIGHT:
            self.bg_y = 0
        # se a linha já apareceu não spawna novos objetos
        if not self.finish_visible:
            self.spawn_timer += dt * 1000
            if self.spawn_timer > self.spawn_interval:
                self._spawn_objetos()
                self.spawn_timer = 0
        # movimenta obstáculos 
        for obj in self.obstaculos[:]:
            obj["rect"].y += int(self.scroll_speed * dt)
            if obj["rect"].top > HEIGHT:
                self.obstaculos.remove(obj)
            else:
                # checa colisão com jogador (hitboxes reduzidas)
                player_hitbox = self.player.rect.inflate(-PLAYER_WIDTH * 0.45, -PLAYER_HEIGHT * 0.2)
                obj_hitbox = obj["rect"].inflate(-obj["rect"].width * 0.5, -obj["rect"].height * 0.18)
                if obj_hitbox.colliderect(player_hitbox):
                    self._end_game(won=False)
        # movimenta moedas 
        for m in self.moedas[:]:
            m["rect"].y += int(self.scroll_speed * dt)
            if m["rect"].top > HEIGHT:
                self.moedas.remove(m)
            else:
                # hitbox menor para evitar pegar moeda sem encostar (corrigida por ia)
                player_hitbox = self.player.rect.inflate(-PLAYER_WIDTH * 0.35, -PLAYER_HEIGHT * 0.2)
                coin_hitbox = m["rect"].inflate(-m["rect"].width * 0.4, -m["rect"].height * 0.4)
                if coin_hitbox.colliderect(player_hitbox):
                    ganho = self.coin_multiplier
                    self.coin_count += ganho
                    som = self.assets.get('moeda_sound')
                    if som:
                        som.play()
                    self.moedas.remove(m)
        # movimenta boosts
        for b in self.boosts[:]:
            b["rect"].y += int(self.scroll_speed * dt)
            if b["rect"].top > HEIGHT:
                self.boosts.remove(b)
            else:
                player_hitbox = self.player.rect.inflate(-PLAYER_WIDTH * 0.35, -PLAYER_HEIGHT * 0.2)
                boost_hitbox = b["rect"].inflate(-b["rect"].width * 0.4, -b["rect"].height * 0.4)
                if boost_hitbox.colliderect(player_hitbox):
                    self._ativar_boost()
                    self.boosts.remove(b)
        # desativa boost quando tempo acaba
        if self.boost_ativo and pygame.time.get_ticks() - self.boost_timer > self.boost_duracao:
            self.boost_ativo = False
            self.coin_multiplier = 1
        # move a linha junto com o scroll e checa vitória
        if self.finish:
            # move a linha
            self.finish['rect'].y += int(self.scroll_speed * dt)
            # checa se a linha aparece na tela
            if self.finish['rect'].bottom > HEIGHT * 0.25:
                self.finish_visible = True
                # limpa objetos da tela
                if not getattr(self, 'finish_cleared', False):
                    self.obstaculos.clear()
                    self.moedas.clear()
                    self.boosts.clear()
                    self.finish_cleared = True
            # checa vitória
            if self.finish['rect'].top >= self.player.rect.top:
                self._end_game(won=True)


    def draw(self):
        screen = self.manager.screen

        # fundo
        screen.blit(self.background, (0, self.bg_y))
        screen.blit(self.background, (0, self.bg_y - HEIGHT))

        # desenha obstáculos
        for obj in self.obstaculos:
            screen.blit(obj["img"], obj["rect"])

        # desenha finish line se estiver chegando
        if self.finish:
            screen.blit(self.finish['img'], self.finish['rect'])

        # desenha moedas
        for m in self.moedas:
            screen.blit(m["img"], m["rect"])

        # desenha boosts
        for b in self.boosts:
            screen.blit(b["img"], b["rect"])

        # desenha o jogador
        self.player.draw(screen)

        # texto de HUD
        texto_moedas = f"Moedas: {self.coin_count}"
        cor = (255, 255, 0)
        hud = self.font.render(texto_moedas, True, cor)
        screen.blit(hud, (20, 20))

        if self.boost_ativo:
            boost_txt = self.font.render("BOOST ATIVO!", True, (255, 255, 255))
            screen.blit(boost_txt, (20, 50))

        if self.game_over:
            # pega as telas/imagens finais
            if self.won:
                final_img = self.assets.get('vitoria_img')  
            else:
                final_img = self.assets.get('game_over_img')  
            # desenha tela final 
            screen.blit(final_img, (0, 0))
            # escreve número de moedas 
            sub = self.font.render(f"Moedas: {self.coin_count}", True, (255, 255, 0))
            screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))



