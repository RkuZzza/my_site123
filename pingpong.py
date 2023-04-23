from pygame import *
from time import sleep

BLUE = (200,255,255)


height = 700
width = 900
win = display.set_mode((width,height))
display.set_caption("Пинг-Понг")
win.fill(BLUE)
clock = time.Clock() 
FPS = 80

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

font.init()
font1 = font.SysFont("Tahoma", 40)
num_right = 0
num_left = 0
right = font1.render(str(num_right), True, (0,0,0))
left = font1.render(str(num_left), True, (0,0,0))

ball = GameSprite("ball.png", width/2, height/2, 50, 50, 5)
pl_right = Player("platform.png", 875, 300, 20, 100, 5)
pl_left = Player("platform.png", 5, 300, 20, 100, 5)

ball_vx = ball.speed
ball_vy = ball.speed

finish = False
game = True
while game:
    win.fill(BLUE)
    ball.reset()
    pl_left.reset()
    pl_right.reset()
    win.blit(right,(250, 20))
    win.blit(left,(400, 20))

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += ball_vx
        ball.rect.y += ball_vy

        if ball.rect.y > height - 50 or ball.rect.y < 0:
            ball_vy *= -1

        if sprite.collide_rect(ball, pl_right) or sprite.collide_rect(ball, pl_left):
            ball_vx *= -1

        if ball.rect.x < 0:
            num_right += 1

        if ball.rect.x > width - 50:
            num_left += 1

        if ball.rect.x < 0 or ball.rect.x > width - 50:
            sleep(2)
            ball.rect.x = 450
            ball.rect.y = 350       
            ball_vx *= -1

        pl_left.update_left()
        pl_right.update_right()
        right = font1.render(str(num_right), True, (0,0,0))
        left = font1.render(str(num_left), True, (0,0,0))

    display.update()
    clock.tick(FPS)
