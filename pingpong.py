from pygame import *

BLUE = (200,255,255)


height = 700
width = 900
win = display.set_mode((width,height))
display.set_caption("Пинг-Понг")
win.fill(BLUE)
clock = time.Clock() 
FPS = 40

class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_width, player_heigth, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_heigth))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
	# Метод перерисовки персонажа
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < height - 100:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 

    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < height - 100:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 

class Ball(GameSprite):
    def update(self):
        pass

ball = Ball("ball.png", width/2, height/2, 50, 50, 5)
pl_right = Player("platform.png", 875, 300, 20, 100, 5)
pl_left = Player("platform.png", 5, 300, 20, 100, 5)

game = True
while game:
    win.fill(BLUE)
    ball.reset()
    pl_left.reset()
    pl_right.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.update()
    pl_left.update_left()
    pl_right.update_right()

    display.update()
    clock.tick(FPS)
