import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ИГРА')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        pygame.display.flip()
    pygame.quit()