import os
import sys
import pygame
from os import path


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, ' '), level_map))


pygame.init()
size = width, height = 900, 700
tile_width = tile_height = 50
screen = pygame.display.set_mode(size)
FPS = 50
clock = pygame.time.Clock()
pygame.display.set_caption('тип марио')


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x - width // 2)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def menu():
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    fon = pygame.transform.scale(load_image('menu00.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(1, 6, 3, 'menu'), Button(2, 6, 6, 'menu'), Button(3, 6, 9, 'menu')]
    aa, bb, cc = 0, 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse[0] <= 590 and 150 <= mouse[1] <= 225:
                    a[0].upd()
                elif 300 <= mouse[0] <= 590 and 300 <= mouse[1] <= 375:
                    a[1].upd()
                elif 300 <= mouse[0] <= 590 and 450 <= mouse[1] <= 525:
                    a[2].upd()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 150 <= mouse[1] <= 225:
                    sound2.play()
                    return aa, bb, cc
                elif 300 <= mouse[0] <= 590 and 300 <= mouse[1] <= 375:
                    sound2.play()
                    aa, bb, cc = Setting(aa, bb, cc)
                    a[1].upd()
                elif 300 <= mouse[0] <= 590 and 450 <= mouse[1] <= 525:
                    sound2.play()
                    terminate()
        pygame.display.flip()
        screen.blit(pygame.transform.scale(load_image('fon/fon1.png'), (width, height)), (0, 0))
        screen.blit(fon, (0, 0))
        button_group.draw(screen)
        clock.tick(FPS)


def Setting(aa, bb, cc):
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    fon = pygame.transform.scale(load_image('menu00.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(7, 6, 3, 'setting'), Button(4, 6, 5, 'setting'),
         Button(5, 6, 7, 'setting'), Button(6, 6, 9, 'setting')]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse[0] <= 590 and 150 <= mouse[1] <= 225:
                    a[0].upd()
                elif 300 <= mouse[0] <= 590 and 250 <= mouse[1] <= 325:
                    a[1].upd()
                elif 300 <= mouse[0] <= 590 and 350 <= mouse[1] <= 425:
                    a[2].upd()
                elif 300 <= mouse[0] <= 590 and 450 <= mouse[1] <= 525:
                    a[3].upd()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 150 <= mouse[1] <= 225:
                    sound2.play()
                    return aa, bb, cc
                elif 300 <= mouse[0] <= 590 and 250 <= mouse[1] <= 325:
                    sound2.play()
                    aa = Character(aa)
                    a[1].upd()
                elif 300 <= mouse[0] <= 590 and 350 <= mouse[1] <= 425:
                    sound2.play()
                    bb = Surface(bb)
                    a[2].upd()
                elif 300 <= mouse[0] <= 590 and 450 <= mouse[1] <= 525:
                    sound2.play()
                    cc = Fon(cc)
                    a[3].upd()
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        setting_group.draw(screen)
        clock.tick(FPS)


def Character(aa):
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    sound = pygame.mixer.Sound('data/click1.ogg')
    fon = pygame.transform.scale(load_image('menu000.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(7, 6, 2.5, 'character'), Button(8, 6, 4.2, 'character'), Button(8, 11.04, 4.2, 'character')]
    a[aa + 1].upd()
    gg = a[aa + 1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse[0] <= 590 and 125 <= mouse[1] <= 200:
                    a[0].upd()
                if 300 <= mouse[0] <= 338 and 210 <= mouse[1] <= 246:
                    gg.upd()
                    sound.play()
                    gg = a[1]
                    a[1].upd()
                if 552 <= mouse[0] <= 590 and 210 <= mouse[1] <= 246:
                    gg.upd()
                    sound.play()
                    gg = a[2]
                    a[2].upd()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 125 <= mouse[1] <= 200:
                    sound2.play()
                    return a.index(gg) - 1
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        character_group.draw(screen)
        clock.tick(FPS)


def Surface(bb):
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    sound = pygame.mixer.Sound('data/click1.ogg')
    fon = pygame.transform.scale(load_image('menu001.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(7, 6, 2.5, 'surface'), Button(8, 5.75, 4.5, 'surface'), Button(8, 8.58, 4.5, 'surface'),
         Button(8, 11.41, 4.5, 'surface'), Button(8, 5.75, 8.07, 'surface'), Button(8, 8.58, 8.07, 'surface'),
         Button(8, 11.41, 8.07, 'surface')]
    a[bb + 1].upd()
    gg = a[bb + 1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse[0] <= 590 and 125 <= mouse[1] <= 200:
                    gg.upd()
                elif 288 <= mouse[0] <= 326 and 225 <= mouse[1] <= 261:
                    gg.upd()
                    sound.play()
                    gg = a[1]
                    a[1].upd()
                elif 429 <= mouse[0] <= 467 and 225 <= mouse[1] <= 261:
                    gg.upd()
                    sound.play()
                    gg = a[2]
                    a[2].upd()
                elif 570 <= mouse[0] <= 608 and 225 <= mouse[1] <= 261:
                    gg.upd()
                    sound.play()
                    gg = a[3]
                    a[3].upd()
                elif 288 <= mouse[0] <= 326 and 404 <= mouse[1] <= 440:
                    gg.upd()
                    sound.play()
                    gg = a[4]
                    a[4].upd()
                elif 429 <= mouse[0] <= 467 and 404 <= mouse[1] <= 440:
                    gg.upd()
                    sound.play()
                    gg = a[5]
                    a[5].upd()
                elif 570 <= mouse[0] <= 608 and 404 <= mouse[1] <= 440:
                    gg.upd()
                    sound.play()
                    gg = a[6]
                    a[6].upd()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 125 <= mouse[1] <= 200:
                    sound2.play()
                    return a.index(gg) - 1
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        surface_group.draw(screen)
        clock.tick(FPS)


def Fon(cc):
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    sound = pygame.mixer.Sound('data/click1.ogg')
    fon = pygame.transform.scale(load_image('menu0000.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(7, 6, 2.5, 'fon'), Button(8, 6.17, 4.5, 'fon'), Button(8, 11.07, 4.5, 'fon'),
         Button(8, 6.17, 7.98, 'fon'), Button(8, 11.07, 7.98, 'fon')]
    a[cc + 1].upd()
    gg = a[cc + 1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse[0] <= 590 and 125 <= mouse[1] <= 200:
                    gg.upd()
                elif 309 <= mouse[0] <= 347 and 225 <= mouse[1] <= 251:
                    gg.upd()
                    sound.play()
                    gg = a[1]
                    a[1].upd()
                elif 554 <= mouse[0] <= 592 and 225 <= mouse[1] <= 251:
                    gg.upd()
                    sound.play()
                    gg = a[2]
                    a[2].upd()
                elif 309 <= mouse[0] <= 347 and 399 <= mouse[1] <= 435:
                    gg.upd()
                    sound.play()
                    gg = a[3]
                    a[3].upd()
                elif 554 <= mouse[0] <= 592 and 399 <= mouse[1] <= 435:
                    gg.upd()
                    sound.play()
                    gg = a[4]
                    a[4].upd()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 125 <= mouse[1] <= 200:
                    sound2.play()
                    return a.index(gg) - 1
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        fon_group.draw(screen)
        clock.tick(FPS)


def Pause():
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    fon = pygame.transform.scale(load_image('menu00.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(9, 6, 4, 'pause'), Button(3, 6, 8, 'pause')]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse[0] <= 590 and 200 <= mouse[1] <= 275:
                    a[0].upd()
                    sound2.play()
                elif 300 <= mouse[0] <= 590 and 400 <= mouse[1] <= 475:
                    a[1].upd()
                    sound2.play()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 200 <= mouse[1] <= 275:
                    a[0].upd()
                    return
                elif 300 <= mouse[0] <= 590 and 400 <= mouse[1] <= 475:
                    a[1].upd()
                    terminate()
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        pause_group.draw(screen)
        clock.tick(FPS)


def Game_over(a):
    sound2 = pygame.mixer.Sound('data/rollover1.wav')
    fon = pygame.transform.scale(load_image(a), (width, height))
    fon1 = pygame.transform.scale(load_image('menu00.png'), (width, height))
    a = [Button('a', 6, 4, 'game_over'), Button(3, 6, 8, 'game_over')]
    c = 0
    while True:
        c += 1
        if c < 150:
            screen.blit(fon, (0, 0))
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if 300 <= mouse[0] <= 590 and 200 <= mouse[1] <= 275:
                        a[0].upd()
                        sound2.play()
                    elif 300 <= mouse[0] <= 590 and 400 <= mouse[1] <= 475:
                        a[1].upd()
                        sound2.play()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 300 <= mouse[0] <= 590 and 200 <= mouse[1] <= 275:
                        a[0].upd()
                        return
                    elif 300 <= mouse[0] <= 590 and 400 <= mouse[1] <= 475:
                        a[1].upd()
                        terminate()
            screen.blit(fon1, (0, 0))
            game_over_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


class Button(pygame.sprite.Sprite):
    def __init__(self, a, pos_x, pos_y, c):
        if c == 'setting':
            super().__init__(setting_group)
        elif c == 'character':
            super().__init__(character_group)
        elif c == 'menu':
            super().__init__(button_group)
        elif c == 'surface':
            super().__init__(surface_group)
        elif c == 'fon':
            super().__init__(fon_group)
        elif c == 'pause':
            super().__init__(pause_group)
        elif c == 'p':
            super().__init__(all_sprites)
        elif c == 'game_over':
            super().__init__(game_over_group)
        self.c = a
        self.a = load_image(f'menu1/menu{a}.png')
        self.b = load_image(f'menu2/menu{a}{a}.png')
        self.image = self.a
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def upd(self):
        if self.image == self.a:
            self.image = self.b
        else:
            self.image = self.a


a = ['.png', 'Center.png', 'Cliff_left.png', 'Cliff_right.png',
     'Left.png', 'Mid.png', 'Right.png']
tile_images = {
    'dirt': [load_image(f'dirt/dirt{i}') for i in a],
    'snow': [load_image(f'snow/snow{i}') for i in a],
    'stone': [load_image(f'stone/stone{i}') for i in a],
    'grass': [load_image(f'grass/grass{i}') for i in a],
    'planet': [load_image(f'planet/planet{i}') for i in a],
    'sand': [load_image(f'sand/sand{i}') for i in a],
    'empty': load_image('grass2.png'),
    'blok': load_image('grass2.png'),
    'abyss': load_image('grass2.png'),
    'l': load_image('grass2.png'),
    'chek': load_image('sign.png')}


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, pos_blok=None):
        super().__init__(all_sprites)
        if tile_type == 'l':
            l_group.add(self)
        elif tile_type == 'abyss':
            abyss_group.add(self)
        elif tile_type == 'chek':
            chek_group.add(self)
        elif tile_type not in ['empty', 'abyss']:
            a_group.add(self)
        if pos_blok is not None:
            self.image = tile_images[tile_type][pos_blok]
        else:
            self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Red_enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, red_enemy)
        self.a = ['spikeMan_walk1.png', 'spikeMan_walk2.png']
        self.a2 = ['spikeMan_walk3.png', 'spikeMan_walk4.png']
        self.c, self.b = 0, 0
        self.image = load_image(self.a[self.b])
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y - 4)
        self.m = self.a
        self.v = 5

    def update(self):
        self.c += 1
        if self.c % 3 == 0:
            self.b += 1
            self.image = load_image(self.m[self.b % 2])
        self.rect.x += self.v
        a = pygame.sprite.spritecollideany(self, a_group)
        if a:
            self.v = -self.v
            if self.m == self.a:
                self.m = self.a2
            else:
                self.m = self.a


class Gold(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(gold_group, all_sprites)
        self.a = [load_image(f'gold/gold_{i + 1}.png') for i in range(6)]
        self.c = 0
        self.b = 0
        self.image = self.a[self.b]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)

    def update(self):
        self.c += 1
        if self.c % 3 == 0:
            self.b += 1
            self.image = self.a[self.b % len(self.a)]


class Life(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.a = [load_image(f'life/0{5 - i}.png') for i in range(6)]
        self.c = 0
        self.image = self.a[self.c]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def upd(self):
        self.c += 1
        self.image = self.a[self.c]


class Number(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.a = [load_image(f'number/{i}.png') for i in range(10)]
        self.image = self.a[0]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def upd(self, c):
        self.image = self.a[c]


class Money(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = load_image('money_table.png')
        self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)


class Yellow_enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, red_enemy)
        self.a = ['wingMan1.png', 'wingMan2.png', 'wingMan3.png', 'wingMan4.png', 'wingMan5.png']
        self.c, self.b = 0, 0
        self.image = load_image(self.a[self.b])
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y - 4)
        self.v = 5

    def update(self):
        self.c += 1
        self.rect.y += self.v
        if self.c % 3 == 0:
            self.b += 1
            self.image = load_image(self.a[self.b % len(self.a)])
        a = pygame.sprite.spritecollideany(self, a_group)
        if a or self.rect.y < 0:
            self.v = -self.v


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        # изображения для анимации
        self.image1 = player_image
        self.image2 = player_image2
        self.image3 = player_image3
        self.image4 = pygame.transform.flip(player_image2, True, False)
        self.image5 = pygame.transform.flip(player_image3, True, False)
        self.image = self.image1
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.c = 0
        self.b = 0
        self.cc = ['bunny4_stand.png', 'bunny5_stand.png']
        self.bb = 0
        self.m = False
        self.money = 0
        self.sound = pygame.mixer.Sound('data/cloth1.mp3')
        self.sound2 = pygame.mixer.Sound('data/марио.mp3')
        self.sound2.set_volume(0.1)
        self.x, self.y = self.rect.x, self.rect.y
        self.check = []

    def update(self):
        self.c += 1
        a = pygame.sprite.spritecollideany(self, red_enemy)
        if a:
            if not self.m:
                self.sound.play()
            self.b = 0
            self.m = True
        if self.m:
            if self.b != 3:
                if self.c % 2 == 0:
                    self.b += 1
                    self.bb += 1
                    self.image = load_image(self.cc[self.bb % 2])
            else:
                life.upd()
                self.m = False
                self.b = 0
        a = pygame.sprite.spritecollide(self, gold_group, True)
        if a:
            self.sound2.play()
            self.money += 1
            m = list(str(self.money))
            if len(m) == 1:
                m = [str(0)] + m
            num1.upd(int(m[0]))
            num2.upd(int(m[1]))
        a = pygame.sprite.spritecollideany(self, chek_group)
        if a:
            self.check.append(a)


def generate_level(level, bb):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ' ':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile(bb, x, y, 5)
            elif level[y][x] == '0':
                Tile(bb, x, y, 1)
            elif level[y][x] == '7':
                Tile('empty', x, y)
                Gold(x, y)
            elif level[y][x] == '1':
                Tile(bb, x, y, 4)
            elif level[y][x] == '2':
                Tile(bb, x, y, 6)
            elif level[y][x] == '3':
                Tile(bb, x, y, 2)
            elif level[y][x] == '4':
                Tile(bb, x, y, 3)
            elif level[y][x] == '5':
                Tile(bb, x, y, 0)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '8':
                Tile('empty', x, y)
                Red_enemy(x, y)
            elif level[y][x] == '9':
                Tile('empty', x, y)
                Yellow_enemy(x, y)
            elif level[y][x] == '*':
                Tile('blok', x, y)
            elif level[y][x] == '6':
                Tile('abyss', x, y)
            elif level[y][x] == 'g':
                Tile('chek', x, y)
            elif level[y][x] == 'l':
                Tile('l', x, y)
    life = Life(0, 0)
    mon, num1, num2, = Money(0, 1), Number(0.85, 1.1), Number(1.5, 1.1)
    button = Button(10, 15, 0, 'p')
    return new_player, x, y, life, num1, num2, button


# все группы спрайтов
all_sprites = pygame.sprite.Group()
red_enemy = pygame.sprite.Group()
a_group = pygame.sprite.Group()
gold_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()
setting_group = pygame.sprite.Group()
character_group = pygame.sprite.Group()
surface_group = pygame.sprite.Group()
pause_group = pygame.sprite.Group()
fon_group = pygame.sprite.Group()
abyss_group = pygame.sprite.Group()
chek_group = pygame.sprite.Group()
l_group = pygame.sprite.Group()
game_over_group = pygame.sprite.Group()
sprites = [all_sprites, red_enemy, a_group, gold_group, button_group, setting_group,
           character_group, surface_group, pause_group, fon_group, abyss_group, chek_group, game_over_group, l_group]
running = True
camera = Camera()
u, d, l, r, upbool = False, False, False, False, False
# заставка
sound1 = pygame.mixer.Sound('data/C418-Key.wav')
s = sound1.play(-1)
aa, bb, cc = menu()
s.pause()
sound = pygame.mixer.Sound('data/для уровня.mp3')
sound.set_volume(0.4)
ss = sound.play(-1)
sound2 = pygame.mixer.Sound('data/марио прыжок.mp3')
sound2.set_volume(0.2)
player_image = load_image(f'bunny{aa + 1}/bunny{aa + 1}_stand.png')
player_image2 = load_image(f'bunny{aa + 1}/bunny{aa + 1}_walk1.png')
player_image3 = load_image(f'bunny{aa + 1}/bunny{aa + 1}_walk2.png')
fon = pygame.transform.scale(load_image(f'fon/fon{cc + 1}.png'), (width, height))
b = ['dirt', 'snow', 'sand', 'grass', 'stone', 'planet']
player, level_x, level_y, life, num1, num2, button = generate_level(load_level('level1.txt'), b[bb])
while running:
    screen.blit(fon, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if upbool:
                    sound2.play()
                    up = 0
                    u = True
            if event.key == pygame.K_RIGHT:
                r = True
                rg = 0
                rbl = False
            if event.key == pygame.K_LEFT:
                l = True
                lg = 0
                lbl = False
            player.y = player.rect.y
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 750 <= mouse[0] <= 900 and 0 <= mouse[1] <= 70:
                button.upd()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if 750 <= mouse[0] <= 900 and 0 <= mouse[1] <= 70:
                ss.pause()
                s.unpause()
                Pause()
                s.pause()
                ss.unpause()
                button.upd()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                u = False
            if event.key == pygame.K_RIGHT:
                r = False
            if event.key == pygame.K_LEFT:
                l = False
    if life.c == 5 or pygame.sprite.spritecollideany(player, l_group):
        ss.pause()
        s.unpause()
        if life.c == 5:
            Game_over('GAME_OVER.png')
        else:
            Game_over('congrats.png')
        u, d, l, r, upbool = False, False, False, False, False
        for i in sprites:
            for j in i:
                i.remove(j)
        aa, bb, cc = menu()
        s.pause()
        ss.unpause()
        player_image = load_image(f'bunny{aa + 1}/bunny{aa + 1}_stand.png')
        player_image2 = load_image(f'bunny{aa + 1}/bunny{aa + 1}_walk1.png')
        player_image3 = load_image(f'bunny{aa + 1}/bunny{aa + 1}_walk2.png')
        fon = pygame.transform.scale(load_image(f'fon/fon{cc + 1}.png'), (width, height))
        player, level_x, level_y, life, num1, num2, button = generate_level(load_level('level1.txt'), b[bb])
    if pygame.sprite.spritecollideany(player, abyss_group):
        life.upd()
        player.rect.x = player.check[-1].rect.x
        player.rect.y = player.check[-1].rect.y - 30
    # cвободное падение
    player.rect.y += 15
    a = pygame.sprite.spritecollideany(player, a_group)
    if a:
        upbool = True
        while a:
            player.rect.y -= 1
            a = pygame.sprite.spritecollideany(player, a_group)
    else:
        upbool = False
    if not player.m:
        # перемещение:
        # прыжок
        if u and up < 4:
            up += 1
            player.rect.y -= 65
            a = pygame.sprite.spritecollideany(player, a_group)
            if a:
                while a:
                    player.rect.y += 1
                    a = pygame.sprite.spritecollideany(player, a_group)
        # право
        if r:
            rg += 1
            if rg % 3 == 0:
                if rbl:
                    rbl = False
                    player.image = player.image2
                else:
                    rbl = True
                    player.image = player.image3
            player.rect.x += 10
            a = pygame.sprite.spritecollideany(player, a_group)
            if a:
                while a:
                    player.rect.x -= 1
                    a = pygame.sprite.spritecollideany(player, a_group)
        # лево
        if l:
            lg += 1
            if lg % 3 == 0:
                if lbl:
                    lbl = False
                    player.image = player.image4
                else:
                    lbl = True
                    player.image = player.image5
            player.rect.x -= 10
            a = pygame.sprite.spritecollideany(player, a_group)
            if a:
                while a:
                    player.rect.x += 1
                    a = pygame.sprite.spritecollideany(player, a_group)
        # просто стоит на месте
        if not l and not r:
            player.image = player.image1
    # обновляем положение всех спрайтов и отрисовываем
    all_sprites.update()
    camera.update(player)
    all_sprites.draw(screen)
    for sprite in all_sprites:
        if sprite.__class__.__name__ not in ['Number', 'Money', 'Life', 'Button']:
            camera.apply(sprite)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
