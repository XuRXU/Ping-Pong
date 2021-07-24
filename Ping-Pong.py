from pygame import *
from random import randint
 
#backgournd music
mixer.init()
mixer.music.load('Space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font1 = font.Font(None,80)
font2 = font.Font(None,36)
win = font1.render("YOU WIN", True,(255,255,255))
lose  = font1.render("YOU LOSE", True,(180,0,0))

#we need the following images:
img_back = "galaxy.jpg" #game background
img_paddle = "rocket.png" #hero
img_paddle2 = "ufo.png"
img_ball = "bullet.png"


score = 0
lost = 0
 
#parent class for other sprites
class GameSprite(sprite.Sprite):
 #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)
 
       #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
       #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #ToDO method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
#//!main player class
class Player(GameSprite):
   #method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
        
class Player2(GameSprite):
   #method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed

#Create a window
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
#create sprites
paddle = Player(img_, 5, win_height - 100, 80, 100, 10)
paddle2 = Player(img_, 5, win_height - 100, 80, 100, 10)
#the "game is over" variable: as soon as True is there, sprites stop working in the main loop
finish = False
#Main game loop:
run = True #the flag is reset by the window close button
while run:
   #"Close" button press event
    if not finish:
       #update the background
        window.blit(background,(0,0))

        text = font2.render("Score: "+str(score),1,(255,255,255))
        window.blit(text,(10,20))
        text2 = font2.render("Missed: "+str(lost),1,(255,255,255))
        window.blit(text2,(10,3))

 
       #launch sprite movements
        paddle.update()
        paddle2.update()
        asteriods.update()
        bullets.update()
       #update them in a new location in each loop iteration
        ship.reset()
        ufos.draw(window)
        asteriods.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(bullets,ufos,True,True)
        for c in collides:
            score = score + 1
            enemy = Enemy(img_ufo, randint(80, win_width-80),0, 40, 40, randint(1,10))
            ufos.add(enemy)
            asteriod = Enemy(img_meteor, randint(80, win_width-80),0, 40, 40, randint(1,10))
            asteriods.add(asteriod)
        if sprite.spritecollide(ship, asteriods, False) or lost > 5:
            finish = True
            window.blit(lose, (200,200))
        if score == 21:
            finish = True
            window.blit(win, (255,215))
 
        display.update()

    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for u in ufos:
            u.kill()
        time.delay(3000)
        for i in range (5):
            enemy = Enemy(img_ufo, randint(80, win_width-80),0, 40, 40, randint(1,3))
            ufos.add(enemy)
   #the loop is executed each 0.05 sec
    time.delay(50)
