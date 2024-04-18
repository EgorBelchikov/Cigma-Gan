from pygame import *
init()
wight = 900
hight = 500
mw = display.set_mode((wight,hight))
bg = image.load("Без имени4.png")
bg = transform.scale(bg, (wight,hight))
class Rosket(sprite.Sprite):
    def __init__(self, img, x,y, wight_rocket,hight_rocket,speed):
        self.image = transform.scale(image.load(img),(wight_rocket,hight_rocket))
        self.image_hit = self.image.get_rect()
        self.image_hit.x = x
        self.image_hit.y = y
        self.speed = speed

    def show_s(self):
        mw.blit(self.image,(self.image_hit.x, self.image_hit.y))
        
    
class Rosket_player1(Rosket):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.image_hit.y > 5:
            self.image_hit.y -= self.speed
        if keys[K_DOWN] and self.image_hit.y < wight - 80:
            self.image_hit.y += self.speed 

class Rosket_player2(Rosket):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.image_hit.y > 5:
            self.image_hit.y -= self.speed
        if keys[K_s] and self.image_hit.y < wight - 80:
            self.image_hit.y += self.speed 

Rosket1 = Rosket_player1('Без имени2.png',30,200,25,150,4)
Rosket2 = Rosket_player2('Без имени3.png',wight - 55,200,25,150,4)
ball = Rosket('Без имени.png',200,200,50,50,4)

speed_x = 3
speed_y = 3

fps = time.Clock()
game = True 
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    mw.blit(bg,(0,0))
    Rosket1.show_s()
    Rosket2.show_s()
    ball.show_s()
    Rosket1.update_r()
    Rosket2.update_l()

    if Rosket1.ro or sprite.collide_rect(Rosket2,ball):
        speed_x *= -1
        speed_y *= 1
    
    if ball.image_hit.y  < 10:
        speed_y *= -1
    if ball.image_hit.y  > 870:
        speed_y *= 1
    



    ball.image_hit.x += speed_x
    ball.image_hit.y += speed_y

    display.update()
    fps.tick(60)
