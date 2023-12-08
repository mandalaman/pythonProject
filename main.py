import pygame
from pygame.locals import *

def draw_block():
    surface.fill((50, 168, 82))
    surface.blit(block,(block_x, block_y))

    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((50, 168, 82))
    block = pygame.image.load('resource/block.jpg').convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x, block_y))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
                if event.key == K_UP:
                    block_y = block_y - 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y = block_y + 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x = block_x - 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x = block_x + 10
                    draw_block()

            elif event.type == QUIT:
                running = False


