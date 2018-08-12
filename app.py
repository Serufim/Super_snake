import os, sys
import pygame
from pygame.locals import *

#ну тут понятно если у нас нет модулей, то мы ругаемся на это
if not pygame.font: print('Аааа у нас шрифтов нема((')
if not pygame.mixer: print('Надеюсь вы не глухой. а то у нас нету музыки ;_;')

# Функция хелпер, помогает нам грузить изображения берет все на себя, в общем-то
def load_image(name,colorkey=None):
    # Получаем путь картинки
    fullname = os.path.join('data',name)
    try:
        # Пытаемся загрузить
        image = pygame.image.load(fullname)
    except pygame.error:
        # Если не можем, то пишем что у нас проблемы
        print('Не могу загрузить твою картинку',name)
        raise SystemExit
    # Если все получилось, то конвертируем изображение, хз что там внутри
    image = image.convert()
    # Тут у нас типа короч такая тема, что мы задаем какую-то штуку типа фона, хз точно и если ее нет то пофиг если -1
    # то белем топ левый пиксель и заливаем им все что есть
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image, image.get_rect()

#Соотвественно грузим музыку, практически то же самое что и изображениями
def load_sound(name):
    # Прокси класс и если не будет поддержки звуков, то мы загрузим короч этот класс с заглушкой
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    # Имя файлв
    fullname = os.path.join('data',name)
    try:
        # Грузим иначе все плохо
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Не могу загрузить звуки')
        raise SystemExit
    return sound

# Класс Кулака который пиздит обезьян
class Fist(pygame.sprite.Sprite):

    def __init__(self):
        # Грузим короч родительский класс
        pygame.sprite.Sprite.__init__(self)
        # Сейчас будем грузить изображение в img изобаржение а в rect будет размеры
        self.image, self.rect = load_image('fist.bmp',-1)
        # Это короч будет переменная которая говорит ебнули макаку или нет
        self.punching = 0

    def update(self):
        # Получаем координаты мыши
        pos = pygame.mouse.get_pos()
        # Вродь как сдвигаем центр изображения туда где сейчас наша мышка
        self.rect.midtop = pos
        #Когда бьем сдвигаем изображение
        if self.punching:
            self.rect.move_ip(5,10)

    def punch(self, target):
        #Если бьем, то короч проверяем попадание через colliderect
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5,-5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        # Возвращаем кулак в обычное состояние
        self.punching = 0

class Chimp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('chimp.bmp',-1)
        screen = pygame.display.get_surface()
        # хз чо такое area вродь область, думаю это локальная переменная которая говорит что вот тут область по которой
        # макака
        self.area = screen.get_rect()
        self.rect.topleft = 10,10
        # скрость передвижения
        self.move = 1
        # Ебнули или нет макаку
        self.dizzy = 0

    def update(self):
        # Если ебнули, то крутимся, не ебнули значит гуляем
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        "move the monkey across the screen, and turn at the ends"
        # Новая позиция, мы перемещаем на 9 пикселей по горизонтали, и на 0 по Y
        newpos = self.rect.move((self.move, 0))
        # Проверяем короч если мы пересекаем экран, то разворачиваемся и меняем скорость
        if self.rect.left < self.area.left or \
            self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        # Получаем центр
        center = self.rect.center
        # Это мы крутим макаку по 12 градусов за раз
        self.dizzy += 1
        # Как накрутимся так сразу ставим обычное изображение
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            # Иначе короч мы берем и крутим
             rotate = pygame.transform.rotate
             self.image = rotate(self.original,self.dizzy)
        # Ставим центр изображения куда надо
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        # Если обезьяну ебнули, то она короч пока до конца не прокрутится будет крутиться
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((468, 60))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()
    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    chimp = Chimp()
    fist = Fist()
    allsprites = pygame.sprite.RenderPlain((fist, chimp))


#Main Loop
    going = True
    while going:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            elif event.type == MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play() #punch
                    chimp.punched()
                else:
                    whiff_sound.play() #miss
            elif event.type == MOUSEBUTTONUP:
                fist.unpunch()

        allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
