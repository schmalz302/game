import os
import sys
import pygame


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, ' '), level_map))


pygame.init()
lev = load_level('level1.txt')
size = width, height = 900, 700
screen = pygame.display.set_mode(size)
FPS = 50
clock = pygame.time.Clock()


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


def menu(aa, b, c):
    fon = pygame.transform.scale(load_image('menu00.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(aa, 6, 3), Button(b, 6, 6), Button(c, 6, 9)]
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
                    return True
                elif 300 <= mouse[0] <= 590 and 300 <= mouse[1] <= 375:
                    Setting()
                    a[1].upd()
                elif 300 <= mouse[0] <= 590 and 450 <= mouse[1] <= 525:
                    return False
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        button_group.draw(screen)
        clock.tick(FPS)


def Setting():
    fon = pygame.transform.scale(load_image('menu00.png'), (width, height))
    screen.blit(fon, (0, 0))
    a = [Button(7, 6, 3), Button(4, 6, 5), Button(5, 6, 7), Button(6, 6, 9)]
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
                    a[2].upd()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 300 <= mouse[0] <= 590 and 150 <= mouse[1] <= 225:
                    return
                elif 300 <= mouse[0] <= 590 and 250 <= mouse[1] <= 325:
                    a[1].upd()
                elif 300 <= mouse[0] <= 590 and 350 <= mouse[1] <= 425:
                    a[2].upd()
                elif 300 <= mouse[0] <= 590 and 450 <= mouse[1] <= 525:
                    a[2].upd()
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        setting_group.draw(screen)
        clock.tick(FPS)


class Button(pygame.sprite.Sprite):
    def __init__(self, a, pos_x, pos_y):
        if a in [4, 5, 6, 7]:
            super().__init__(setting_group)
        else:
            super().__init__(button_group)
        self.c = a
        self.a = load_image(f'menu{a}.png')
        self.b = load_image(f'menu{a}{a}.png')
        self.image = self.a
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def upd(self):
        if self.image == self.a:
            self.image = self.b
        else:
            self.image = self.a


tile_images = {
    'wall': load_image('dirtMid.png'),
    'empty': load_image('grass2.png'),
    'blok': load_image('grass2.png'),
    'dirtCenter': load_image('dirtCenter.png'),
    'dirtLeft': load_image('dirtLeft.png'),
    'dirtRight': load_image('dirtRight.png'),
    'dirt': load_image('dirt.png'),
    'dirtCliff_left': load_image('dirtCliff_left.png'),
    'dirtCliff_right': load_image('dirtCliff_right.png'),
}
player_image = load_image('bunny1_stand.png')
player_image2 = load_image('bunny1_walk1.png')
player_image3 = load_image('bunny1_walk2.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type != 'empty':
            a_group.add(self)
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
        self.a = ['gold_1.png', 'gold_2.png', 'gold_3.png', 'gold_4.png', 'gold_6.png', 'gold_5.png']
        self.c = 0
        self.b = 0
        self.image = load_image(self.a[self.b])
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)

    def update(self):
        self.c += 1
        if self.c % 3 == 0:
            self.b += 1
            self.image = load_image(self.a[self.b % len(self.a)])


class Life(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.a = ['05.png', '04.png', '03.png', '02.png', '01.png', '00.png']
        self.c = 0
        self.image = load_image(self.a[self.c])
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def upd(self):
        self.c += 1
        self.image = load_image(self.a[self.c])


class Number(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.a = ['0.png', '1.png', '2.png', '3.png', '4.png',
                  '5.png', '6.png', '7.png', '8.png', '9.png']
        self.image = load_image(self.a[0])
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def upd(self, c):
        self.image = load_image(self.a[c])


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
        super().__init__(player_group, all_sprites)
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
        self.cc = ['bunny2_stand.png', 'bunny3_stand.png']
        self.bb = 0
        self.m = False
        self.money = 0

    def update(self):
        self.c += 1
        a = pygame.sprite.spritecollideany(self, red_enemy)
        if a:
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
            self.money += 1
            m = list(str(self.money))
            if len(m) == 1:
                m = [str(0)] + m
            num1.upd(int(m[0]))
            num2.upd(int(m[1]))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ' ':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '0':
                Tile('dirtCenter', x, y)
            elif level[y][x] == '7':
                Tile('empty', x, y)
                Gold(x, y)
            elif level[y][x] == '1':
                Tile('dirtLeft', x, y)
            elif level[y][x] == '2':
                Tile('dirtRight', x, y)
            elif level[y][x] == '3':
                Tile('dirtCliff_left', x, y)
            elif level[y][x] == '4':
                Tile('dirtCliff_right', x, y)
            elif level[y][x] == '5':
                Tile('dirt', x, y)
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
    life = Life(0, 0)
    mon, num1, num2, = Money(0, 1), Number(0.85, 1.1), Number(1.5, 1.1)
    return new_player, x, y, life, num1, num2


def background_generation(background):
    for i in background:
        screen.blit(i, (0, 0))


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
red_enemy = pygame.sprite.Group()
player_group = pygame.sprite.Group()
a_group = pygame.sprite.Group()
b_group = pygame.sprite.Group()
gold_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()
setting_group = pygame.sprite.Group()
running = True
pygame.display.set_caption('Перемещение героя')
camera = Camera()
player, level_x, level_y, life, num1, num2 = generate_level(lev)
u, d, l, r = False, False, False, False
background = [pygame.transform.scale(load_image(f'bg_layer{i + 1}.png'), (width, height))
              for i in range(4)]
background_generation(background)
running = menu(1, 2, 3)
while running:
    background_generation(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                u = False
            if event.key == pygame.K_RIGHT:
                r = False
            if event.key == pygame.K_LEFT:
                l = False
    # cвободное падение
    player.rect.y += 10
    a = pygame.sprite.spritecollideany(player, a_group)
    if a:
        player.rect.y -= 10
    if not player.m:
        # перемещение:
        # прыжок
        if u and up < 4:
            up += 1
            player.rect.y -= 40
            a = pygame.sprite.spritecollideany(player, a_group)
            if a:
                player.rect.y += 40
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
                player.rect.x -= 10
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
                player.rect.x += 10
        # просто стоит на месте
        if not l and not r:
            player.image = player.image1
    # обновляем положение всех спрайтов и отрисовываем
    all_sprites.update()
    camera.update(player)
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    for sprite in all_sprites:
        if sprite.__class__.__name__ not in ['Number', 'Money', 'Life']:
            camera.apply(sprite)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
