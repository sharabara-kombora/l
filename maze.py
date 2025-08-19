#создай игру "Лабиринт"!
from pygame import *
mixer.init()
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.napravleniye = 'left'
    def update(self):
        if self.napravleniye == 'left':
            if self.rect.x > 400:
                self.rect.x -= self.speed
            if self.rect.x <= 400:
                self.napravleniye = 'right'
        if self.napravleniye == 'right':
            if self.rect.x < 600:
                self.rect.x += self.speed
            if self.rect.x >= 600:
                self.napravleniye = 'left'
class Wall(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def wall_reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


mw = display.set_mode((700, 500))
display.set_caption('Лабиринт')
fon = transform.scale(image.load('background.jpg'), (700, 500))

igrok = Player('hero.png', 1, 430, 7)
vrag = Enemy('cyborg.png', 600, 420, 5)
igr = GameSprite('treasure.png', 600, 430, 10)
w1 = Wall((70, 200, 0), 75, 10, 7, 375)
w2 = Wall((70, 200, 0), 75, 10, 600, 7)
w3 = Wall((70, 200, 0), 75, 485, 600, 7)
w4 = Wall((70, 200, 0), 175, 110, 7, 390)
w5 = Wall((70, 200, 0), 275, 10, 7, 190)
w6 = Wall((70, 200, 0), 275, 290, 7, 195)
w7 = Wall((70, 200, 0), 675, 10, 7, 482)
w8 = Wall((70, 200, 0), 275, 290, 240, 7)
w9 = Wall((70, 200, 0), 600, 290, 7, 50)
w10 = Wall((70, 200, 0), 600, 290, 80, 7)
w11 = Wall((70, 200, 0), 515, 95, 7, 202)
w12 = Wall((70, 200, 0), 275, 200, 150, 7)

w_12 = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12]

x1 = 400
x2 = 600


udar = mixer.Sound('kick.ogg')
udar.set_volume(0.15)
money = mixer.Sound('money.ogg')
money.set_volume(0.15)
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.15)
mixer.music.play()
igra = True
clock = time.Clock()
FPS = 60

finish = False
font = font.SysFont('Arial', 70)

while igra:
    for e in event.get():
        if e.type == QUIT:
            igra = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish == True:
                finish = False
                igrok.rect.x = 1
                igrok.rect.y = 430
    mw.blit(fon, (0,0))
    if finish == False:
        igrok.reset()
        igrok.update()
        vrag.reset()
        vrag.update()
        igr.reset()
        w1.wall_reset()
        w2.wall_reset()
        w3.wall_reset()
        w4.wall_reset()
        w5.wall_reset()
        w6.wall_reset()
        w7.wall_reset()
        w8.wall_reset()
        w9.wall_reset()
        w10.wall_reset()
        w11.wall_reset()
        w12.wall_reset()
        w11.wall_reset()
        for w in w_12:
            if sprite.collide_rect(igrok, w):
                udar.play()
                finish = True
                win = font.render('ВЫ ПРОИГРАЛИ!!!', True, (255, 215, 0))    
        if sprite.collide_rect(igrok, vrag):
            udar.play()
            finish = True
            win = font.render('ВЫ ПРОИГРАЛИ!!!', True, (255, 215, 0))
        if sprite.collide_rect(igrok, igr):
            money.play()
            finish = True
            win = font.render('ВЫ ВЫИГРАЛИ!!!', True, (255, 215, 0))
    if finish:
        mw.blit(win, (120, 222))
    clock.tick(FPS)
    display.update()