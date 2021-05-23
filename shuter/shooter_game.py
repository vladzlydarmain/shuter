from pygame import *

#создай окно игры
window = display.set_mode((800,600))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"),(800,600))
#задай фон сцены

clock = time.Clock()
FPS = 100


#создай 2 спрайта и размести их на сцене
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
#обработай событие «клик по кнопке "Закрыть окно"»
class Player(sprite.Sprite):
    def __init__(self,picture,speed,sx,sy,window):
        self.picture = picture
        self.speed = speed
        self.sx = sx
        self.sy = sy
        self.sub = transform.scale(image.load(self.picture),(100,100))
        self.window = window
    def update(self):
        self.window.blit(self.sub,(self.sx,self.sy))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.sx < 800:
            self.sx += self.speed
        if keys_pressed[K_a] and self.sx >0:
            self.sx -= self.speed
x = 3
y = 500
game = True
player = Player("rocket.png",10,x,y,window)


while game:
    window.blit(background,(0,0))
    player.update()
    for e in event.get():
        if e.type == QUIT:
            game=False
    clock.tick(FPS)
