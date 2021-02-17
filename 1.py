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
size = width, height = len(lev[0]) * 50, len(lev) * 50
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
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


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


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


tile_images = {
    'wall': load_image('dirtMid.png'),
    'empty': load_image('grass2.png')

}
player_image = load_image('bunny1_stand.png')
player_image2 = load_image('bunny1_walk1.png')
player_image3 = load_image('bunny1_walk2.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type == 'wall':
            a_group.add(self)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


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


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ' ':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def background_generation(background):
    for i in background:
        screen.blit(i, (0, 0))


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
a_group = pygame.sprite.Group()
b_group = pygame.sprite.Group()
running = True
pygame.display.set_caption('Перемещение героя')
start_screen()
camera = Camera()
player, level_x, level_y = generate_level(lev)
u, d, l, r = False, False, False, False
background = [pygame.transform.scale(load_image(f'bg_layer{i + 1}.png'), (width, height))
              for i in range(4)]
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
    player.rect.y += 5
    a = pygame.sprite.spritecollideany(player, a_group)
    if a:
        player.rect.y -= 5
    # перемещение:
    # прыжок
    if u and up < 8:
        up += 1
        player.rect.y -= 15
        a = pygame.sprite.spritecollideany(player, a_group)
        if a:
            player.rect.y += 15
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
    # обновляем положение всех спрайтов
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
